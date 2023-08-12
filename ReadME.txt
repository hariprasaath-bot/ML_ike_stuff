This is basic ML project

Gurunathar : https://www.youtube.com/playlist?list=PLpM-Dvs8t0VZPZKggcql-MmjaBdZKeDMw
ML framework --MATRICES
DATABASES

basic ml for : Gates

    dataset : 
                x1 x2 y
                0  0  0
                0  1  1
                1  0  1
                1  1  1
    weight :
                w1 w2
    bias :
                b
    
    MAT OP :
            x1 W1
    
    Process :
            create two weight for two input
            put in cost function of 
                            err += y - sigmoid(x1*w1 + x2*w2 + b)
                            ret err/dataset_count
            Train count ::
                Find the derivative =>
                            delw1 = cost(w1 + e, w2, b) - cost(w1, w2, b)  / e
                            delw2 = cost(w1, w2 + e, b) - cost(w1, w2, b)  / e
                            delb  = cost(w1, w2, b + e) - cost(w1, w2, b)  / e
                            w1 -= delw1
                            w2 -= delw2
                            b -= delb
