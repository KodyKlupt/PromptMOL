"""
PromptMol pmcfg + pmlog command tests
Run: conda activate pymol && python test_config_log.py
"""
import sys, os, json, time

sys.path.insert(0, '/Users/kodyklupt/Documents/claudecode')
import pymol
pymol.finish_launching(['pymol', '-c', '-q'])
from pymol import cmd
time.sleep(1)

import promptmol
from promptmol import config, session
promptmol.__init_plugin__()

TEST_DIR = os.path.expanduser('~/Desktop/promptmol_test_output/config_log_tests')
os.makedirs(TEST_DIR, exist_ok=True)
CONFIG_PATH = os.path.expanduser('~/.promptmol.json')

PASS = '  ✓'
FAIL = '  ✗'

def separator(title):
    print(f'\n{"="*60}')
    print(f'  TEST: {title}')
    print('='*60)

def check(condition, label, extra=''):
    if condition:
        print(f'{PASS} {label}' + (f'  [{extra}]' if extra else ''))
    else:
        print(f'{FAIL} FAILED: {label}' + (f'  [{extra}]' if extra else ''))

def read_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {}

# ── Save original config to restore at end ───────────────────────────────────
original_config = read_config()

# =============================================================================
separator('1 — pmcfg show (baseline)')
# =============================================================================
print()
promptmol._pmcfg('show')

# =============================================================================
separator('2 — pmcfg set: output_dir')
# =============================================================================
promptmol._pmcfg(f'set output_dir {TEST_DIR}')
cfg = read_config()
check(cfg.get('output_dir') == TEST_DIR, 'output_dir written to config', cfg.get('output_dir'))

# =============================================================================
separator('3 — pmcfg set: max_history (integer conversion)')
# =============================================================================
promptmol._pmcfg('set max_history 5')
cfg = read_config()
check(cfg.get('max_history') == 5, 'max_history stored as int', str(cfg.get('max_history')))
# Confirm session object updated live
sess = session.get_session()
check(sess.max_history == 5, 'session.max_history updated live', str(sess.max_history))

# =============================================================================
separator('4 — pmcfg set: api_key (masked in show)')
# =============================================================================
promptmol._pmcfg('set api_key test-key-12345')
cfg = read_config()
check(cfg.get('api_key') == 'test-key-12345', 'api_key stored correctly')
# Confirm it shows as *** in pmcfg show
print('  pmcfg show output (api_key should show as ***):', end=' ')
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmcfg('show')
output = buf.getvalue()
check('api_key = ***' in output, 'api_key masked in pmcfg show')
check('test-key-12345' not in output, 'raw key not printed in pmcfg show')

# =============================================================================
separator('5 — pmcfg set: switch backend to openai')
# =============================================================================
promptmol._pmcfg('set backend openai')
cfg = read_config()
check(cfg.get('backend') == 'openai', 'backend set to openai')

# =============================================================================
separator('6 — pmcfg set: switch backend to anthropic')
# =============================================================================
promptmol._pmcfg('set backend anthropic')
cfg = read_config()
check(cfg.get('backend') == 'anthropic', 'backend set to anthropic')

# =============================================================================
separator('7 — pmcfg set: switch backend back to lmstudio')
# =============================================================================
promptmol._pmcfg('set backend lmstudio')
cfg = read_config()
check(cfg.get('backend') == 'lmstudio', 'backend restored to lmstudio')

# =============================================================================
separator('8 — pmcfg set: invalid backend rejected')
# =============================================================================
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmcfg('set backend badvalue')
output = buf.getvalue()
cfg = read_config()
check('badvalue' not in cfg.get('backend', ''), 'invalid backend rejected')
check('must be one of' in output, 'error message printed for invalid backend')

# =============================================================================
separator('9 — pmcfg set: invalid key rejected')
# =============================================================================
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmcfg('set nonexistent_key foo')
output = buf.getvalue()
check('Unknown config key' in output, 'unknown key rejected with error message')

