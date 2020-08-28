import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

        
while True:
    semiCounter = 0
    line = ser.readline().decode('utf-8').rstrip()
    parsedLine = ""
    for x in range (len(line)):
        if semiCounter < 3:
            if line[x] == ":":
                semiCounter = semiCounter + 1
                parsedLine = parsedLine + ";"
            else:
                parsedLine = parsedLine + line[x]
        else:
            if line[x].isnumeric():
               parsedLine = parsedLine + line[x]+";"
            else:
                semiCounter = semiCounter + 1
    if len(parsedLine)>8:
        f = open("tempInfo.txt", "a")
        temp = parsedLine[-4] +"."+parsedLine[-2]
        parsedLine = parsedLine[:-5]
        
        parsedLine = parsedLine+temp
        f.truncate(0)
        f.write(parsedLine)
        
        print(parsedLine)
        f.close()
        time.sleep(.1)

    
