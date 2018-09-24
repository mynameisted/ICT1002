import sys

def quit(message="Please enter valid integers."):
    print message
    sys.exit(message)

def add(x,y):
    try:
        addSum = int(x) + int(y)
        return (addSum)
    except ValueError:
        quit("Please enter valid integers as separate arguments. Example: [10,20]")

def subtraction(x,y):
    try:
        difference = int(x) - int(y)
        return (difference)
    except ValueError:
        quit("Please enter valid integers as separate arguments. Example: [10,20]")

def evenNum(x):
    try:
        countEven = 0
        for i in range(len(x)):
            if int(x[i]) % 2 == 0:
                countEven +=1
            else:
                pass
        return (countEven)
    except ValueError:
        quit("Please enter valid integers in a list. Example: [10,20,30,...]")

def maximum(x):
    try:
        x2 = []
        for i in range(len(x)):
            x2.append(int(x[i]))
        x2.sort()
        return x2[(len(x2)-1)]
    except ValueError:
        quit("Please enter valid integers in a list. Example: [10,20,30,...]")

def minimum(x):
    try:
        x2 = []
        for i in range(len(x)):
            x2.append(int(x[i]))
        x2.sort()
        return x2[0]
    except ValueError:
        quit("Please enter valid integers in a list. Example: [10,20,30,...]")

def absolute(x):
    try:
        x = int(x)
        return abs(x)
    except ValueError:
        quit("Please enter a valid integer.")

def sumTotal(x):
    try:
        addedTotal = 0
        for i in range(len(x)):
            addedTotal += int(x[i])
        return (addedTotal)
    except ValueError:
        quit("Please enter valid integers in a list. Example: [10,20,30,...]")

def clear(x):
    try:
        for i in range(len(x)):
            x[i] = 0
        return x
    except ValueError:
        quit("Please enter valid integers in a list. Example: [10,20,30,...]")


#goodValue = [-200,10,20,15,25,30,5]
#badValue = [10,20,15,25,30,"adsf"]
#print add(goodValue[1],goodValue[2])
#print subtraction(goodValue[1],goodValue[2])
#print evenNum(goodValue)
#print maximum(goodValue)
#print minimum(goodValue)
#print absolute(goodValue[0])
#print sumTotal(goodValue)
#print clear(goodValue)