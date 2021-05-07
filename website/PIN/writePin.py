import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
while True:
    pin = int(input("Choose a pin: "))
    GPIO.setup(int(pin),GPIO.OUT)
    print("Pin " + str(pin) + " status:"+str(GPIO.input(pin)))
    if (GPIO.input(pin) == 0):
        print("Turning it on")
        GPIO.output(pin,GPIO.HIGH)
    else:
        print("Turning it off")
        GPIO.output(pin,GPIO.LOW)