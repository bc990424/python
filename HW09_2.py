class evv:
    def __init__(self,n,P):
        self.degree = n
        self.P = P

    def Getdegree(self):
        return self.degree

    def setCoefficient(self,i,v):
        self.P[i] = v

    def Getcoefficient(self,i):
        return self.P[i]

    def evaluate(self,x):
        result,temp = 0, 0

        for i in self.P:
            result += i *(x ** temp)
            temp += 1

        return result
