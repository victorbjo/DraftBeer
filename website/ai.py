import numpy as np
import think
import readData
import time
import target
synss = np.load('NN.npy')
syn0 = synss[0]
syn1 = synss[1]
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
    data = np.array([readData.getData10Sec()['temp']]) #Loads last 20 data entries
    #print(data)
    #print("HERE")
    data = np.array([data[0][-20:]])
    print(data)
    #print(data.size)
    #print(np.array([readData.getData3Min()['goal']]))
    #print(data)
    tempArray = np.array([[str(float(target.readTarget())/10)]])
    buffer = np.array([[data[0][0]]])
    #print(tempArray)
    while (data[0].size < 20):  #19 or 20, ehh
        #print(data[0].size)
        print(data[0].size)
        data = np.array([np.append(buffer, data)])
        #print(data[0].size)
    data = np.array([np.append(data, tempArray)])
    print (data)
    return data

def estimate():
    X = prepareData()
    Y = 0
    #print(X.shape)
    X = X.astype(float)
    print(X)
    print(X.size)
    print("x")
    result = (think.think(X,Y,syn0,syn1,0.1,False))
    resultRounded = [0]*9
    for x in range(result[0].size):
        resultRounded[x]=int(round(result[0][x],0))
    out = 0
    for bit in resultRounded:  #Converts results(binary) into an int
        out = (out << 1) | bit 
    return (addTime(out))
#print(estimate())
