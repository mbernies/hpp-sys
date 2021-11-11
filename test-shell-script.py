import subprocess
import shlex

subprocess.run("ls -al", shell=True)
print("Current email queue " + subprocess.run("ls", shell=True))
