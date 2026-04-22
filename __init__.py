"""
PromptMol — natural-language PyMOL assistant.

Commands registered in the PyMOL command line:
  pm [--dry] [--save [filename]] [--outdir /path] <prompt>
  pmsetup                                   interactive first-run setup wizard
  pmsetup lmstudio                          configure LM Studio backend
  pmsetup openai <api_key>                  configure OpenAI backend
  pmsetup anthropic <api_key>               configure Anthropic backend
  pmcfg set <key> <value>                   configure any individual setting
  pmcfg show                                print current config
  pmreset                                   clear conversation history and log
  pmsave [filename]                         save last generated script
  pmlog save [filename]                     save full session log as .py script
  pmlog show                                print session log to console
"""

import os
import re
import datetime
from typing import Optional

_LAST_SCRIPT: Optional[str] = None  # stores last generated code block


def __init_plugin__(app=None):
    from pymol import cmd
    from . import config
    cmd.extend("pm", _pm)
    cmd.extend("pmcfg", _pmcfg)
    cmd.extend("pmreset", _pmreset)
    cmd.extend("pmsave", _pmsave)
    cmd.extend("pmlog", _pmlog)
    cmd.extend("pmsetup", _pmsetup)

    # First-run detection: show setup wizard if no config file exists yet
    if not os.path.exists(config.CONFIG_PATH):
        _print_setup_wizard(first_run=True)
    else:
        print("PromptMol loaded. Type 'pm help' for usage or 'pmsetup' to reconfigure.")


# ---------------------------------------------------------------------------
# pm command
# ---------------------------------------------------------------------------

