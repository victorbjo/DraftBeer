#!/usr/bin/env python
import serial
import time
ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 57600,
        timeout=1
)
counter=0
ser.flushInput()
ser.flushOutput()
while True:
    #line = ser.readline().decode('utf-8').rstrip()
    #print(line)
    a = input()
    if a == 1:
        ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0x01,0x08,0xFB,0xfe]))
    else:
        ser.write(serial.to_bytes([0xff,0xff,0xfd]))
