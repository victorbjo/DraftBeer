import numpy as np
import think
import readData
import time
syns = np.load('NN.npy')
syn0 = syns[0]
syn1 = syns[1]
syn2 = syns[2]
syn3 = syns[3]
syn4 = syns[4]
print("loaded")
print ("Ready!")
def addTime(minutes):
    localTime = time.localtime(time.time())
    localTimeMin = (localTime.tm_min)
    localTimeHour = (localTime.tm_hour)
    extraTimeHour = int(int(minutes)/60)
    localTimeHour += extraTimeHour
    localTimeMin += int(minutes)-(extraTimeHour*60)
    return(str(localTimeHour)+":"+str(localTimeMin))
def estimate():
    data = np.array([readData.getData3Min()['temp']])
    Y = 0
    X = np.array([data[0][-20:data.size]])
    X = X.astype(float)
    result = (think.think(X,Y,syn0,syn1,syn2,syn3,syn4,0.1,False))
    resultRounded = [0]*8
    for x in range(result[0].size):
        resultRounded[x]=int(round(result[0][x],0))
    out = 0
    for bit in resultRounded:  #Converts results(binary) into an int
        out = (out << 1) | bit 
    return (addTime(out))

