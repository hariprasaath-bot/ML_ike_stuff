from Mat import *
from initializer import *
import random
import time

# random.seed(time.time())

# mat1 = Mat(1,3)
# mat1.data = [1,1,1]
# mat1.matPrint()
# print()
# mat2 = Mat(3,1)
# mat2.data = [1,1,1]
# mat2.matPrint()
# print()
# # mat1.matAdd(mat2)
# dot = mat1.matDot(mat2)


# print()
# dot.matPrint()

obj = neuronsetup(2,2,3)

w = obj.formWeights()
b = obj.formBiases()
a = obj.formActivationWeights()
w.matPrint()
print("Weight===============")
for l in a:
    l.matPrint()
print("activations===============")
for l in b:
    l.matPrint()