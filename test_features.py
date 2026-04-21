"""
PromptMol feature tests — run headless via:
  conda activate pymol && python test_features.py
"""
import sys
import os
import time

sys.path.insert(0, '/Users/kodyklupt/Documents/claudecode')

# ── Boot PyMOL headless ───────────────────────────────────────────────────────
import pymol
pymol.finish_launching(['pymol', '-c', '-q'])  # -c = no GUI, -q = quiet
from pymol import cmd
time.sleep(1)

# ── Load plugin ───────────────────────────────────────────────────────────────
import promptmol
promptmol.__init_plugin__()

# ── Test output directory ─────────────────────────────────────────────────────
TEST_DIR = os.path.expanduser('~/Desktop/promptmol_test_output')
os.makedirs(TEST_DIR, exist_ok=True)

def separator(title):
    print(f'\n{"="*60}')
    print(f'  TEST: {title}')
    print('='*60)

def check_file(path, label):
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f'  ✓ {label}: {path} ({size} bytes)')
    else:
        print(f'  ✗ MISSING {label}: {path}')

# ─────────────────────────────────────────────────────────────────────────────
separator('1 — Basic pm command (fetch + visualize)')
# This tests: LMStudio connection, command execution, scene state injection
promptmol._pm(f'--outdir {TEST_DIR} fetch 1hpv and show as cartoon colored by chain')
time.sleep(1)
atoms = cmd.count_atoms('all')
print(f'  Atoms loaded: {atoms}')
assert atoms > 0, 'No atoms loaded — LLM may have failed to generate fetch command'

# ─────────────────────────────────────────────────────────────────────────────
separator('2 — --save flag (auto filename)')
promptmol._pm(f'--outdir {TEST_DIR} --save color the protein slate blue')
time.sleep(1)
saved = [f for f in os.listdir(TEST_DIR) if f.startswith('promptmol_') and f.endswith('.py')]
print(f'  Auto-saved scripts found: {saved}')
assert len(saved) >= 1, 'No auto-named script saved'

# ─────────────────────────────────────────────────────────────────────────────
separator('3 — --save with explicit filename')
promptmol._pm(f'--outdir {TEST_DIR} --save cartoon_style.py show the ligand as yellow sticks')
time.sleep(1)
check_file(os.path.join(TEST_DIR, 'cartoon_style.py'), '--save named file')

# ─────────────────────────────────────────────────────────────────────────────
separator('4 — pmsave (save last script retroactively)')
promptmol._pm(f'--outdir {TEST_DIR} add a transparent surface to the protein')
time.sleep(1)
promptmol._pmsave(f'retro_save.py')
check_file(os.path.join(os.getcwd(), 'retro_save.py'), 'pmsave output')

# ─────────────────────────────────────────────────────────────────────────────
separator('5 — --dry flag (no execution)')
atoms_before = cmd.count_atoms('all')
promptmol._pm(f'--dry reinitialize and load something else entirely')
time.sleep(1)
atoms_after = cmd.count_atoms('all')
print(f'  Atoms before dry run: {atoms_before}, after: {atoms_after}')
assert atoms_before == atoms_after, '--dry flag should not have changed the scene'
print('  ✓ --dry correctly blocked execution')

# ─────────────────────────────────────────────────────────────────────────────
separator('6 — Data export (CSV via LLM-generated code)')
promptmol._pm(f'--outdir {TEST_DIR} --save bfactor_export.py export a CSV of B-factors for all alpha carbons in the protein')
time.sleep(2)
check_file(os.path.join(TEST_DIR, 'bfactor_export.py'), 'B-factor export script')
# CSV might be named anything — check for any .csv in output dir
csvs = [f for f in os.listdir(TEST_DIR) if f.endswith('.csv')]
print(f'  CSV files in output dir: {csvs}')

# ─────────────────────────────────────────────────────────────────────────────
separator('7 — PNG render with --outdir')
promptmol._pm(f'--outdir {TEST_DIR} --save render_script.py render a 1200x900 PNG with white background and ray tracing')
time.sleep(2)
check_file(os.path.join(TEST_DIR, 'render_script.py'), 'render script')
pngs = [f for f in os.listdir(TEST_DIR) if f.endswith('.png')]
print(f'  PNG files in output dir: {pngs}')

# ─────────────────────────────────────────────────────────────────────────────
separator('8 — pmlog show (console output)')
print()
promptmol._pmlog('show')

# ─────────────────────────────────────────────────────────────────────────────
separator('9 — pmlog save (session log to file)')
promptmol._pmlog(f'save {os.path.join(TEST_DIR, "test_session.py")}')
check_file(os.path.join(TEST_DIR, 'test_session.py'), 'session log')

# ─────────────────────────────────────────────────────────────────────────────
separator('10 — pmreset clears log')
promptmol._pmreset()
from promptmol import session
log = session.get_session().get_log()
assert len(log) == 0, f'Log should be empty after pmreset, got {len(log)} entries'
print('  ✓ pmreset cleared session log')

# ─────────────────────────────────────────────────────────────────────────────
separator('SUMMARY')
print(f'\n  Output files in {TEST_DIR}:')
for f in sorted(os.listdir(TEST_DIR)):
    size = os.path.getsize(os.path.join(TEST_DIR, f))
    print(f'    {f}  ({size} bytes)')
print('\n  All tests complete.')
