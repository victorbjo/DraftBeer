import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin = 14
GPIO.setup(pin,GPIO.OUT)

coolers = False
while True:
    GPIO.output(pin,GPIO.LOW)
    print(pin)
    print(GPIO.input(pin))
    time.sleep(1)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(5)


