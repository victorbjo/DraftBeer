import os
import datetime
from time import sleep
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor0 = '/sys/bus/w1/devices/28-0114485317aa/w1_slave'
temp_sensor1 = '/sys/bus/w1/devices/28-0114477905aa/w1_slave'  
temp_sensor2 ='/sys/bus/w1/devices/28-0114487279aa/w1_slave' 
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

def read_temp():
   parsedTemp = parse_temp(temp_sensor0)
   file = open("tempData.txt", "r")
   f = file.read()
   file.close()
   return(parsedTemp,f[:f.find(";")],f[f.find(";")+1:])


def get_temp():
   try:
      parsedTemp = parse_temp(temp_sensor0)
      try:
         f = open("tempDataMain.txt","w")
         f.write(str(parsedTemp))
         f.close()
      except:
         f = open("crashTemp.txt", "a")
         now = datetime.datetime.now()
         f.write("Could not open or save file @ " + str(now.hour)+":"+str(now.minute)+"\n")
         f.write(str(e))
         f.write("\n")
         f.close()

   except:
      f = open("crashTemp.txt", "a")
      now = datetime.datetime.now()
      f.write("Could not parse Temp @ " + str(now.hour)+":"+str(now.minute)+"\n")
      f.write(str(e))
      f.write("\n")
      f.close()
      parsedTemp=0
   return parsedTemp
