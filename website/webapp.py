from flask import Flask, render_template,request
app = Flask(__name__)
import random
import socket
from smbus import SMBus
import serial
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.flush()
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input
GPIO.setup(10, GPIO.OUT)




@app.route('/',methods = ['GET'])
@app.route('/send',methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        return render_template('age.html',age=3, ip=s.getsockname()[0])
    return render_template('index.html')
@app.route('/cakes',methods = ['GET'])
def cakes():
    y = 0
    
    
    import numpy as np
    f = open("test.txt", "r")
    fread = f.read()
    
    tempsCount=0
    temps = ["","",""]
    for x in range(len(fread)):
        if fread[x] != ";" and fread[x].isnumeric():
            temps[tempsCount] = temps[tempsCount] + str(fread[x])
        else:
            tempsCount =+ 1
    y = temps[0]
    return render_template('cakes.html', cake = y)
@app.route('/ledOn',methods = ['GET'])
def ledOn():
    bus.write_byte(addr, 0x1)
    return render_template('index.html')
@app.route('/ledOff',methods = ['GET'])
def ledOff():
    bus.write_byte(addr, 0x0)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=False,port=80,host='0.0.0.0')
    
