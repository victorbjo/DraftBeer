import RPi.GPIO as GPIO
import time
import numpy as np
import datetime
import target
import tempRead
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pumps = 24
peltier = 25
GPIO.setup(pumps,GPIO.OUT)
GPIO.setup(peltier,GPIO.OUT)
recentlyCycled = False
coolers = False
while True:
    
    try:
        tempTarget = target.readTarget()
        tempTarget = float(tempTarget)
        time.sleep(0.01)
        #print("\n\n")
        #print(tempTarget)
        #print(GPIO.input(pumps))
        actualTemp = tempRead.get_temp()
        #print(actualTemp)
        #print("\n\n")
        #actualTemp = tempRead.read_temp()
        #actualTemp = tempRead.get_temp()
        if tempTarget > actualTemp + 0.5 and GPIO.input(pumps) == 1:
            print("Turning OFF coolers")
            GPIO.output(pumps,GPIO.LOW)
            GPIO.output(peltier,GPIO.LOW)
            recentlyCycled = False
        elif tempTarget< actualTemp and GPIO.input(pumps) == 0:
            print("Turning ON coolers")
            GPIO.output(pumps,GPIO.HIGH)
            GPIO.output(peltier,GPIO.HIGH)
            recentlyCycled = False
        elif tempTarget < actualTemp + 0.2 and GPIO.input(pumps) == 0 and recentlyCycled == False:
            GPIO.output(pumps,GPIO.HIGH)
            GPIO.output(peltier,GPIO.HIGH)
            print("Cycling hot water")
            time.sleep(5)
            GPIO.output(pumps,GPIO.LOW)
            GPIO.output(peltier,GPIO.LOW)
            recentlyCycled = True
        '''except Exception as e:
            print("Failed to do it")
            print(e)
            print(type(tempTarget))
            print(type(actualTemp))
            print(type(GPIO.input(14)))
            print("Failed to do it")
            #exit()'''
    except Exception as e:
        f = open("crash.txt", "a")
        now = datetime.datetime.now()
        f.write("Site crashed @ " + str(now.hour)+":"+str(now.minute)+"\n")
        f.write(str(e))
        f.write("\n")
        f.close()

