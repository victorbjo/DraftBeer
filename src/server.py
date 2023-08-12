from flask import Flask, render_template,request
app = Flask(__name__)
import socket
import numpy as np
from flask import jsonify

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])


@app.route('/',methods = ['GET'])
def main():
    return render_template('age.html', ip=s.getsockname()[0])

@app.route('/send',methods = ['GET','POST'])
def send():
    return render_template('send.html', ip=s.getsockname()[0])
@app.route('/admin',methods = ['GET','POST'])
def admin():
    return render_template('admin.html', ip=s.getsockname()[0])

@app.route('/images',methods = ['GET','POST'])
def images():
    return render_template('images.html', ip=s.getsockname()[0])


@app.route('/info',methods = ['GET','POST'])
def info():
    return render_template('info.html', ip=s.getsockname()[0])

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



@app.route('/estimate',methods = ['GET','POST'])
def estimate():
    print("HERE!!!")
    list ={'estimate':[ai.estimate()]}
    return jsonify(list) #Returns JSON with list

if __name__ == '__main__':
    app.run(debug=False,port=80,host='0.0.0.0')    


