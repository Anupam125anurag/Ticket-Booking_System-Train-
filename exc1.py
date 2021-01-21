import os
import re
#L=[]
#L1=[]
#L2=[]

mydir = "F:/TrainTicketing1/"
for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".txt"):
            if filename=="test11log.txt":
                print(filepath)
                print("\n")
