import numpy as np
import thinks as think
np.random.seed(1)
import os
#afkommenter the following for at lave nyt sæt af synapser.
'''
syn0 = 2*np.random.random((21,20)) - 1
syn1 = 2*np.random.random((20,20)) - 1
syn2 = 2*np.random.random((20,10)) - 1
syn3 = 2*np.random.random((10,9)) - 1

'''
#afkommenter the following for at loade allerede trænede synapser.
synss = np.load('NN.npy')
syn0 = synss[0]
syn1 = synss[1]
print("loaded")
print ("Ready!")


X = np.array([[0.4,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],[0.4,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]])
Y = np.array([[0,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0]])


#Træn

for x in range(1000):
    think.think(X, Y, syn0, syn1, syn2, syn3, 0.08)
    
print(think.think(X,Y,syn0,syn1,syn2,syn3,0.1,False))

syns = np.array([syn0,syn1,syn2,syn3])
np.save("NN.npy",syns)

