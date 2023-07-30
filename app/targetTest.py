import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
    a = time.time()
    temperature = sensor.get_temperature()
    #print("The temperature is %s celsius" % temperature)
    print(time.time()-a)