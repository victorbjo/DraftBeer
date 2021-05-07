import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
while True:
    pin = int(input("Choose a pin: "))
    GPIO.setup(int(pin),GPIO.OUT)
    print(str(GPIO.input(pin)))