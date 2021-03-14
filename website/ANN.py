import numpy as np
import think
np.random.seed(1)
import os
#afkommenter the following for at lave nyt sæt af synapser.
'''
syn0 = 2*np.random.random((20,20)) - 1
syn1 = 2*np.random.random((20,20)) - 1
syn2 = 2*np.random.random((20,10)) - 1
syn3 = 2*np.random.random((10,10)) - 1
syn4 = 2*np.random.random((10,8)) -1
'''
#afkommenter the following for at loade allerede trænede synapser.
syns = np.load('NN.npy')
syn0 = syns[0]
syn1 = syns[1]
syn2 = syns[2]
syn3 = syns[3]
syn4 = syns[4]
print("loaded")
print ("Ready!")


X = np.array([[20.2,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]])
Y = np.array([1,0,0,0,0,0,0,0])


#Træn
for x in range(1000):
    think.think(X, Y, syn0, syn1, syn2, syn3, syn4, 0.08)
    
print(think.think(X,Y,syn0,syn1,syn2,syn3,syn4,0.1,False))

syns = np.array([syn0,syn1,syn2,syn3,syn4])
np.save("NN.npy",syns)

