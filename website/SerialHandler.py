#!/usr/bin/env python
import serial
import time
import updateDB as db
from datetime import datetime
start = [255, 255, 253, 0]
ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 57600,
        timeout=1
)
def param2Temp(params):
    temps = [None] * int(len(params)/2)
    for x in range(int(len(params)/2)):
        temps[x]=float(params[x*2])+float(params[x*2+1])/100
        print(x)
    return temps
def listen():
    count=0
    line = [0x02,0x02,0x02,0x02,0x02]
    print("ISAI")
    while True:
        line[count] = ser.read()
        print("AM HERE")
        print(line)
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
                print("asd")
                print(packet)
                return params
                print(";;;")
            break
        count += 1
        
counter=0
ser.flushInput()
ser.flushOutput()
start = [255, 255, 253, 0]
def changeUnitStatus(state, temp):
    
    if (int(state[0])!=3):
        print("Changing units. FUCK ME")
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xd,0x3,int(state[0]),int(state[1])
                               ,int(state[2]),int(state[3]),int(state[4]),int(state[5]),0xfe]))
        time.sleep(0.1)
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x4,0x0,0x5,0x4,0xfe]))
        db.auto("toArd.txt",0)
        db.updateUnits("toArd.txt",state)
        db.goalTemp("toArd.txt",temp)
    else:
        temp2 = int((float(temp)-int(temp))*10)
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x4,0x1,int(temp),temp2,0xfe]))
        db.auto("toArd.txt",1)
        db.updateUnits("toArd.txt",state)
        db.goalTemp("toArd.txt",temp)
    print(int(state[0])!=3)
def getTemps():
    now = datetime.now()
    current_time = now.strftime("%S")
    if (int(current_time)%5 == 0):
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x1,0x9,0x9,0x9,0xfe]))
        params = listen()
        #print(params)
        temps = param2Temp(params)
        #print(temps)
        db.writeTmp("toPi.txt",temps)



    
