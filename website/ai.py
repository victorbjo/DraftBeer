import numpy as np
import think
import readData
import time
import target
syns = np.load('NN.npy')
syn0 = syns[0]
syn1 = syns[1]
syn2 = syns[2]
syn3 = syns[3]
syn4 = syns[4]
#print(syn0.shape)
print("loaded")
print ("Ready!")
def addTime(minutes):
    localTime = time.localtime(time.time())
    localTimeMin = (localTime.tm_min)
    localTimeHour = (localTime.tm_hour)
    extraTimeHour = int(int(minutes)/60)
    localTimeHour += extraTimeHour
    localTimeMin += int(minutes)-(extraTimeHour*60)
    if localTimeMin >= 60: #Converts every 60 min to hour
        localTimeMin -= 60
        localTimeHour += 1
    if int(localTimeHour) > 23: #Converts over 24 hours to 00
        localTimeHour = str(int(localTimeHour)-24)
    return(str(localTimeHour)+":"+str(localTimeMin))

def prepareData():
    data = np.array([readData.getData3Min()['temp']])
    data = np.array([data[0][-20:]])
    print(data.size)
    #print(np.array([readData.getData3Min()['goal']]))
    tempArray = np.array([[str(float(target.readTarget())/10)]])
    buffer = np.array([[data[0][0]]])
    #print(tempArray)
    while (data[0].size < 19):
        #print(data[0].size)
        print(data[0].size)
        data = np.array([np.append(buffer, data)])
        #print(data[0].size)
    data = np.array([np.append(tempArray, data)])
    return data

def estimate():
    X = prepareData()
    Y = 0
    #print(X.shape)
    X = X.astype(float)
    print(X.size)
    print("x")
    result = (think.think(X,Y,syn0,syn1,syn2,syn3,syn4,0.1,False))
    resultRounded = [0]*9
    for x in range(result[0].size):
        resultRounded[x]=int(round(result[0][x],0))
    out = 0
    for bit in resultRounded:  #Converts results(binary) into an int
        out = (out << 1) | bit 
    return (addTime(out))
print(estimate())
