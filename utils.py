"""Shared utility functions used by both __init__.py and gui.py."""

import os
import re
from typing import Optional, Tuple

# Calls that must never run inside generated code — they close PyMOL
BLOCKED_CALLS = ("cmd.quit", "cmd.exit", "pymol.quit", "sys.exit", "quit(", "exit(")


def execute_code(code: str, output_dir: str = "") -> Optional[str]:
    """Execute a Python code block in the PyMOL context.

    Returns an error string on failure, or None on success.
    Imports are lazy so this module stays importable without PyMOL.
    """
    for blocked in BLOCKED_CALLS:
        if blocked in code:
            return f"Blocked unsafe call: '{blocked}'"

    import math
    import csv
    from pymol import cmd
    from pymol import stored as _pymol_stored

    effective_outdir = output_dir or os.getcwd()
    ns = {
        "cmd": cmd,
        "output_dir": effective_outdir,
        "os": os,
        "math": math,
        "csv": csv,
        "stored": _pymol_stored,
    }
    try:
        exec(compile(code, "<promptmol>", "exec"), ns)
        return None
    except Exception as e:
        return str(e)


def parse_response(response: str) -> Tuple[str, str]:
    """Return (summary_text, code_block_text). Either may be empty string."""
    pattern = r"```(?:python|pymol)?\s*\n(.*?)```"
    match = re.search(pattern, response, re.DOTALL)
    if match:
        code = match.group(1).strip()
        summary = response[: match.start()].strip().rstrip(":").strip()
        return summary, code
    return response.strip(), ""
