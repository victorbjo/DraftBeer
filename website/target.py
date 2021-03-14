import os
def updateTarget(temp):
    f = open("targetTemp.txt", "w")
    f.write(str(temp))
def readTarget():
    f = open("targetTemp.txt", "r")
    return(f.read())