def _pm(*args, **kwargs):
    """pm [--dry] [--save [filename]] [--outdir /path] <natural language prompt>"""
    global _LAST_SCRIPT

    # PyMOL passes the whole input as a single string — split it into tokens
    raw = " ".join(str(a) for a in args).strip()
    args = raw.split()
    dry = False
    save = False
    save_filename: Optional[str] = None
    outdir_override: Optional[str] = None

    # Parse flags
    while args and args[0].startswith("--"):
        flag = args.pop(0)
        if flag == "--dry":
            dry = True
        elif flag == "--save":
            save = True
            if args and not args[0].startswith("-") and _looks_like_filename(args[0]):
                save_filename = args.pop(0)
        elif flag == "--outdir":
            if not args:
                print("PromptMol: --outdir requires a path")
                return
            outdir_override = args.pop(0)
        else:
            print(f"PromptMol: unknown flag '{flag}'")
            return

    prompt = " ".join(args).strip()

    if not prompt or prompt.lower() == "help":
        _print_help()
        return

    from . import llm, session, state
    from .prompts import SYSTEM_PROMPT
    from . import config

    cfg = config.load_config()
    sess = session.get_session()
    sess.max_history = cfg.get("max_history", 20)

    # Resolve output directory: flag > config > cwd
    output_dir = outdir_override or cfg.get("output_dir") or os.getcwd()
    output_dir = os.path.expanduser(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    scene = state.get_scene_state()
    user_msg = f"{scene}\n\nOutput directory for any saved files: {output_dir}\n\nUser request: {prompt}"

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += sess.get_messages()
    messages.append({"role": "user", "content": user_msg})

    backend = cfg.get("backend", "lmstudio")
    print(f"PromptMol [{backend}]: thinking...")

    try:
        response = llm.chat(messages)
    except RuntimeError as e:
        print(f"PromptMol ERROR: {e}")
        return

    # Split plain-English summary from code block
    summary, code = _parse_response(response)
    if summary:
        print(f"PromptMol: {summary}")

    if code:
        _LAST_SCRIPT = code
        lines = [l for l in code.splitlines() if l.strip() and not l.strip().startswith("#")]

        if dry:
            print(f"--- Generated commands (dry run) [outdir: {output_dir}] ---")
            for line in code.splitlines():
                print(f"  {line}")
            print("--- End dry run ---")
        else:
            print(f"--- Executing [outdir: {output_dir}] ---")
            _execute_code(code, output_dir)
            print("--- Done ---")

        if save:
            _do_save(code, save_filename, output_dir)
    else:
        # Pure answer, no code
        print(response)

    # Update session history and log
    sess.add_user(f"User request: {prompt}")
    sess.add_assistant(response)
    sess.log_exchange(prompt, summary, code if code else None)


def _execute_code(code: str, output_dir: str = "") -> None:
    """Execute a Python code block in the PyMOL context."""
    from pymol import cmd  # noqa: F401 — available to exec'd code
    import math
    import csv

    effective_outdir = output_dir or os.getcwd()
    from pymol import stored as _pymol_stored
    ns = {"cmd": cmd, "output_dir": effective_outdir, "os": os, "math": math, "csv": csv, "stored": _pymol_stored}
    try:
        exec(compile(code, "<promptmol>", "exec"), ns)
    except Exception as e:
        print(f"PromptMol execution error: {e}")
        # Try line-by-line as fallback
        for line in code.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                exec(compile(line, "<promptmol>", "exec"), ns)
            except Exception as le:
                print(f"  Error on: {line!r} → {le}")


def _parse_response(response: str):
    """Return (summary_text, code_block_text). Either may be empty string."""
    # Extract ```python ... ``` or ``` ... ```
    pattern = r"```(?:python|pymol)?\s*\n(.*?)```"
    match = re.search(pattern, response, re.DOTALL)
    if match:
        code = match.group(1).strip()
        # Summary is everything before the code block
        summary = response[:match.start()].strip()
        # Clean up trailing colons or filler
        summary = summary.rstrip(":").strip()
        return summary, code
    return response.strip(), ""


def _looks_like_filename(s: str) -> bool:
    return "." in s and len(s.split()) == 1


# ---------------------------------------------------------------------------
# pmsetup command
# ---------------------------------------------------------------------------

def _pmsetup(*args, **kwargs):
    """pmsetup | pmsetup lmstudio | pmsetup openai <key> | pmsetup anthropic <key>"""
    from . import config

    args = " ".join(str(a) for a in args).split()

    if not args:
        _print_setup_wizard(first_run=False)
        return

    backend = args[0].lower()

    if backend == "lmstudio":
        config.save_config("backend", "lmstudio")
        print("")
        print("  PromptMol: backend set to LM Studio (local)")
        print("")
        print("  Make sure LM Studio is running with a model loaded.")
        print(f"  Server URL: {config.get('base_url')}")
        print("")
        print("  Optional tweaks:")
        print("    pmcfg set model <model-name>        set the model name if needed")
        print("    pmcfg set base_url <url>            change server URL (default: localhost:1234)")
        print("")
        print("  Setup complete! Try:  pm fetch 1hpv and show as cartoon colored by chain")
        return

    if backend == "openai":
        api_key = args[1] if len(args) > 1 else ""
        config.save_config("backend", "openai")
        if api_key:
            config.save_config("api_key", api_key)
            print("")
            print("  PromptMol: backend set to OpenAI, API key saved.")
            print(f"  Model: {config.get('openai_model')} (change with: pmcfg set openai_model <name>)")
            print("")
            print("  Setup complete! Try:  pm fetch 1hpv and show as cartoon colored by chain")
        else:
            print("")
            print("  PromptMol: backend set to OpenAI.")
            print("  Enter your API key:")
            print("")
            print("    pmsetup openai <your-api-key>")
            print("")
            print("  Get a key at: https://platform.openai.com/api-keys")
        return

    if backend == "anthropic":
        api_key = args[1] if len(args) > 1 else ""
        config.save_config("backend", "anthropic")
        if api_key:
            config.save_config("api_key", api_key)
            print("")
            print("  PromptMol: backend set to Anthropic, API key saved.")
            print(f"  Model: {config.get('anthropic_model')} (change with: pmcfg set anthropic_model <name>)")
            print("")
            print("  Setup complete! Try:  pm fetch 1hpv and show as cartoon colored by chain")
        else:
            print("")
            print("  PromptMol: backend set to Anthropic.")
            print("  Enter your API key:")
            print("")
            print("    pmsetup anthropic <your-api-key>")
            print("")
            print("  Get a key at: https://console.anthropic.com/settings/keys")
        return

    print(f"  Unknown backend '{backend}'. Choose: lmstudio, openai, anthropic")
    _print_setup_wizard(first_run=False)


def _print_setup_wizard(first_run: bool = False):
    from . import config
    cfg = config.load_config()
    current = cfg.get("backend", "lmstudio")

    if first_run:
        print("")
        print("  ╔══════════════════════════════════════════════════╗")
        print("  ║           Welcome to PromptMol!                  ║")
        print("  ║  Natural-language control for PyMOL              ║")
        print("  ╚══════════════════════════════════════════════════╝")
        print("")
        print("  First-time setup — choose your LLM backend:")
    else:
        print("")
        print("  PromptMol Setup  (current backend: {})".format(current))
        print("  " + "─" * 48)
        print("")
        print("  Choose a backend:")

    print("")
    print("  1. LM Studio  — local model, no API key needed (recommended)")
    print("")
    print("       pmsetup lmstudio")
    print("")
    print("  2. OpenAI  — GPT-4o, requires API key")
    print("")
    print("       pmsetup openai <your-api-key>")
    print("")
    print("  3. Anthropic  — Claude, requires API key")
    print("")
    print("       pmsetup anthropic <your-api-key>")
    print("")
    print("  ─────────────────────────────────────────────────────")
    print("  Type 'pmsetup' at any time to return to this screen.")
    print("  Type 'pmcfg show' to view all current settings.")
    print("")


def _print_help():
    print(
        "PromptMol usage:\n"
        "  pm <prompt>                        ask the LLM and auto-execute\n"
        "  pm --dry <prompt>                  preview commands without executing\n"
        "  pm --save <prompt>                 execute and save script (auto filename)\n"
        "  pm --save file.py <prompt>         execute and save to file.py\n"
        "  pm --outdir /path <prompt>         set output folder for this command\n"
        "  pm --dry --save --outdir /p <p>    combine flags freely\n"
        "\n"
        "  pmsetup                            show backend setup wizard\n"
        "  pmsetup lmstudio                   switch to LM Studio (local)\n"
        "  pmsetup openai <key>               switch to OpenAI + set API key\n"
        "  pmsetup anthropic <key>            switch to Anthropic + set API key\n"
        "\n"
        "  pmcfg show                         show current config\n"
        "  pmcfg set output_dir /path         set persistent output folder\n"
        "  pmcfg set <key> <value>            set any config value\n"
        "  pmreset                            clear conversation history and log\n"
        "  pmsave [file.py]                   save last generated script\n"
        "  pmlog show                         print session log to console\n"
        "  pmlog save [file.py]               save full session log as runnable script\n"
    )


# ---------------------------------------------------------------------------
# pmcfg command
# ---------------------------------------------------------------------------

def _pmcfg(*args, **kwargs):
    """pmcfg set <key> <value>  |  pmcfg show"""
    from . import config

    args = " ".join(str(a) for a in args).split()
    if not args or args[0] == "show":
        cfg = config.load_config()
        print("PromptMol config:")
        for k, v in cfg.items():
            display = "***" if k == "api_key" and v else v
            print(f"  {k} = {display}")
        return

    if args[0] == "set":
        if len(args) < 3:
            print("Usage: pmcfg set <key> <value>")
            return
        key, value = args[1], " ".join(args[2:])
        valid_keys = {"backend", "model", "api_key", "base_url", "max_history",
                      "anthropic_model", "openai_model", "output_dir"}
        if key not in valid_keys:
            print(f"Unknown config key '{key}'. Valid keys: {', '.join(sorted(valid_keys))}")
            return
        if key == "backend" and value not in ("lmstudio", "openai", "anthropic"):
            print("backend must be one of: lmstudio, openai, anthropic")
            return
        config.save_config(key, value)
        # Update session max_history live if changed
        if key == "max_history":
            from . import session
            session.update_max_history(int(value))
        print(f"PromptMol: set {key} = {value}")
        return

    print("Usage: pmcfg show  |  pmcfg set <key> <value>")


# ---------------------------------------------------------------------------
# pmreset command
# ---------------------------------------------------------------------------

def _pmreset(*args, **kwargs):
    """Clear conversation history and last script."""
    global _LAST_SCRIPT
    from . import session
    session.reset_session()
    _LAST_SCRIPT = None
    print("PromptMol: conversation history cleared.")


# ---------------------------------------------------------------------------
# pmsave command
# ---------------------------------------------------------------------------

def _pmsave(*args, **kwargs):
    """pmsave [filename]  — save the last generated script to a file."""
    global _LAST_SCRIPT
    if _LAST_SCRIPT is None:
        print("PromptMol: no script has been generated yet.")
        return
    tokens = " ".join(str(a) for a in args).split()
    filename = tokens[0] if tokens else None
    _do_save(_LAST_SCRIPT, filename)


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


# ---------------------------------------------------------------------------
# pmlog command
# ---------------------------------------------------------------------------

def _pmlog(*args, **kwargs):
    """pmlog show | pmlog save [filename]"""
    from . import session

    args = " ".join(str(a) for a in args).split()
    subcommand = args[0] if args else "show"

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
            if entry['summary']:
                print(f"  Summary: {entry['summary']}")
            if entry['code']:
                for line in entry['code'].splitlines():
                    print(f"    {line}")
        return

    if subcommand == "save":
        from . import config as _cfg
        filename = args[1] if len(args) > 1 else None
        out = _cfg.get('output_dir') or os.getcwd()
        out = os.path.expanduser(out)
        _save_session_log(sess, log, filename, out)
        return

    print("Usage: pmlog show  |  pmlog save [filename]")


def _save_session_log(sess, log: list, filename: Optional[str], output_dir: str = "") -> None:
    # If filename is an absolute path, use it directly; otherwise place in output_dir
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
        if entry['summary']:
            lines.append(f"# {entry['summary']}")
        if entry['code']:
            lines.append(entry['code'])
        else:
            lines.append("# (no commands generated for this step)")
        lines.append("")

    content = "\n".join(lines)

    try:
        with open(path, "w") as f:
            f.write(content)
    except OSError:
        fallback = os.path.join(os.path.expanduser("~/promptmol_scripts"), os.path.basename(path))
        os.makedirs(os.path.dirname(fallback), exist_ok=True)
        with open(fallback, "w") as f:
            f.write(content)
        path = fallback

    print(f"PromptMol: session log saved to {path}")
