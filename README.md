# PromptMol

A PyMOL plugin that lets you control PyMOL with natural language. Type plain-English prompts directly in the PyMOL command line and have an LLM translate them into PyMOL commands that execute automatically.

```
PyMOL> pm fetch 1hpv and show as cartoon colored by chain
PyMOL> pm make the ligand yellow sticks with a transparent surface
PyMOL> pm render a publication quality PNG with a white background
```

Supports [LM Studio](https://lmstudio.ai) (local, no API key needed), OpenAI, and Anthropic — switchable at any time with a single command.

---

## Features

- **Natural language → PyMOL commands** — describe what you want, PromptMol generates and executes the API calls
- **Multi-turn conversation** — the LLM remembers prior context within a session, so follow-up commands just work
- **Three LLM backends** — LM Studio (local), OpenAI, Anthropic; switch with `pmcfg set backend`
- **Dry-run mode** — preview generated commands before executing with `--dry`
- **Script saving** — save any generated script as a standalone `.py` file with `--save` or `pmsave`
- **Session log** — save the full session as a replayable annotated script with `pmlog save`
- **Output directory** — route all saved files (PNGs, CSVs, etc.) to a folder with `--outdir` or `pmcfg set output_dir`

---

## Requirements

- [PyMOL](https://pymol.org) (open-source or commercial) — tested with open-source PyMOL via conda
- Python 3.8+
- One of:
  - [LM Studio](https://lmstudio.ai) running locally (recommended for getting started, no API key needed)
  - An OpenAI API key
  - An Anthropic API key

---

## Installation

### 1. Install PromptMol

Activate the same conda environment that PyMOL uses, then install directly from GitHub:

```bash
conda activate pymol
pip install git+https://github.com/KodyKlupt/PromptMOL.git
```

This installs PromptMol and its dependencies (`openai`, `anthropic`) in one step.

To update to the latest version later:

```bash
pip install --upgrade git+https://github.com/KodyKlupt/PromptMOL.git
```

### 2. Load the plugin in PyMOL

Add these two lines to `~/.pymolrc` (create the file if it doesn't exist):

```python
import promptmol
promptmol.__init_plugin__()
```

PyMOL will load PromptMol automatically every time it starts. To verify it worked, open PyMOL and type:

```
pm help
```

---

## Quick Start

### Using LM Studio (local, no API key)

1. Download and open [LM Studio](https://lmstudio.ai)
2. Load any chat model
3. Start the local server (default port: 1234)
4. Open PyMOL — PromptMol defaults to LM Studio, no configuration needed

```
PyMOL> pm fetch 1hpv
PyMOL> pm show it as cartoon colored by secondary structure
PyMOL> pm make the ligand sticks with yellow carbons
```

### Using OpenAI or Anthropic

```
PyMOL> pmcfg set backend openai
PyMOL> pmcfg set api_key sk-...

PyMOL> pmcfg set backend anthropic
PyMOL> pmcfg set api_key sk-ant-...
```

---

## Examples

**Visualization & Styling**
```
pm fetch 1hpv and display it as a cartoon colored by chain
pm show the ligand as yellow sticks and add a transparent grey surface to the protein
pm make the protein slate blue and color residues 50-60 red
```

**Structural Analysis**
```
pm what residues are within 4 angstroms of the ligand?
pm measure the distance between residue 50 CA and residue 100 CA
pm calculate the molecular weight of the protein
```

**Exporting & Rendering**
```
pm render a 300dpi publication quality PNG with a white background
pm save the current structure as a PDB file in my downloads folder
pm export a CSV containing the B-factors for all alpha carbons
```

---

## Command Reference

### `pm` — main command

```
pm <prompt>
pm --dry <prompt>                    preview commands without executing
pm --save <prompt>                   execute and save script (auto-named)
pm --save filename.py <prompt>       execute and save to filename.py
pm --outdir /path <prompt>           set output folder for this command
pm --dry --save --outdir /p <prompt> combine flags freely
pm help                              show usage
```

### `pmcfg` — configuration

```
pmcfg show                           print current config
pmcfg set backend lmstudio           use LM Studio (default)
pmcfg set backend openai             use OpenAI
pmcfg set backend anthropic          use Anthropic
pmcfg set api_key <key>              set API key (OpenAI or Anthropic)
pmcfg set model <name>               set LM Studio model name
pmcfg set openai_model gpt-4o        set OpenAI model
pmcfg set anthropic_model claude-sonnet-4-6
pmcfg set base_url http://localhost:1234/v1   LM Studio server URL
pmcfg set output_dir ~/my/figures    persistent output folder
pmcfg set max_history 20             number of conversation turns to keep
```

Config is saved to `~/.promptmol.json`.

### `pmreset` — clear session

```
pmreset                              clear conversation history and session log
```

### `pmsave` — save last script

```
pmsave                               save last generated script (auto-named)
pmsave filename.py                   save with a specific name
```

### `pmlog` — session log

```
pmlog show                           print full session log to console
pmlog save                           save session as annotated .py script (auto-named)
pmlog save session.py                save with a specific name
```

The session log is a valid Python script with each step labeled by timestamp and prompt, so it can be replayed directly in PyMOL.

---

## Output Directory

Any files generated by LLM scripts (PNGs, CSVs, exported PDBs, etc.) respect the active output directory:

```
# Per-command
pm --outdir ~/Desktop/figures render a 300dpi PNG

# Persistent (survives restarts)
pmcfg set output_dir ~/Desktop/figures
```

Scripts saved by `--save`, `pmsave`, and `pmlog save` also land in this directory. Defaults to the current working directory if not set.

---

## Tips

- **Give context**: `pm the ligand is called LIG — show it as sticks` works better than assuming the LLM knows your structure
- **Follow-up naturally**: after loading a structure, subsequent commands can reference it without reloading
- **Use `--dry` first** for complex requests to review commands before they run
- **Replay sessions**: `pmlog save` produces a standalone script you can share or re-run

---

## Project Structure

```
promptmol/
├── __init__.py     # plugin entry point, command handlers
├── llm.py          # LLM client (LM Studio / OpenAI / Anthropic)
├── config.py       # config load/save (~/.promptmol.json)
├── session.py      # conversation history and session log
├── state.py        # PyMOL scene state inspector
└── prompts.py      # system prompt with PyMOL API reference
```

---

