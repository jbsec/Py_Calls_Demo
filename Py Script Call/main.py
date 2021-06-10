import subprocess

cmd = 'python script.py'
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
print(err)
print(out)
