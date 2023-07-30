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
    return 2/k

#Her er funktionen der lærer og "tænker"
def think(X1, y, syn0, syn1, tmultiplier=0.025,train=True): 
    # Feed forward through layers 0, 1, and 2

       
    '''Her laver den vores synapser mellem vores neuroner.''' 
    l0 = X1

    l1 = nonlin(np.dot(l0,syn0))

    l2 = nonlin(np.dot(l1,syn1))
    #tjekker om vi træner vores netværk
    if (train==True):
        #Regner vores error ud
        l2_error = y - l2

         

       
        #printer vores gennemsnits error, så man kan se ens error når man træner
        print ("Error:" + str(np.mean(np.abs(l2_error))))
        
        #Her tjekker vi hvilken vej vores error var.
        # Vi sørger også for at den ikke retter den error for meget

        l2_delta = l2_error*nonlin(l2,deriv=True)

         

        #Tjekker hvor meget hvert lag har tilføjet til vores Error

        l1_error = l2_delta.dot(syn1.T)



        #Her prøver vi at ramme vores ideele l1 ("lag 1")        
        l1_delta = l1_error * nonlin(l1,deriv=True)
        
        syn1 += (l1.T.dot(l2_delta)*tmultiplier)

        syn0 += (l0.T.dot(l1_delta)*tmultiplier)
    #Til sidst returnere vi vores sidste lag, som er det hvor at vores svar ligger i
    return (l2)

