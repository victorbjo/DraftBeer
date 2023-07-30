import numpy as np
import math
import thinks as think
import random
np.random.seed(1)
import os
'''
syn0 = 2*np.random.random((21,10)) - 1
syn1 = 2*np.random.random((10,1)) - 1
#syn01 = 2*np.random.random((21,8)) - 1
#syn11 = 2*np.random.random((8,1)) - 1
#syn02 = 2*np.random.random((21,8)) - 1
#syn12 = 2*np.random.random((8,1)) - 1

#afkommenter the following for at loade allerede trænede synapser.
'''
synss = np.load('NN.npy')
syn0 = synss[0]
syn1 = synss[1]


print("loaded")
print ("Ready!")
def cooling(x):
    y = 0.5062/pow(x,0.112)
    y = y * 24
    return round(y -8.84, 2)
def time2cool(goal,current=17):
    return 60*(cooling(goal)-cooling(current))

def tempAtTime(x):
    x += 8.84
    x = x/24
    y=65445*math.exp(-22.44*x)
    return y
def tempAtSec(x):
    x = x/60/60
    x += 8.84
    x = x/24
    y=65445*np.exp(-22.44*x)
    return y
sets = 520
goalTemp = 4
X= np.array([[1.0]*21]*sets)
Y=np.array([[1.0]]*sets)
for x in range(1000):
    secCount = 0# random.randint(0,1)
    for y in range(sets):
        for x in range(20): 
            X[y][x]=tempAtSec(secCount)
            secCount += 10
        secCount -= 190
        X[y][20] = 4
        toBinary = ((time2cool(goalTemp,X[y][19])))
        Y[y] = float(toBinary)/140.0
    for x in range(20):
        #if X[y][19]- X[y][20] > 4 and X[y][19]- X[y][20] < 10:
        think.think(X, Y, syn0, syn1, 0.000000000001)


synss = np.array([syn0,syn1])
np.save("NN.npy",synss)

X = np.array([X[1]])
print(X[0])
print(time2cool(4,X[0][19]))
print((think.think(X, Y[10], syn0, syn1, 0.01,False))*140)
print((Y[1])*140)

