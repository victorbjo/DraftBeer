import RPi.GPIO as GPIO
import time
import tempRead
import target
import numpy as np
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
coolers = False
while True:
    try:

        tempTarget = target.readTarget()
        #actualTemp = tempRead.read_temp()
        f = open("tempDataMain.txt","r")
        actualTemp = float(f.read())
        f.close()
        if float(tempTarget) > actualTemp + 0.5 and GPIO.input(14) == 1:
            print("Turning OFF coolers")
            GPIO.output(14,GPIO.LOW)
        elif float(tempTarget)< actualTemp and GPIO.input(14) == 0:
            print("Turning ON coolers")
            GPIO.output(14,GPIO.HIGH)
        elif float(tempTarget) < actualTemp + 0.2 and GPIO.input(14) == 0:
            GPIO.output(14,GPIO.HIGH)
            print("Cycling hot water")
            time.sleep(2)
            GPIO.output(14,GPIO.LOW)
        time.sleep(0.5)
    except Exception as e:
        print(e)
        print(tempTarget)
        print(actualTemp)
        #exit()


