import numpy as np
f = open("test.txt", "r")
fread = f.read()
print(fread[0])
#temps = np.array(["","","","","","","","",""])
tempsCount=0
temps = ["","",""]
print(temps)
for x in range(len(fread)):
    if fread[x] != ";" and fread[x].isnumeric():
        temps[tempsCount] = temps[tempsCount] + str(fread[x])
    else:
        tempsCount =+ 1
print(temps)
