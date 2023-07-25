from Mat import *
import random
import time

random.seed(time.time())

mat1 = Mat(1,3)
mat1.data = [1,1,1]
mat1.matPrint()
print()
mat2 = Mat(3,1)
mat2.data = [1,1,1]
mat2.matPrint()
print()
# mat1.matAdd(mat2)
dot = mat1.matDot(mat2)


print()
dot.matPrint()
