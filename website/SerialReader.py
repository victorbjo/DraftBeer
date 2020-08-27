import serial
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
    if len(parsedLine)>8:
        temp = parsedLine[-4] +"."+parsedLine[-2]
        parsedLine = parsedLine[:-4]
        print(temp)
    print(parsedLine)
    
