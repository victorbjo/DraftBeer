import os
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor0 = '/sys/bus/w1/devices/28-0114485317aa/w1_slave'
temp_sensor1 = '/sys/bus/w1/devices/28-0000079a27fb/w1_slave'  
temp_sensor2 ='/sys/bus/w1/devices/28-0000079b4382/w1_slave' 
def read_temp_raw(sensor):

   f = open(sensor, 'r')
   lines = f.readlines()
   f.close()
   return lines

def parse_temp(sensor):

   lines = read_temp_raw(sensor)
   while lines[0].strip()[-3:] != 'YES':
      sleep(0.2)
      lines = read_temp_raw(sensor)
   temp_result = lines[1].find('t=')

   if temp_result != -1:
      temp_string = lines[1].strip()[temp_result + 2:]
      # Temperature in Celcius
      temp = float(temp_string) / 1000.0
      # Temperature in Fahrenheit
      #temp = ((float(temp_string) / 1000.0) * (9.0 / 5.0)) + 32.0
      return temp
while True:
    temp1 = parse_temp(temp_sensor1)
    time.sleep(0.5)
    temp2 = parse_temp(temp_sensor2)
    time.sleep(0.5)
    f = open("tempData.txt", "w")
    f.write(str(temp1)+";"+str(temp2))
    f.close()
    time.sleep(0.5)
