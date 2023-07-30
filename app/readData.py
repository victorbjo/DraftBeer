#import tempRead
import time
import numpy as np
import os

localTime = time.localtime(time.time())
localTimeHour = str(localTime.tm_hour)

path = os.path.abspath(os.getcwd())
jsonData10Sec = (np.load(path+"/data10Sec.npz"))
data3Min = np.load("data3Min.npz")

def printData():
    for x in range(jsonData10Sec['temp'].size):
        print(jsonData10Sec['temp'][x] + "C @"+jsonData10Sec['time'][x])

    print("3Min data")
    for x in range(data3Min['temp'].size):
        print(data3Min['temp'][x] + "C @"+data3Min['time'][x])

def getData3Min():
    jsonData = (np.load(path+"/data3Min.npz"))
    return jsonData
def getData10Sec():
    jsonData = (np.load(path+"/data10Sec.npz"))
    return jsonData
#print(jsonData10Sec['temp'].size)
#printData()
