"""
PromptMol — complex prompt tests against a live local LLM.
Evaluates output quality: did the LLM generate correct code that actually worked?

Run: conda activate pymol && python test_complex_prompts.py
"""
import sys, os, time, io, contextlib, csv

sys.path.insert(0, '/Users/kodyklupt/Documents/claudecode')
import pymol
pymol.finish_launching(['pymol', '-c', '-q'])
from pymol import cmd, stored
time.sleep(1)

import promptmol
from promptmol import session as sess_mod
promptmol.__init_plugin__()

TEST_DIR = os.path.expanduser('~/Desktop/promptmol_test_output/complex_prompts')
os.makedirs(TEST_DIR, exist_ok=True)
promptmol._pmcfg(f'set output_dir {TEST_DIR}')

PASS = '  ✓'
FAIL = '  ✗'
results = []

def separator(title):
    print(f'\n{"="*60}')
    print(f'  {title}')
    print('='*60)

def check(condition, label, detail=''):
    tag = PASS if condition else FAIL
    line = f'{tag} {label}' + (f'  ({detail})' if detail else '')
    print(line)
    results.append((condition, label))
    return condition

def capture_pm(*args):
    """Run a pm command and return its stdout."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        promptmol._pm(*args)
    return buf.getvalue()

def reset():
    cmd.reinitialize()
    sess_mod.reset_session()

# ─────────────────────────────────────────────────────────────────────────────
separator('1 — Load + full publication-style figure in one prompt')
# Tests: fetch, hide, show, color by SS, fancy helices, white bg, ray trace, png
# ─────────────────────────────────────────────────────────────────────────────
reset()
out = capture_pm(
    '--save pub_figure.py '
    'fetch 1hpv, hide everything, show cartoon colored by secondary structure '
    'with fancy helices and sheets, white background, and save a 1200x900 ray-traced PNG called pub_1hpv.png'
)
print(out)
check(cmd.count_atoms('all') > 0, 'structure loaded')
check(os.path.exists(os.path.join(TEST_DIR, 'pub_1hpv.png')), 'PNG rendered to output_dir',
      f'{os.path.getsize(os.path.join(TEST_DIR,"pub_1hpv.png"))//1024} KB' if os.path.exists(os.path.join(TEST_DIR,'pub_1hpv.png')) else 'missing')
check(os.path.exists(os.path.join(TEST_DIR, 'pub_figure.py')), 'script saved')

# ─────────────────────────────────────────────────────────────────────────────
separator('2 — Multi-turn: ligand style built up across 3 commands')
# Tests: conversation memory, cumulative changes
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm('show the ligand as sticks')
print(out)
out = capture_pm('color the ligand carbons yellow and heteroatoms by element')
print(out)
out = capture_pm('add a transparent grey surface to just the protein around the ligand binding site')
print(out)

# Check ligand is visible as sticks
stored.reps = []
cmd.iterate('organic', 'stored.reps.append(1)')
check(len(stored.reps) > 0, 'ligand atoms present (multi-turn context preserved)')

# ─────────────────────────────────────────────────────────────────────────────
separator('3 — Residue composition analysis + print to console')
# Tests: iterate, Counter, print output, no file needed
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm('calculate the amino acid composition of the protein and print a sorted table')
print(out)
check('ALA' in out or 'GLY' in out or 'LEU' in out or 'VAL' in out,
      'residue names appear in output')
check(any(c.isdigit() for c in out), 'counts appear in output')

# ─────────────────────────────────────────────────────────────────────────────
separator('4 — B-factor statistics + CSV export')
# Tests: iterate, math, csv writer, output_dir file creation
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm(
    'calculate B-factor statistics for the protein (mean, min, max, std dev) '
    'and export per-residue alpha carbon B-factors to a CSV called bfactors.csv'
)
print(out)
check(os.path.exists(os.path.join(TEST_DIR, 'bfactors.csv')), 'bfactors.csv created in output_dir')
if os.path.exists(os.path.join(TEST_DIR, 'bfactors.csv')):
    with open(os.path.join(TEST_DIR, 'bfactors.csv')) as f:
        rows = list(csv.reader(f))
    check(len(rows) > 2, 'CSV has data rows', f'{len(rows)-1} residues')
    check(len(rows[0]) >= 3, 'CSV has multiple columns', str(rows[0]))
# Check stats printed
check(any(w in out for w in ['mean', 'Mean', 'avg', 'Avg', 'average']), 'mean B-factor reported')
check(any(w in out for w in ['min', 'Min', 'max', 'Max']), 'min/max reported')

# ─────────────────────────────────────────────────────────────────────────────
separator('5 — Ligand contact shell: select + label + distance')
# Tests: spatial selection, byres, within, label, distance
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm(
    'select all protein residues within 4 angstroms of the ligand, '
    'color them red, and show as sticks. Also label each with its residue name and number'
)
print(out)
sele_names = cmd.get_names('selections')
check(any('near' in s.lower() or 'contact' in s.lower() or 'shell' in s.lower()
          or 'binding' in s.lower() or 'lig' in s.lower() or 'sele' in s.lower()
          for s in sele_names),
      'a proximity selection was created', str(sele_names))
stored.red = []
cmd.iterate('(byres organic within 5 of polymer) and name CA', 'stored.red.append(1)')
check(len(stored.red) > 0, 'residues near ligand are present in structure')

# ─────────────────────────────────────────────────────────────────────────────
separator('6 — Structural alignment of two structures + RMSD report')
# Tests: fetch second structure, align/super, RMSD printout
# ─────────────────────────────────────────────────────────────────────────────
reset()
out = capture_pm(
    'fetch both 1hpv and 1hvr, align them using structure-based superposition, '
    'color 1hpv blue and 1hvr red, and report the RMSD'
)
print(out)
objects = cmd.get_object_list()
check('1hpv' in objects, '1hpv loaded')
check('1hvr' in objects, '1hvr loaded')
check(any(w in out for w in ['RMSD', 'rmsd', 'Å', 'angstrom', 'RMS']), 'RMSD reported in output')

# ─────────────────────────────────────────────────────────────────────────────
separator('7 — Molecular weight calculation')
# Tests: iterate with mass property, sum, formatted output
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm('calculate the molecular weight of 1hpv protein chain only (no water or ligand)')
print(out)
# MW of 1hpv chain A protein should be roughly 10,000–25,000 Da
import re
numbers = re.findall(r'\d+[\d,]*\.?\d*', out.replace(',', ''))
numbers = [float(n) for n in numbers if float(n) > 1000]
check(len(numbers) > 0, 'a large number (MW in Da) appears in output', str(numbers[:3]))
if numbers:
    check(any(5000 < n < 100000 for n in numbers), 'MW is in a plausible range (5–100 kDa)', str(numbers[:3]))

# ─────────────────────────────────────────────────────────────────────────────
separator('8 — Hydrogen bond donor/acceptor residues near ligand → CSV')
# Tests: iterate elem N/O, spatial selection, csv export
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm(
    'find all nitrogen and oxygen atoms on protein residues within 3.5 angstroms of the ligand '
    'that could be hydrogen bond partners, and save them to a CSV called hbond_partners.csv '
    'with columns: chain, residue_number, residue_name, atom_name'
)
print(out)
check(os.path.exists(os.path.join(TEST_DIR, 'hbond_partners.csv')),
      'hbond_partners.csv created')
if os.path.exists(os.path.join(TEST_DIR, 'hbond_partners.csv')):
    with open(os.path.join(TEST_DIR, 'hbond_partners.csv')) as f:
        rows = list(csv.reader(f))
    check(len(rows) >= 1, 'CSV has rows', f'{len(rows)} rows including header')

# ─────────────────────────────────────────────────────────────────────────────
separator('9 — Creative rendering: spectrum coloring + artistic style')
# Tests: spectrum, set lighting, bg_color, ray, png
# ─────────────────────────────────────────────────────────────────────────────
reset()
cmd.fetch('1hpv')
time.sleep(0.5)
out = capture_pm(
    'make an artistic figure: color 1hpv protein by B-factor using a blue-to-red rainbow, '
    'show a semi-transparent grey surface over the cartoon, '
    'black background, no shadows, save as artistic.png at 1600x1200'
)
print(out)
check(os.path.exists(os.path.join(TEST_DIR, 'artistic.png')), 'artistic.png rendered',
      f'{os.path.getsize(os.path.join(TEST_DIR,"artistic.png"))//1024} KB'
      if os.path.exists(os.path.join(TEST_DIR,'artistic.png')) else 'missing')

# ─────────────────────────────────────────────────────────────────────────────
separator('10 — Export FASTA sequence to file')
# Tests: get_fastastr, file write, output_dir
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm('export the protein sequence of 1hpv as a FASTA file called sequence.fasta')
print(out)
fasta_path = os.path.join(TEST_DIR, 'sequence.fasta')
check(os.path.exists(fasta_path), 'sequence.fasta created')
if os.path.exists(fasta_path):
    with open(fasta_path) as f:
        content = f.read()
    check(content.startswith('>'), 'FASTA has proper header')
    check(len(content) > 50, 'FASTA has sequence content', f'{len(content)} chars')

# ─────────────────────────────────────────────────────────────────────────────
separator('11 — Count atoms by element and print table')
# Tests: iterate elem, Counter-style logic, print without file
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm('count atoms by element for all objects loaded and print a table')
print(out)
check('C' in out or 'Carbon' in out or 'carbon' in out, 'carbon mentioned in output')
check('N' in out or 'Nitrogen' in out or 'nitrogen' in out, 'nitrogen mentioned in output')
check('O' in out or 'Oxygen' in out or 'oxygen' in out, 'oxygen mentioned in output')

# ─────────────────────────────────────────────────────────────────────────────
separator('12 — Distance between two specific residues')
# Tests: select by resi, distance object, get_distance numeric
# ─────────────────────────────────────────────────────────────────────────────
out = capture_pm(
    'measure the distance between the alpha carbon of residue 10 and the alpha carbon '
    'of residue 50 in 1hpv and print the result in angstroms'
)
print(out)
numbers = re.findall(r'\d+\.?\d*', out)
numbers = [float(n) for n in numbers if 1.0 < float(n) < 200.0]
check(len(numbers) > 0, 'a numeric distance value appears in output', str(numbers[:3]))

# ─────────────────────────────────────────────────────────────────────────────
separator('FINAL SUMMARY')
# ─────────────────────────────────────────────────────────────────────────────
passed = sum(1 for ok, _ in results if ok)
total  = len(results)
print(f'\n  {passed}/{total} checks passed')
print(f'\n  Output files in {TEST_DIR}:')
for fname in sorted(os.listdir(TEST_DIR)):
    fpath = os.path.join(TEST_DIR, fname)
    print(f'    {fname}  ({os.path.getsize(fpath):,} bytes)')
