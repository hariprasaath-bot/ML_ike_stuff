from Mat import *
import time

input = Mat(6, 1, [1,2,3,4,5,6])
output = Mat(6, 1, [3, 6, 9, 12, 15, 18])

# put in cost function of 
#                             err += y - sigmoid(x1*w1 + x2*w2 + b)
#                             ret err/dataset_count

def cost(w_mat,b_mat):

    err =  input.matDot(w_mat)
    err.matAdd(b_mat)
    err.matSub(output)
    # print("error")
    # err.matPrint()
    return err.matTot() / err.getRows()

def main():
    w_mat = Mat(1,1)
    w_mat.matRandom(1,10,time.time())
    b_mat = Mat(input.getCols(),1,[0.01, 0.001, 0.01, 0.01, 0.01, 0.01])
    ep = Mat(1,1,[0.001])
    rate = Mat(1,1,[0.01])
    print("ïnitial ",end=" ")
    w_mat.matPrint()

    for i in range(200):
        print(i," going with : ",end=" ")
        w_mat.matPrint()

        err  = cost(w_mat,b_mat)
        b_mat.matAdd(ep)

        berr = cost(w_mat,b_mat)
        b_mat.matSub(ep)

        w_mat.matAdd(ep)
        derr = cost(w_mat,b_mat)
        w_mat.matSub(ep)

        delwnum = Mat(1,1,[derr - err])
        delwnum.matDiv(ep)
        delw = delwnum.matDot(rate)


        delbnum = Mat(1,1,[berr - err])
        delbnum.matDiv(ep)
        delb = delbnum.matDot(rate)

        w_mat.matSub(delw)
        b_mat.matSub(delb)


    w_mat.matPrint()

main()

        




