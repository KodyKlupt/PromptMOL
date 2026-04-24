"""
PromptMol — natural-language PyMOL assistant.

Commands registered in the PyMOL command line:
  pm [--dry] [--save [filename]] [--outdir /path] [--model name] <prompt>
  pmundo                                    restore scene to before last command
  pmsetup                                   interactive first-run setup wizard
  pmsetup lmstudio                          configure LM Studio backend
  pmsetup openai <api_key>                  configure OpenAI backend
  pmsetup anthropic <api_key>               configure Anthropic backend
  pmcfg set <key> <value>                   configure any individual setting
  pmcfg show                                print current config
  pmreset                                   clear conversation history and log
  pmsave [filename]                         save last generated script
  pmlog show                                print session log to console
  pmlog save [filename]                     save full session log as .py script
  pmlog export [filename]                   export session log as JSON
"""

import os
import datetime
from typing import Optional

# ── Module-level state ────────────────────────────────────────────────────────
_LAST_SCRIPT: Optional[str] = None       # most recently generated code block
_UNDO_STATE: Optional[dict] = None       # PyMOL session snapshot for undo
_LAST_EXECUTION_NOTE: str = ""           # injected into the next user message


# ── Plugin registration ───────────────────────────────────────────────────────

def __init_plugin__(app=None):
    from pymol import cmd
    from . import config
    cmd.extend("pm",      _pm)
    cmd.extend("pmcfg",   _pmcfg)
    cmd.extend("pmreset", _pmreset)
    cmd.extend("pmsave",  _pmsave)
    cmd.extend("pmlog",   _pmlog)
    cmd.extend("pmsetup", _pmsetup)
    cmd.extend("pmundo",  _pmundo)

    if not os.path.exists(config.CONFIG_PATH):
        _print_setup_wizard(first_run=True)
    else:
        print("PromptMol loaded. Type 'pm help' for usage or 'pmsetup' to reconfigure.")


# ── pm command ────────────────────────────────────────────────────────────────

def _pm(*args, **kwargs):
    """pm [--dry] [--save [file]] [--outdir /path] [--model name] <prompt>"""
    raw = " ".join(str(a) for a in args).strip()
    tokens = raw.split()

    dry = False
    save = False
    save_filename: Optional[str] = None
    outdir_override: Optional[str] = None
    model_override: Optional[str] = None

    while tokens and tokens[0].startswith("--"):
        flag = tokens.pop(0)
        if flag == "--dry":
            dry = True
        elif flag == "--save":
            save = True
            if tokens and not tokens[0].startswith("-") and _looks_like_filename(tokens[0]):
                save_filename = tokens.pop(0)
        elif flag == "--outdir":
            if not tokens:
                print("PromptMol: --outdir requires a path")
                return
            outdir_override = tokens.pop(0)
        elif flag == "--model":
            if not tokens:
                print("PromptMol: --model requires a model name")
                return
            model_override = tokens.pop(0)
        else:
            print(f"PromptMol: unknown flag '{flag}'")
            return

    prompt = " ".join(tokens).strip()
    if not prompt or prompt.lower() == "help":
        _print_help()
        return

    _run_prompt(
        prompt,
        dry=dry,
        save=save,
        save_filename=save_filename,
        output_dir=outdir_override or "",
        model_override=model_override,
    )


# ── Core prompt runner ────────────────────────────────────────────────────────

