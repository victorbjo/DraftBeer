import tempRead
import time
import numpy as np
import os
path = os.path.abspath(os.getcwd()) #Absolute path of current file


localTime = time.localtime(time.time())
localTimeMin = str(localTime.tm_min)
localTimeHour = str(localTime.tm_hour)
localTimeSec = str(localTime.tm_sec)
temps = tempRead.read_temp()
temps = round(temps, 2)
temps = format(temps, '.2f')

if int(localTimeHour) < 10:
    localTimeHour = "0"+localTimeHour
if int(localTimeMin) < 10:
    localTimeMin = "0"+localTimeMin

timeStamp3Min = np.array([localTimeHour+":"+localTimeMin])
timeStamp10Sec = np.array([localTimeHour+":"+localTimeMin])
dataTemp3Min = np.array([temps])
dataTemp10Sec = np.array([temps])
counterMin = 0 #To make sure that "old" date doesnt get deleted
counterSec = 0 #same
numOfEntries = 361 #Maximum number of entries in a dataset before it gets saved as an old
fiveMin = False

while True:
    localTime = time.localtime(time.time())
    localTimeMin = str(localTime.tm_min)
    localTimeHour = str(localTime.tm_hour)
    localTimeSec = str(localTime.tm_sec)
    if int(localTimeHour) < 10:
        localTimeHour = "0"+localTimeHour
    if int(localTimeMin) < 10:
        localTimeMin = "0"+localTimeMin


        
    if int(localTimeMin)%3 == 0 and fiveMin == False: #Will log every 3rd min, as long as it hasnt done so in same min
        temps = tempRead.read_temp()
        temps = round(temps, 2)
        temps = format(temps, '.2f')
        timeStamp3Min = np.append(timeStamp3Min,[localTimeHour+":"+localTimeMin])
        dataTemp3Min = np.append(dataTemp3Min,[temps])
        print("Saving temp: "+str(temps)+" and timestamp @"+timeStamp3Min[-1])
        np.savez('data3Min', temp=dataTemp3Min, time=timeStamp3Min)
        fiveMin = True
        counterMin = counterMin +1 
        if timeStamp3Min.size > numOfEntries:
            timeStamp3Min = np.delete(timeStamp3Min,0,0)
        if dataTemp3Min.size > numOfEntries:
            dataTemp3Min = np.delete(dataTemp3Min, 0, 0)
        counterMin = counterMin + 1
    elif int(localTimeMin)%3!=0:
        fiveMin = False
        
        
    if int(localTimeSec)%10 == 0:  #Will log every 10th sec
        temps = tempRead.read_temp()
        temps = round(temps, 2)
        temps = format(temps, '.2f')
        timeStamp10Sec = np.append(timeStamp10Sec,[localTimeHour+":"+localTimeMin])
        dataTemp10Sec = np.append(dataTemp10Sec,[temps])
        print("Saving temp: "+str(temps)+" and timestamp @"+timeStamp10Sec[-1])
        np.savez('data10Sec', temp=dataTemp10Sec, time=timeStamp10Sec)
        time.sleep(1)
        counterSec = counterSec + 1
        if timeStamp10Sec.size > numOfEntries:
            timeStamp10Sec = np.delete(timeStamp10Sec,0,0)
        if dataTemp10Sec.size > numOfEntries:
            dataTemp10Sec = np.delete(dataTemp10Sec, 0, 0)

    if counterSec >= numOfEntries:
        print("Renaming data10Sec.npz into oldLogs/data10Sec"+localTimeHour+".npz")
        os.rename("data10Sec.npz", "oldLogs/data10Sec"+localTimeHour+".npz")
        counterSec = 0
    if counterSec >= numOfEntries:
        print("Renaming data10Sec.npz into oldLogs/data10Sec"+localTimeHour+".npz")
        os.rename("data10Sec.npz", "oldLogs/data10Sec"+localTimeHour+".npz")
        counterSec = 0