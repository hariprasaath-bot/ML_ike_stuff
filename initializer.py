from Mat import *
import time

# Trying to form framework
class neuronsetup:
    
    def __init__(self,n,a,l):
        self.neurons = n
        self.activation = a + 1
        self.layer = l
    
    def formWeights(self):
         weights = Mat(self.neurons,self.activation)
         weights.matRandom(1,10,time.time())
         return weights
    
    def formActivationWeights(self):
        layers = []
        for i in range(self.layer):
            if( i == self.layer - 1):
                weights = Mat(self.activation,1)
            else:
                weights = Mat(self.activation,self.layer)
            weights.matRandom(1,10,time.time())
            layers.append(weights)
        return layers
    
    def formBiases(self):
        biases = []
        for i in range(self.layer):
            b = Mat(1,self.activation)
            b.matRandom(0.01,0.01,0.01)
            biases.append(b)
        return biases
    


