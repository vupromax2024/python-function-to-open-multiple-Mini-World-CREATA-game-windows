import subprocess
import os

exe = os.path.expandvars(r"%AppData%\miniworldOverseasgame\MiniGameApp.exe")
param = 'parenthwnd=0'
cmd = f'{exe} {param}'

subprocess.Popen(cmd, cwd=os.path.dirname(exe))