def _run_prompt(
    prompt: str,
    dry: bool = False,
    save: bool = False,
    save_filename: Optional[str] = None,
    output_dir: str = "",
    model_override: Optional[str] = None,
    on_token=None,  # optional callback for GUI streaming
) -> None:
    global _LAST_SCRIPT, _UNDO_STATE, _LAST_EXECUTION_NOTE

    from . import llm, session, state
    from .prompts import SYSTEM_PROMPT
    from . import config
    from .utils import execute_code, parse_response

    cfg = config.load_config()
    sess = session.get_session()
    sess.max_history = int(cfg.get("max_history", 20))

    # Resolve output directory
    resolved_dir = os.path.expanduser(
        output_dir or cfg.get("output_dir") or os.getcwd()
    )
    if not os.path.exists(resolved_dir):
        print(f"PromptMol: output directory '{resolved_dir}' does not exist — creating it.")
    os.makedirs(resolved_dir, exist_ok=True)

    # Build user message — include scene state and any note from last execution
    scene = state.get_scene_state()
    exec_note = (
        f"\n\nNote from previous command: {_LAST_EXECUTION_NOTE}"
        if _LAST_EXECUTION_NOTE
        else ""
    )
    user_msg = (
        f"{scene}{exec_note}"
        f"\n\nOutput directory for any saved files: {resolved_dir}"
        f"\n\nUser request: {prompt}"
    )

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += sess.get_messages()
    messages.append({"role": "user", "content": user_msg})

    backend = cfg.get("backend", "lmstudio")
    if model_override:
        print(f"PromptMol [{backend}]: thinking (model: {model_override})…")
    else:
        print(f"PromptMol [{backend}]: thinking…")

    try:
        response = llm.chat(messages, on_token=on_token, model_override=model_override)
    except RuntimeError as e:
        print(f"PromptMol ERROR: {e}")
        _LAST_EXECUTION_NOTE = ""
        return

    summary, code = parse_response(response)

    if code:
        _LAST_SCRIPT = code

        if dry:
            print(f"--- Generated commands (dry run) [outdir: {resolved_dir}] ---")
            for line in code.splitlines():
                print(f"  {line}")
            print("--- End dry run ---")
            _LAST_EXECUTION_NOTE = ""
        else:
            # Snapshot scene for undo
            _save_undo_state()

            # Track objects before execution for change reporting
            try:
                from pymol import cmd as _cmd
                objects_before = set(_cmd.get_object_list() or [])
            except Exception:
                objects_before = set()

            print(f"--- Executing [outdir: {resolved_dir}] ---")
            error = execute_code(code, resolved_dir)

            if error:
                # ── Auto-retry: ask the LLM to fix the error once ─────────────
                print(f"PromptMol: execution error — {error}")
                print("PromptMol: asking LLM to fix…")
                retry_messages = messages + [
                    {"role": "assistant", "content": response},
                    {
                        "role": "user",
                        "content": (
                            f"The code raised this error:\n\n    {error}\n\n"
                            "Please fix it and try again."
                        ),
                    },
                ]
                try:
                    response2 = llm.chat(
                        retry_messages, on_token=on_token, model_override=model_override
                    )
                    _, code2 = parse_response(response2)
                    if code2:
                        error2 = execute_code(code2, resolved_dir)
                        if error2:
                            print(f"PromptMol: auto-fix also failed — {error2}")
                            _LAST_EXECUTION_NOTE = (
                                f"Code failed ({error}). Auto-fix also failed ({error2})."
                            )
                        else:
                            print("--- Done (auto-fixed) ---")
                            code = code2
                            response = response2
                            _LAST_EXECUTION_NOTE = "Previous code had an error that was auto-fixed."
                    else:
                        print("PromptMol: LLM did not produce code on retry.")
                        _LAST_EXECUTION_NOTE = f"Code failed with error: {error}"
                except RuntimeError as retry_err:
                    print(f"PromptMol: retry LLM call failed — {retry_err}")
                    _LAST_EXECUTION_NOTE = f"Code failed with error: {error}"
            else:
                # ── Success — compute what changed ────────────────────────────
                try:
                    objects_after = set(_cmd.get_object_list() or [])
                    added = objects_after - objects_before
                    removed = objects_before - objects_after
                    notes = []
                    if added:
                        notes.append(f"added {', '.join(sorted(added))}")
                    if removed:
                        notes.append(f"removed {', '.join(sorted(removed))}")
                    change_str = "; ".join(notes) if notes else "no object changes"
                    _LAST_EXECUTION_NOTE = f"Executed successfully. Scene: {change_str}."
                except Exception:
                    _LAST_EXECUTION_NOTE = "Executed successfully."
                print("--- Done ---")

        if save:
            _do_save(code, save_filename, resolved_dir)
    else:
        # Pure text answer — already streamed, nothing extra to do
        _LAST_EXECUTION_NOTE = ""

    # Update session history
    sess.add_user(f"User request: {prompt}")
    sess.add_assistant(response)
    sess.log_exchange(prompt, summary, code if code else None)


