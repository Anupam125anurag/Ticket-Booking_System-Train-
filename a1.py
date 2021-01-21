import os
import time
L=[]
L1=[]
L2=[]


#fetching file from the root folder
mydir = "F:/TrainTicketing1"
for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".txt") and filename=="test11log.txt":
            file=open(filepath,'r').read().splitlines()
            print(file)
            for elements in range(0,len(file)):
                if "caused by" in file[elements]:
                    print(file[elements])
                    print(file[elements+1])
                    
