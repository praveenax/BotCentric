import numpy as np

def initSyn(inp,out):
    return 2*np.random.random((inp,out)) - 1
    

def nonlin(x,deriv=False):
    if(deriv==True):
        return (x*(1-x))
    
    return 1/(1+np.exp(-x))

def trainLayer(in_layer,out_layer):
    return nonlin(np.dot(in_layer,out_layer)) 
    

X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])

Y = np.array([[0],[1],[1],[0]])

np.random.seed(1)

syn0 = initSyn(3,5)
syn1 = initSyn(5,3)
syn2 = initSyn(3,1)

for j in xrange(60000):
    
    l0 = X
    l1 = trainLayer(l0,syn0)
    l2 = trainLayer(l1,syn1)
    l3 = trainLayer(l2,syn2)
    
    l3_error = Y - l3
    
    if(j%10000) == 0:
        print "ERROR:  " + str(np.mean(np.abs(l3_error)))
        
    l3_delta = l3_error * nonlin(l3,deriv=True)

    l2_error = l3_delta.dot(syn2.T)
    
    l2_delta = l2_error * nonlin(l2,deriv=True)
    
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * nonlin(l1,deriv=True)
    
    
    
    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    
print "OUTPUT"
print l3
#print syn0
#print syn1
#print l2[0][0]
#print np.abs(l2[0][0])
print np.rint(l3).astype(int)


#print syn1
#print syn0
    
    