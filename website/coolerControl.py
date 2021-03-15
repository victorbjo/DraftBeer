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
    temp = np.load("data10Sec.npz")
    tempTarget = target.readTarget()
    #actualTemp = tempRead.read_temp()
    actualTemp = float(temp['temp'][-1])
    #print(tryTemp[-1])
    if float(tempTarget) < actualTemp + 0.5:
        if (coolers == False):
            print("Turning ON coolers")
            GPIO.output(14,GPIO.HIGH)
            coolers = True
    else:
        if (coolers == True):
            print("Turning OFF coolers")
            GPIO.output(14,GPIO.LOW)
            coolers = False
    time.sleep(0.5)