# =============================================================================
separator('10 — pmcfg set: model name with spaces (multi-token value)')
# =============================================================================
promptmol._pmcfg('set model my-local-model-q4')
cfg = read_config()
check(cfg.get('model') == 'my-local-model-q4', 'model name set', cfg.get('model'))

# =============================================================================
separator('11 — pmlog show when session is empty')
# =============================================================================
session.reset_session()
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmlog('show')
output = buf.getvalue()
check('no exchanges' in output.lower(), 'pmlog show handles empty session gracefully')

# =============================================================================
separator('12 — pmlog show after a real pm command')
# =============================================================================
cmd.fetch('1hpv')
time.sleep(0.5)
promptmol._pm('color the protein white')
time.sleep(1)

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmlog('show')
output = buf.getvalue()
check('color the protein white' in output, 'pmlog show contains user prompt')
check('Prompt' in output, 'pmlog show has Prompt label')
check('Summary' in output, 'pmlog show has Summary label')
check('cmd.' in output, 'pmlog show contains generated code')

# =============================================================================
separator('13 — pmlog save: auto filename')
# =============================================================================
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmlog('save')
output = buf.getvalue()
check('session log saved' in output.lower(), 'pmlog save auto-filename reported')
saved_logs = [f for f in os.listdir(TEST_DIR) if f.startswith('promptmol_session_')]
check(len(saved_logs) >= 1, 'auto-named session log file created', str(saved_logs))

# =============================================================================
separator('14 — pmlog save: explicit filename')
# =============================================================================
log_path = os.path.join(TEST_DIR, 'my_session.py')
promptmol._pmlog(f'save {log_path}')
check(os.path.exists(log_path), 'pmlog save explicit filename created')
if os.path.exists(log_path):
    with open(log_path) as f:
        content = f.read()
    check('from pymol import cmd' in content, 'session log has cmd import header')
    check('# ── Step 1' in content, 'session log has step markers')
    check('# Prompt:' in content, 'session log has prompt annotations')
    check('cmd.' in content, 'session log contains generated code')
    print(f'  Log file size: {os.path.getsize(log_path)} bytes')

# =============================================================================
separator('15 — pmlog save: invalid subcommand')
# =============================================================================
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmlog('badcmd')
output = buf.getvalue()
check('Usage' in output or 'usage' in output, 'invalid pmlog subcommand shows usage')

# =============================================================================
separator('16 — pmreset clears both conversation and log')
# =============================================================================
sess = session.get_session()
msgs_before = len(sess.get_messages())
log_before  = len(sess.get_log())
check(msgs_before > 0, 'session has messages before reset', str(msgs_before))
check(log_before  > 0, 'session has log entries before reset', str(log_before))

promptmol._pmreset()

msgs_after = len(sess.get_messages())
log_after  = len(sess.get_log())
check(msgs_after == 0, 'conversation messages cleared after pmreset')
check(log_after  == 0, 'log entries cleared after pmreset')

# =============================================================================
separator('17 — pmlog save after pmreset (should report empty)')
# =============================================================================
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmlog('save')
output = buf.getvalue()
check('no exchanges' in output.lower(), 'pmlog save after pmreset reports empty session')

# =============================================================================
separator('18 — pmsave when no script generated')
# =============================================================================
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    promptmol._pmsave()
output = buf.getvalue()
check('no script' in output.lower(), 'pmsave with no prior script reports correctly')

# =============================================================================
separator('19 — Restore original config')
# =============================================================================
if original_config:
    with open(CONFIG_PATH, 'w') as f:
        json.dump(original_config, f, indent=2)
    print(f'  Original config restored from backup.')
else:
    os.remove(CONFIG_PATH)
    print(f'  Config file removed (was not present before tests).')

# =============================================================================
separator('SUMMARY — output files')
# =============================================================================
print(f'\n  Files in {TEST_DIR}:')
for fname in sorted(os.listdir(TEST_DIR)):
    fpath = os.path.join(TEST_DIR, fname)
    print(f'    {fname}  ({os.path.getsize(fpath)} bytes)')
print('\n  Config + log tests complete.')