# ── Undo helpers ──────────────────────────────────────────────────────────────

def _save_undo_state() -> None:
    global _UNDO_STATE
    try:
        from pymol import cmd
        _UNDO_STATE = cmd.get_session()
    except Exception:
        _UNDO_STATE = None


def _pmundo(*args, **kwargs):
    """Restore the PyMOL session to before the last executed pm command."""
    global _UNDO_STATE
    if _UNDO_STATE is None:
        print("PromptMol: nothing to undo.")
        return
    try:
        from pymol import cmd
        cmd.set_session(_UNDO_STATE)
        _UNDO_STATE = None
        print("PromptMol: scene restored to before last command.")
    except Exception as e:
        print(f"PromptMol: undo failed — {e}")


# ── Shared helpers ────────────────────────────────────────────────────────────

def _looks_like_filename(s: str) -> bool:
    return "." in s and len(s.split()) == 1


# ── pmsetup ───────────────────────────────────────────────────────────────────

def _pmsetup(*args, **kwargs):
    """pmsetup | pmsetup lmstudio | pmsetup openai <key> | pmsetup anthropic <key>"""
    from . import config

    tokens = " ".join(str(a) for a in args).split()
    if not tokens:
        _print_setup_wizard(first_run=False)
        return

    backend = tokens[0].lower()

    if backend == "lmstudio":
        config.save_config("backend", "lmstudio")
        print("\n  PromptMol: backend set to LM Studio (local)")
        print(f"  Server URL: {config.get('base_url')}")
        print("  Optional tweaks:")
        print("    pmcfg set model <model-name>")
        print("    pmcfg set base_url <url>\n")
        print("  Setup complete! Try:  pm fetch 1hpv and show as cartoon colored by chain")
        return

    if backend == "openai":
        api_key = tokens[1] if len(tokens) > 1 else ""
        config.save_config("backend", "openai")
        if api_key:
            config.save_config("api_key", api_key)
            print("\n  PromptMol: backend set to OpenAI, API key saved.")
            print(f"  Model: {config.get('openai_model')}  (pmcfg set openai_model <name>)\n")
            print("  Setup complete! Try:  pm fetch 1hpv and show as cartoon colored by chain")
        else:
            print("\n  PromptMol: backend set to OpenAI.")
            print("  Enter your API key:  pmsetup openai <your-api-key>")
            print("  Get a key at: https://platform.openai.com/api-keys\n")
        return

    if backend == "anthropic":
        api_key = tokens[1] if len(tokens) > 1 else ""
        config.save_config("backend", "anthropic")
        if api_key:
            config.save_config("api_key", api_key)
            print("\n  PromptMol: backend set to Anthropic, API key saved.")
            print(f"  Model: {config.get('anthropic_model')}  (pmcfg set anthropic_model <name>)\n")
            print("  Setup complete! Try:  pm fetch 1hpv and show as cartoon colored by chain")
        else:
            print("\n  PromptMol: backend set to Anthropic.")
            print("  Enter your API key:  pmsetup anthropic <your-api-key>")
            print("  Get a key at: https://console.anthropic.com/settings/keys\n")
        return

    print(f"  Unknown backend '{backend}'. Choose: lmstudio, openai, anthropic")
    _print_setup_wizard(first_run=False)


def _print_setup_wizard(first_run: bool = False) -> None:
    from . import config
    current = config.get("backend")

    if first_run:
        print("")
        print("  ╔══════════════════════════════════════════════════╗")
        print("  ║           Welcome to PromptMol!                  ║")
        print("  ║  Natural-language control for PyMOL              ║")
        print("  ╚══════════════════════════════════════════════════╝")
        print("")
        print("  First-time setup — choose your LLM backend:")
    else:
        print(f"\n  PromptMol Setup  (current backend: {current})")
        print("  " + "─" * 48)
        print("\n  Choose a backend:")

    print("")
    print("  1. LM Studio  — local model, no API key needed (recommended)")
    print("       pmsetup lmstudio")
    print("")
    print("  2. OpenAI  — GPT-4o, requires API key")
    print("       pmsetup openai <your-api-key>")
    print("")
    print("  3. Anthropic  — Claude, requires API key")
    print("       pmsetup anthropic <your-api-key>")
    print("")
    print("  ─────────────────────────────────────────────────────")
    print("  Type 'pmsetup' to return here at any time.")
    print("  Type 'pmcfg show' to view all current settings.\n")


