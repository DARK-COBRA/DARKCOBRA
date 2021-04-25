import os 
import subprocess
os.system("git clone https://github.com/DARK-COBRA/DARKCOBRA cobra && cd cobra")
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
os.system("rm -rf /usr/local/lib/python3.9/site-packages/.wh*")
