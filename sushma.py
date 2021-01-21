mydir = "F:/TrainTicketing1"
for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".txt") and filename=="test11log.txt":
            file=open(filepath)
            for line in file:
                if "Caused by:" in line :
                    L=line.split()
                    for i in range(0,len(L)):
                        string_encode = L[i].encode("ascii", "ignore")
                        string_decode = string_encode.decode()
                        #L[i]=string_decode 
                        if L[i]=="Caused":
                            for j in range(0,20):
                                 L1.append(L[i+j])

            for i in range(0,len(L1)):
                if L1[i].startswith("com."):
                    L2.append(L1[i])
            print("List of packages with Exception:",L2)
            print("\n")   
