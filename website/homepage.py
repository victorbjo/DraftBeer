from flask import Flask, render_template,request
app = Flask(__name__)
import random
import socket
import os
import numpy as np
from time import sleep
import time
import tempRead as temp
import json
from flask import jsonify
import target
import ai
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])


@app.route('/',methods = ['GET'])
@app.route('/send',methods = ['GET','POST'])
def send():
    return render_template('age.html', ip=s.getsockname()[0])

@app.route('/admin',methods = ['GET','POST'])
def admin():
    return render_template('admin.html', ip=s.getsockname()[0])

@app.route('/images',methods = ['GET','POST'])
def images():
    return render_template('images.html', ip=s.getsockname()[0])


@app.route('/info',methods = ['GET','POST'])
def info():
    return render_template('info.html', ip=s.getsockname()[0])
@app.route('/temps',methods = ['GET','POST'])
def temps():
    temps = temp.read_temp()
    return render_template('temp.html',temp0=temps[0],temp1=temps[1],temp2=temps[2], ip=s.getsockname()[0])
@app.route('/test',methods = ['GET','POST'])
def test():

    jsonData = (np.load("data10Sec.npz"))#Loads JSON data
    list ={'del':[10,12,13,14,15]} #Creates dictionary
    list.update({"temp":jsonData['temp'].tolist()}) #Converts from np array to list
    list.update({"time":jsonData['time'].tolist()}) #Same again
    del list["del"] #Deletes the first entry 

    return jsonify(list) #Returns JSON with list

@app.route('/charts',methods = ['GET','POST'])
def charts():
    return render_template('chart.html', ip=s.getsockname()[0])

@app.route('/readTarget',methods = ['GET','POST'])

def readTarget():
    list ={'target':[target.readTarget()],'status':[str(GPIO.input(14))]}
    return jsonify(list) #Returns JSON with list


@app.route('/updateTarget',methods = ['GET','POST'])
def updateTarget():
    tempTarget=str(request.args.get("target"))
    target.updateTarget(tempTarget)
    list ={'target':[str(request.args.get("target"))]}
    return jsonify(list) #Returns JSON with list


@app.route('/estimate',methods = ['GET','POST'])
def estimate():
    print("HERE!!!")
    list ={'estimate':[ai.estimate()]}
    return jsonify(list) #Returns JSON with list

if __name__ == '__main__':
    app.run(debug=False,port=80,host='0.0.0.0')    


