import random

# random.seed(time.time())
class Mat:
    def __init__(self,rows,cols,data=[]):
         self.rows = rows
         self.cols = cols
         self.data = data
    
    def getRows(self):
        return self.rows
    
    def getCols(self):
        return self.cols

    def returnIndex(self,i,j) -> int:
        return i*self.cols + j
    
    def matAdd(self, mat):
        assert(self.cols == mat.cols)
        # assert(self.rows == mat.rows)
        for i in  range(self.rows):
            for j in range(self.cols):
                self.data[self.returnIndex(i,j)] += mat.data[mat.returnIndex(i,j)]
    
    def matSub(self, mat):
        assert(self.cols == mat.cols)
        # assert(self.rows == mat.rows)
        for i in  range(self.rows):
            for j in range(self.cols):
                self.data[self.returnIndex(i,j)] -= mat.data[mat.returnIndex(i,j)]
    
    def matDiv(self, mat):
        for i in  range(self.rows):
            for j in range(self.cols):
                self.data[self.returnIndex(i,j)] /= mat.data[mat.returnIndex(0,0)]
    
    def matTot(self):
        tot = 0
        for i in  range(self.rows):
            for j in range(self.cols):
                tot += self.data[self.returnIndex(i,j)] * self.data[self.returnIndex(i,j)]
        return tot 
    
    def matPrint(self):
        for i in  range(self.rows):
            for j in range(self.cols):
                print("{:.4f}".format(self.data[self.returnIndex(i,j)]), end="  ")
            print()
    
    def matDot(self,mat):
        dot = Mat(self.rows,mat.cols)
        dot.matRandom(0,0,8)
        assert(self.cols == mat.rows)
        # assert(self.rows == mat.cols)
        for i in  range(dot.rows):
            for j in range(dot.cols):
                for k in range(self.cols):
                    dot.data[dot.returnIndex(i,j)] += self.data[self.returnIndex(i,k)] * mat.data[mat.returnIndex(k,j)]
        return dot

    def matRandom(self,low,up,seed):
        random.seed(seed)
        self.data = []
        for i in  range(self.rows):
            for j in range(self.cols):
                self.data.append(round(random.uniform(low, up),2))
