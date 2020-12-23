import time

def writeTmp(file,Tmps):
    f = open(file,"r")
    print(Tmps)
    tempPart1 = "Tmp1:"+str(Tmps[0])+";\n"
    tempPart2 = "Tmp2:"+str(Tmps[1])+";\n"
    tempPart3 = "Tmp3:"+str(Tmps[2])+";\n"
    tempPart=tempPart1 + tempPart2 + tempPart3 
    ff = f.read()
    f.close()
    f = open(file, "w")
    after = ff[ff.find("C0"):]
    print(after)
    ff= tempPart + after
    
    f.write(ff)
    f.close()
    #print("")
def auto(file, auto):
    f = open(file,"r")
    ff = f.read()
 
    f.close()
    f = open(file, "w")
    after = ff[:ff.find(";\n")]
    before = after[:ff.find(":")]
    fAuto = before+":"+str(auto)+";\n"
    fRest = ff[ff.find("\n")+1:]
    
    f.write(fAuto + fRest)
    f.close()
    #print(fAuto + fRest)
def updateUnits(file,units):
    f = open(file,"r")
    ff = f.read()
    f.close()
    f = open(file, "w")
    after = ff[:ff.find("C0")]
    unitStr =""
    for x in range(6):
        unitStr += "C"+str(x)+":"+str(units[x])+";\n"
    print(after)
    f.write(after+unitStr)
def goalTemp(file, temp):
    f = open(file,"r")
    ff = f.read()
    f.close()
    f = open(file, "w")
    before = ff[:ff.find("Temp")]
    after = ff[ff.find("Temp")+5:]
    after = after[after.find(";"):]
    f.write(str(before)+"Temp:"+str(temp)+str(after))
    f.close()
'''
goalTemp("ToArd.txt",10)

a = time.time()
writeTmp("toPi.txt",[12,00,45,6,78,9])
updateUnits("toPi.txt",[1,0,1,0,1,1])
b = time.time()
auto("toArd.txt",1)
updateUnits("toArd.txt",[1,0,1,0,1,1])
c = time.time()
print("A-B: "+str(b-a)+"; B-C: "+str(c-b)+";\nOverall: "+str(c-a))
'''
