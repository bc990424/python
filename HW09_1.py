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

    def __add__(self,other):
        result = {}
        for i,n in other.items():
            print(i,n)
            if i in self.P.keys():
                result[i] += n
            else :
                result[i] = n
    def __sub__(self,other):
        result = {}
        for i,n in other.items():
            print(i,n)
            if i in self.P.keys():
                result[i] -= n
            else :
                result[i] = n * -1

    def __mul__(self,c):
        result = {}
        for i,n in self.P.items():
            result[i] = n * c

        return result




P1 = evv(4,{0 : 3, 1 : 5, 2 : 0, 3 : 2})

print(P1.Getdegree())
P1.setCoefficient(1,2)
print(P1.Getcoefficient(1))
print(P1.evaluate(2))
P1.__add__({5:2,3:4})

P2 = evv(4,{0 : 1, 1 : 3, 2 : 2, 3 : 1})
