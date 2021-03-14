import os
from time import sleep
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor = '/sys/bus/w1/devices/28-0114485317aa/w1_slave'
def read_temp_raw():

   f = open(temp_sensor, 'r')
   lines = f.readlines()
   f.close()
   return lines

def read_temp():

   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':
      sleep(0.2)
      lines = read_temp_raw()
   temp_result = lines[1].find('t=')

   if temp_result != -1:
      temp_string = lines[1].strip()[temp_result + 2:]
      # Temperature in Celcius
      temp = float(temp_string) / 1000.0
      # Temperature in Fahrenheit
      #temp = ((float(temp_string) / 1000.0) * (9.0 / 5.0)) + 32.0
      return temp