def _print_help() -> None:
    print(
        "PromptMol usage:\n"
        "  pm <prompt>                        ask the LLM and auto-execute\n"
        "  pm --dry <prompt>                  preview commands without executing\n"
        "  pm --save <prompt>                 execute and save script (auto filename)\n"
        "  pm --save file.py <prompt>         execute and save to file.py\n"
        "  pm --outdir /path <prompt>         set output folder for this command\n"
        "  pm --model <name> <prompt>         override LLM model for this command\n"
        "  pm --dry --save --outdir /p <p>    combine flags freely\n"
        "\n"
        "  pmundo                             restore scene to before last command\n"
        "\n"
        "  pmsetup                            show backend setup wizard\n"
        "  pmsetup lmstudio                   switch to LM Studio (local)\n"
        "  pmsetup openai <key>               switch to OpenAI + set API key\n"
        "  pmsetup anthropic <key>            switch to Anthropic + set API key\n"
        "\n"
        "  pmcfg show                         show current config\n"
        "  pmcfg set output_dir /path         set persistent output folder\n"
        "  pmcfg set temperature 0.1          set LLM sampling temperature\n"
        "  pmcfg set <key> <value>            set any config value\n"
        "  pmreset                            clear conversation history and log\n"
        "  pmsave [file.py]                   save last generated script\n"
        "  pmlog show                         print session log to console\n"
        "  pmlog save [file.py]               save full session log as runnable script\n"
        "  pmlog export [file.json]           export session log as JSON\n"
    )


# ── pmcfg ─────────────────────────────────────────────────────────────────────

def _pmcfg(*args, **kwargs):
    """pmcfg set <key> <value>  |  pmcfg show"""
    from . import config

    tokens = " ".join(str(a) for a in args).split()
    if not tokens or tokens[0] == "show":
        cfg = config.load_config()
        print("PromptMol config:")
        for k, v in cfg.items():
            display = "***" if k == "api_key" and v else v
            print(f"  {k} = {display}")
        return

    if tokens[0] == "set":
        if len(tokens) < 3:
            print("Usage: pmcfg set <key> <value>")
            return
        key, value = tokens[1], " ".join(tokens[2:])
        valid_keys = {
            "backend", "model", "api_key", "base_url", "max_history",
            "anthropic_model", "openai_model", "output_dir", "temperature",
        }
        if key not in valid_keys:
            print(f"Unknown config key '{key}'. Valid keys: {', '.join(sorted(valid_keys))}")
            return
        if key == "backend" and value not in ("lmstudio", "openai", "anthropic"):
            print("backend must be one of: lmstudio, openai, anthropic")
            return
        config.save_config(key, value)
        if key == "max_history":
            from . import session
            session.update_max_history(int(value))
        print(f"PromptMol: set {key} = {value}")
        return

    print("Usage: pmcfg show  |  pmcfg set <key> <value>")


# ── pmreset ───────────────────────────────────────────────────────────────────

def _pmreset(*args, **kwargs):
    """Clear conversation history, session log, undo state, and last script."""
    global _LAST_SCRIPT, _UNDO_STATE, _LAST_EXECUTION_NOTE
    from . import session
    session.reset_session()
    _LAST_SCRIPT = None
    _UNDO_STATE = None
    _LAST_EXECUTION_NOTE = ""
    print("PromptMol: conversation history cleared.")


# ── pmsave ────────────────────────────────────────────────────────────────────

