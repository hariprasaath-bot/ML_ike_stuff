from Mat import *
import time

def cost(w1, b1):
    l1 =  indata.matDot(w1)
    l1.matAdd(b1)
    l1.matSig()

    l1.matSub(outdata)

    return l1.matTot()/l1.getRows()

def testcost(w1, b1):
    l1 =  testdata.matDot(w1)
    l1.matAdd(b1)
    l1.matSig()
    l1.matPrint()
    l1.matSub(outdata)

    return l1.matTot()/l1.getRows()

def test():
    testcost(w1,b1)

def train(n):
    ep = 0.0001
    rate = Mat(1,1,[2.5])
    for i in range(n):
        # print(i," going with : ",end=" ")
        # w1.matPrint()

        err  = cost(w1,b1)
        print(i," cost : ", err) 
        b1.matInc(ep)

        berr = cost(w1,b1)
        b1.matDec(ep)

        w1.matInc(ep)
        derr = cost(w1,b1)
        w1.matDec(ep)

        delwnum = Mat(1,1,[derr - err])
        delwnum.matRed(ep)
        delw = delwnum.matDot(rate)

        
        delbnum = Mat(1,1,[berr - err])
        delbnum.matRed(ep)
        delb = delbnum.matDot(rate)

        w1.matDec(delw.data[delw.returnIndex(0,0)])
        b1.matDec(delb.data[delw.returnIndex(0,0)])


indata = Mat(4, 2, [0, 0, 0, 1, 1, 0, 1, 1])

outdata = Mat(4, 1, [0, 0, 0, 1])

testdata = Mat(1, 2, [1, 1])

w1 = Mat(2,1)
w1.matRandom(1,10,time.time())
b1 = Mat(4,1,[0.01, 0.01, 0.01, 0.01])

train(2000)
testdata.matPrint()
test()





