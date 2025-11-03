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
        pass

    def __sub__(self,other):
        pass

    def __mul__(self,other):
        pass




P1 = evv(4,(3, 5, 0, 2))

print(P1.Getdegree())
print(P1.setCoefficient(1,2))
print(P1.Getcoefficient(1))
print(P1.evaluate(2))
"""
print(f"{degree(P1)}")
print(f"{coefficient(P1, 1)}")
print(f"{coefficient(P1, 2)}")
print(f"{coefficient(P1, 4)}")
print(f"{evaluate(P1, 1)}")
print(f"{evaluate(P1, 2)}")

P2 = (2, 1, -3)

print(f"{degree(P2)}")
print(f"{coefficient(P2, 2)}")
print(f"{coefficient(P2, 3)}")
print(f"{evaluate(P2, 2)}")

"""