import subprocess
result=subprocess.call(["echo","Hello Python"], shell=True)

result=subprocess.run(["echo","Hello Python"], shell=True)

res=subprocess.run(["ls","-l"], shell=True)