def _pmsave(*args, **kwargs):
    """pmsave [filename]  — save the last generated script."""
    global _LAST_SCRIPT
    if _LAST_SCRIPT is None:
        print("PromptMol: no script has been generated yet.")
        return
    from . import config
    tokens = " ".join(str(a) for a in args).split()
    filename = tokens[0] if tokens else None
    out = os.path.expanduser(config.get("output_dir") or os.getcwd())
    _do_save(_LAST_SCRIPT, filename, out)


def _do_save(code: str, filename: Optional[str], output_dir: str = "") -> None:
    if not filename:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"promptmol_{ts}.py"
    base = output_dir or os.getcwd()
    try:
        os.makedirs(base, exist_ok=True)
        path = os.path.join(base, filename)
        _write_script(path, code)
    except OSError:
        scripts_dir = os.path.expanduser("~/promptmol_scripts")
        os.makedirs(scripts_dir, exist_ok=True)
        path = os.path.join(scripts_dir, filename)
        _write_script(path, code)


def _write_script(path: str, code: str) -> None:
    header = (
        "# Generated by PromptMol\n"
        f"# {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        "from pymol import cmd\n\n"
    )
    with open(path, "w") as f:
        f.write(header + code + "\n")
    print(f"PromptMol: script saved to {path}")


# ── pmlog ─────────────────────────────────────────────────────────────────────

def _pmlog(*args, **kwargs):
    """pmlog show | pmlog save [filename] | pmlog export [filename]"""
    import json
    from . import session, config as _cfg

    tokens = " ".join(str(a) for a in args).split()
    subcommand = tokens[0] if tokens else "show"

    sess = session.get_session()
    log = sess.get_log()

    if not log:
        print("PromptMol: no exchanges in this session yet.")
        return

    if subcommand == "show":
        print(f"PromptMol session log (started {sess.started_at}):")
        for i, entry in enumerate(log, 1):
            print(f"\n--- [{i}] {entry['timestamp']} ---")
            print(f"  Prompt : {entry['prompt']}")
            if entry["summary"]:
                print(f"  Summary: {entry['summary']}")
            if entry["code"]:
                for line in entry["code"].splitlines():
                    print(f"    {line}")
        return

    out = os.path.expanduser(_cfg.get("output_dir") or os.getcwd())

    if subcommand == "save":
        filename = tokens[1] if len(tokens) > 1 else None
        _save_session_log(sess, log, filename, out)
        return

    if subcommand == "export":
        filename = tokens[1] if len(tokens) > 1 else None
        if not filename:
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"promptmol_session_{ts}.json"
        os.makedirs(out, exist_ok=True)
        path = os.path.join(out, filename) if not os.path.isabs(filename) else filename
        data = {
            "started_at": sess.started_at,
            "exported_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "exchanges": log,
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"PromptMol: session exported to {path}")
        return

    print("Usage: pmlog show  |  pmlog save [filename]  |  pmlog export [filename]")


def _save_session_log(sess, log: list, filename: Optional[str], output_dir: str = "") -> None:
    if filename and os.path.isabs(filename):
        path = filename
    else:
        base = output_dir or os.getcwd()
        if not filename:
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"promptmol_session_{ts}.py"
        os.makedirs(base, exist_ok=True)
        path = os.path.join(base, filename)

    lines = [
        "# PromptMol session log",
        f"# Session started: {sess.started_at}",
        f"# Saved:           {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "from pymol import cmd",
        "",
    ]
    for i, entry in enumerate(log, 1):
        lines.append(f"# ── Step {i}: {entry['timestamp']}")
        lines.append(f"# Prompt: {entry['prompt']}")
        if entry["summary"]:
            lines.append(f"# {entry['summary']}")
        lines.append(entry["code"] if entry["code"] else "# (no commands generated)")
        lines.append("")

    content = "\n".join(lines)
    try:
        with open(path, "w") as f:
            f.write(content)
    except OSError:
        fallback = os.path.join(
            os.path.expanduser("~/promptmol_scripts"), os.path.basename(path)
        )
        os.makedirs(os.path.dirname(fallback), exist_ok=True)
        with open(fallback, "w") as f:
            f.write(content)
        path = fallback

    print(f"PromptMol: session log saved to {path}")
