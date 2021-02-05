import os
import time
mydir = "F:/jenkinsWorkspace/.jenkins/workspace/testAndroid"
for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".txt"):
            if filename=="kernel3log.txt":
                file=open(filepath,'r').read().splitlines()
                for elements in range(0,len(file)):
                    if "Wakeup pending" in file[elements]:
                       print(file[elements])
                       print(file[elements+1])
                       print(file[elements+2])
            elif filename=="test11log.txt":
                file=open(filepath,'r').read().splitlines()
                for elements in range(0,len(file)):
                    if "Caused by" in file[elements]:
                       print(file[elements])
                       print(file[elements+1])
                       print(file[elements+2])
                      
