def readFile():
    f = open("toArd.txt", "r")
    fread = f.read()
    listOfEntries =[""] * 11
    for x in range(9):
        fread = fread[fread.find(":")+1:]
        listOfEntries[x] = (fread[:fread.find(";")])
        fread = fread[fread.find(";"):]
    f = open("toPi.txt", "r")
    fread = f.read()
    for x in range(3):
        fread = fread[fread.find(":")+1:]
        listOfEntries[x+8] = (fread[:fread.find(";")])
        fread = fread[fread.find(";"):]
    return listOfEntries
print(readFile())
        
