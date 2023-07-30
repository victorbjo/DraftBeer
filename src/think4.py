'''
    Skrevet af Hjalte og Victor
'''


import numpy as np
#Vores nonlinear funktion. Her kører vi dataen igennem en sigmoid funktion
def nonlin(x,deriv=False):

    if(deriv==True):
        return x*(1-x)
    for y in range(int(x.size/x[0].size)):
        for x1 in range(x[0].size):
            if (x[y][x1] > 19):
                x[y][x1]= 19
            elif (x[y][x1]<-6.5):
                x[y][x1]=-6.5
    
    k = 1+np.exp(-x)
    return 1/k

#Her er funktionen der lærer og "tænker"
def think(X1, y, syn0, syn1, syn2, syn3, syn4, tmultiplier=0.025,train=True): 
    # Feed forward through layers 0, 1, and 2

       
    '''Her laver den vores synapser mellem vores neuroner.''' 
    l0 = X1

    l1 = nonlin(np.dot(l0,syn0))

    l2 = nonlin(np.dot(l1,syn1))
    l3 = nonlin((np.dot(l2,syn2)))
    l4 = nonlin((np.dot(l3,syn3)))

    #tjekker om vi træner vores netværk
    if (train==True):
        #Regner vores error ud
        l4_error = y - l4

         

       
        #printer vores gennemsnits error, så man kan se ens error når man træner
        print ("Error:" + str(np.mean(np.abs(l4_error))))
        
        #Her tjekker vi hvilken vej vores error var.
        # Vi sørger også for at den ikke retter den error for meget

        l4_delta = l4_error*nonlin(l4,deriv=True)

         

        #Tjekker hvor meget hvert lag har tilføjet til vores Error
        
        l3_error = l4_delta.dot(syn3.T)
        l3_delta = l3_error * nonlin(l3,deriv=True)
        l2_error = l3_delta.dot(syn2.T)
        l2_delta = l2_error * nonlin(l2,deriv=True)
        l1_error = l2_delta.dot(syn1.T)



        #Her prøver vi at ramme vores ideele l1 ("lag 1")        
        l1_delta = l1_error * nonlin(l1,deriv=True)
        
        syn3 += (l3.T.dot(l4_delta)*tmultiplier)
        syn2 += (l2.T.dot(l3_delta)*tmultiplier)
        syn1 += (l1.T.dot(l2_delta)*tmultiplier)

        syn0 += (l0.T.dot(l1_delta)*tmultiplier)
    #Til sidst returnere vi vores sidste lag, som er det hvor at vores svar ligger i
    return (l5)

