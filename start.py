import os 
import subprocess
os.system("git clone https://github.com/DARK-COBRA/DARKCOBRA /root/cobra && cd /root/cobra")

process = subprocess.Popen(
        ["python3", "-m", "userbot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    print(er.decode())
print("::::::::::::::")
if out:
    print(out.decode())
