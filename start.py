import subprocess
process = subprocess.Popen(
        ["git", "clone", "https://github.com/DARK-COBRA/DARKCOBRA", "root/cobra"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
process.communicate()

import os 

os.chdir(os.path.abspath(os.path.expanduser('root/cobra')))

process = subprocess.Popen(
        ["python3", "-m", "userbot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
print(er)
print("::::::::::::::")
print(out)
