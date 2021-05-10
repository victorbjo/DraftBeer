import RPi.GPIO as GPIO
import time
import numpy as np
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

        try:
            tempTarget = target.readTarget()
            tempTarget = float(tempTarget)
        except:
            tempTarget = 3
            print("Something went wrong, could not read TempTarget")
        time.sleep(0.01)
        #print("\n\n")
        
        #print(tempTarget)
        #print("ok")
	#print(GPIO.input(pumps))
        try:
            actualTemp = tempRead.get_temp()
        except:
            print("Could not read temp")
            actualTemp = 5
        #print(actualTemp)
        #print("her")
        #actualTemp = tempRead.read_temp()
        #actualTemp = tempRead.get_temp()
        if tempTarget > float(actualTemp) + 0.5 and GPIO.input(pumps) == 1:
            print("Turning OFF coolers")
            GPIO.output(pumps,GPIO.LOW)
            GPIO.output(peltier,GPIO.LOW)
            recentlyCycled = False
        elif tempTarget < actualTemp and GPIO.input(pumps) == 0:
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
    except:
        print("\n\nSomething went terribly wrong!!!\n\n")


