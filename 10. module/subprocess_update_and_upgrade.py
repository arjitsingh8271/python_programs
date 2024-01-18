import subprocess

subprocess.call("sudo apt update", shell=True)
subprocess.call("sudo apt upgrade", shell=True)
subprocess.call("clear", shell=True)
subprocess.call("exit", shell=True)
