# PromptMOL

## Now with RAG for improved performance with local models.

![PromptMol demo](demo.gif)

A PyMOL plugin that lets you control PyMOL with natural language. Type plain language prompts directly in the PyMOL command line and have an LLM translate them into PyMOL commands that execute automatically.

```
PyMOL> pm fetch 1hpv and show as cartoon colored by chain
PyMOL> pm make the ligand yellow sticks with a transparent surface
PyMOL> pm render a publication quality PNG with a white background
```

And other commands with increasing complexity...

```
PyMOL> pm what residues are within 4 angstroms of the ligand?
PyMOL> pm measure the distance between residue 50 CA and residue 100 CA
PyMOL> pm calculate the molecular weight of the protein
PyMOL> pm export a CSV containing the B-factors 
```

Supports [LM Studio](https://lmstudio.ai) (local, no API key needed), OpenAI, Anthropic, and Google Gemini, switchable at any time with a single command.

---

## Features

- **Natural language → PyMOL commands** - describe what you want, PromptMOL generates and executes the API calls
- **Multi-turn conversation** - the LLM remembers prior context within a session, so follow-up commands just work
- **Four LLM backends** - LM Studio (local), OpenAI, Anthropic, Google Gemini; switch with `pmcfg set backend`
- **RAG for local models** - automatically retrieves relevant PyMOL documentation and injects it into the prompt, improving accuracy for rare commands when using LM Studio
- **Dry-run mode** - preview generated commands before executing with `--dry`
- **Script saving** - save any generated script as a standalone `.py` file with `--save` or `pmsave`
- **Session log** - save the full session as a replayable annotated script with `pmlog save`
- **Output directory** - route all saved files (PNGs, CSVs, etc.) to a folder with `--outdir` or `pmcfg set output_dir`

---

## Requirements

- [PyMOL](https://pymol.org) (open-source) — tested with open-source PyMOL via conda
- Python 3.8+
- One of:
  - [LM Studio](https://lmstudio.ai) running locally (recommended, no API key needed)
  - An OpenAI API key
  - An Anthropic API key
  - A Google API key (free tier available)

---

## Installation

### 1. Install PromptMol

Activate the same conda environment that PyMOL uses, then install directly from GitHub:

```bash
conda activate pymol
pip install git+https://github.com/KodyKlupt/PromptMOL.git
```

This installs PromptMol and its core dependencies (`openai`, `anthropic`) in one step.

**For RAG support with LM Studio** (strongly recommended — improves local model accuracy), install the additional dependencies:

```bash
pip install sentence-transformers chromadb
```

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

**First run with RAG:** On the first `pm` command, PromptMol will automatically download the embedding model (~80 MB, one-time) and build a local vector index of PyMOL documentation. This takes about 30 seconds and happens silently in the background. All subsequent calls are instant.

### Using OpenAI or Anthropic

```
PyMOL> pmcfg set backend openai
PyMOL> pmcfg set api_key sk-...

PyMOL> pmcfg set backend anthropic
PyMOL> pmcfg set api_key sk-ant-...
```

### Using Google Gemini

```
PyMOL> pmsetup google <your-api-key>
```

Or set manually:

```
PyMOL> pmcfg set backend google
PyMOL> pmcfg set google_api_key AIza...
PyMOL> pmcfg set google_model gemini-2.0-flash
```

Get a free API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey). The free tier includes generous rate limits suitable for PyMOL use.

---

## RAG (Retrieval-Augmented Generation) for Local Models

When using LM Studio, PromptMol automatically retrieves relevant PyMOL documentation and injects it into the system prompt before each call. This aims to improve accuracy for commands that local models tend to get wrong — rare API signatures, tricky selection syntax, non-obvious argument orders.

### How it works

1. `docs/` contains markdown files: reference files covering common patterns, plus pagesscraped from the [PyMOL Wiki](https://pymolwiki.org) command reference. 
2. **Embedding** — chunks are embedded with [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) (runs locally, no API key).
3. **Retrieval** — at query time, your prompt is embedded and the top-3 most semantically similar chunks are fetched from the ChromaDB vector store at `~/.promptmol_rag/`.
4. **Injection** — retrieved chunks are appended to the system prompt under a `## Retrieved PyMOL reference` header, giving the model grounded syntax to work from.

RAG is **only active for the LM Studio backend** 

### Setup

```bash
# Install RAG dependencies (one-time)
pip install sentence-transformers chromadb

# Optional: re-scrape the PyMOL wiki to refresh docs
python scripts/scrape_pymol_wiki.py
# Optional: can also scrape other wiki categories

# Then rebuild the index inside PyMOL
pmrag build
```

### Controls

```
pmrag status          show index state (chunk count, paths, enabled/disabled)
pmrag build           (re)build the vector index from docs/
pmrag on / off        enable or disable RAG without removing the index
pmcfg set rag_k 5     retrieve 5 chunks per query instead of 3 (default)
```

The index persists at `~/.promptmol_rag/` across PyMOL sessions. It is only rebuilt when you explicitly run `pmrag build` or when the index is empty (first run).

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

### `pm` - main command

```
pm <prompt>
pm --dry <prompt>                    preview commands without executing
pm --save <prompt>                   execute and save script (auto-named)
pm --save filename.py <prompt>       execute and save to filename.py
pm --outdir /path <prompt>           set output folder for this command
pm --model <name> <prompt>           override LLM model for this one command
pm --dry --save --outdir /p <prompt> combine flags freely
pm help                              show usage
```

If generated code raises an error, PromptMol automatically sends the error
back to the LLM and retries once.

### `pmundo` - undo last command

```
pmundo                               restore scene to before the last pm command
```

The scene state is snapshotted automatically before each execution.

### `pmcfg` - configuration

```
pmcfg show                           print current config
pmcfg set backend lmstudio           use LM Studio (default)
pmcfg set backend openai             use OpenAI
pmcfg set backend anthropic          use Anthropic
pmcfg set api_key <key>              set API key (OpenAI or Anthropic)
pmcfg set model <name>               set LM Studio model name
pmcfg set openai_model gpt-4o        set OpenAI model
pmcfg set anthropic_model claude-sonnet-4-6
pmcfg set google_model gemini-2.5-pro
pmcfg set base_url http://localhost:1234/v1   LM Studio server URL
pmcfg set google_api_key AIza...             set Google API key
pmcfg set output_dir ~/my/figures    persistent output folder
pmcfg set max_history 20             number of conversation turns to keep
```

Config is saved to `~/.promptmol.json`.

### `pmreset` - clear session

```
pmreset                              clear conversation history, log, and undo state
```

### `pmsave` - save last script

```
pmsave                               save last generated script (auto-named)
pmsave filename.py                   save with a specific name
```

### `pmlog` - session log

```
pmlog show                           print full session log to console
pmlog save                           save session as annotated .py script (auto-named)
pmlog save session.py                save with a specific name
pmlog export                         export session as JSON (auto-named)
pmlog export session.json            export with a specific name
```

The session log is a valid Python script with each step labeled by timestamp
and prompt, so it can be replayed directly in PyMOL. The JSON export is useful
for programmatic analysis or sharing structured session data.

### `pmrag` - RAG index management *(LM Studio only)*

```
pmrag status          show whether RAG is enabled, indexed chunk count, and paths
pmrag build           (re)build the vector index from docs/
pmrag on              enable RAG (default)
pmrag off             disable RAG for this session
```

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

- **Give context**: `pm the ligand is called LIG - show it as sticks` works better than assuming the LLM knows your structure
- **Follow-up naturally**: after loading a structure, subsequent commands can reference it without reloading
- **Use `--dry` first** for complex requests to review commands before they run
- **Replay sessions**: `pmlog save` produces a standalone script you can share or re-run

---

## Citation

@misc{PromptMOL,
    author={Kody A. Klupt},
    title={PromptMOL: Controlling PyMOL with Natural Language},
    year={2026},
    url={https://github.com/KodyKlupt/PromptMOL},

---

## Use of AI

This project was developed with the assistance of Claude Code.
