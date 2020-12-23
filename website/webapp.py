from flask import Flask, render_template,request
app = Flask(__name__)
import random
import socket
import fileParser as file
import parser
import SerialHandler
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])


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
@app.route('/test',methods = ['GET'])
def test():
    SerialHandler.getTemps()
    temps = parser.readFile() #Parsing what is essentially the DB
    return render_template('info.html', beerTemp=temps[8], waterTemp=temps[9], airTemp=temps[10],
                           mt=temps[0],t1=temps[2],t2=temps[3],t3=temps[4],t4=temps[5],t5=temps[6],
                           t6=temps[7],t7=1,t8=1,actualTemp=temps[1]) #Renders a html template with data

    '''return render_template('info.html', beerTemp=temps[0], waterTemp=temps[1], airTemp=temps[2],
                           mt=temps[3],t1=temps[4],t2=temps[5],t3=temps[6],t4=temps[7],t5=temps[8],
                           t6=temps[9],t7=temps[10],t8=temps[11],actualTemp=temps[12]) #Renders a html template with data
'''
@app.route('/demo',methods = ['GET'])
def demo():
    print("demo")
    f = open("test.txt", "a")
    f.write("Opened\n")
    coolerGet = str(request.args.get("coolerStates"))
    tempGet = str(request.args.get("temp"))
    if (tempGet == None or tempGet ==""):
        tempGet = "00"
    #print("Coolerget" + str(coolerGet))
    #print("TempGet" + str(tempGet))
    SerialHandler.changeUnitStatus(coolerGet, tempGet)
    return render_template('cakes.html', cake = coolerGet)
if __name__ == '__main__':
    app.run(debug=False,port=80,host='0.0.0.0')    
