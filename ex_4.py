import random

def getLotto():
    myList = []
    temp_lotto = random.randint(1,45)
    for i in range(6):
        while temp_lotto in myList:
            temp_lotto = random.randint(1, 45)

        myList.append(temp_lotto)

    myList.sort()
    return myList

print(getLotto())

