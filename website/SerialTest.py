#!/usr/bin/env python
import serial
import time
import updateDB as db
ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 57600,
        timeout=1
)
counter=0
ser.flushInput()
ser.flushOutput()
start = [255, 255, 253, 0]
def param2Temp(params):
    temps = [None] * int(len(params)/2)
    for x in range(int(len(params)/2)):
        temps[x]=float(params[x*2])+float(params[x*2+1])/100
        print(x)
    return temps
               
def listen():
    count=0
    line = [0x02,0x02,0x02,0x02,0x02]
    while True:
        line[count] = ser.read()
        if (line[count]):
            a = 0
        else:
            break
        if (count == 4):
            proceed = True
            packet = [None] * ord(line[4])
            for i in range(5):
                packet[i] = line[i]
                if (i < 4):
                    if (start[i] != ord(line[i])):
                        proceed = False
            for x in range(ord(line[count])-5):
                packet[x+5]=ser.read()
                
            if ord(packet[-1]) == 254 and proceed == True:
                print("Packet Received succefully")
                print("Instruction:" + str(ord(packet[5])))
                print("Params :")
                params = [None] * (ord(packet[4])-7)
                for i in range(ord(packet[4])-7):                    
                    params[i] = ord(packet[i+6])
                return params
                print(";;;")
            break
        count += 1
        
while True:
    '''count=0
    line = [0x02,0x02,0x02,0x02,0x02]
    while True:
        line[count] = ser.read()
        if (line[count]):
            a = 0
        else:
            break

        if (count == 4):
            proceed = True
            packet = [None] * ord(line[4])
            for i in range(5):
                packet[i] = line[i]
                if (i < 4):
                    if (start[i] != ord(line[i])):
                        proceed = False
            for x in range(ord(line[count])-5):
                packet[x+5]=ser.read()
                
            if ord(packet[-1]) == 254 and proceed == True:
                print("Packet Received succefully")
                print("Instruction:" + str(ord(packet[5])))
                print("Params :")
                for i in range(ord(packet[4])-7):
                    print(ord(packet[i+6]))
                    params[i] = ord(packet[i+6])
                print(";;;")
                
            break
        count += 1'''


    a = input()
    #ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x1,0x9,0x9,0x9,0xfe]))
    if a == 1:
        time.sleep(.3)
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x1,0x9,0x9,0x9,0xfe]))
        params = listen()
        print(params)
        temps = param2Temp(params)
        #print(temps)
        db.writeTmp("toPi.txt",temps)
        time.sleep(.3)
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0x08,0x2,0x9,0xfe]))
        params = listen()
        print(params)
        db.updateUnits("toPi.txt",params)
        #db.writeTmp("toPi.txt",temps)
    elif a == 2:
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xd,0x3,0x1,0x1,0x1,0x0,0x0,0x1,0xfe]))

    elif a == 3:
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x4,0x0,0x5,0x4,0xfe]))
    elif a == 4:
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x4,0x1,0x4,0x4,0xfe]))
