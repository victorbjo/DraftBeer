def readFile(file):
    f = open(file, "r")
    fread = f.read()
    listOfEntries =[""]
    count = 0
    for x in range(len(fread)):
        if(fread[x] != ";"):
            listOfEntries[count]=listOfEntries[count]+fread[x]
        else:
            count = count + 1;
            listOfEntries.append("")
    return listOfEntries

        
