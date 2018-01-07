import os
import subprocess,signal

p = subprocess.Popen('tasklist',stdout=subprocess.PIPE)
out,err = p.communicate()

#print (out)

for line in out.splitlines():
  if 'chrome.exe' in line:
    #print (line)
    #print (line.split(None,1)[1].split()[0])
    pid = int(line.split(None,1)[1].split()[0])
    print (pid)
    os.system('taskkill /pid '+(str)(pid)+' -t -f ')
    #os.kill(pid,signal.SIGKILL)
#os.kill ('chrome.exe')

