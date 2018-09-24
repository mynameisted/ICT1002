import sys
import MyMath

def checkClear(x):
    if MyMath.minimum(x) < 5:
        x = MyMath.clear(x)
    return (x)

def calculate(x):
    difference = MyMath.subtraction(MyMath.maximum(x),MyMath.minimum(x))
    addition = MyMath.add(MyMath.maximum(x),MyMath.minimum(x))
    summation = MyMath.sumTotal(x)
    numEven = MyMath.evenNum(x)
    finalList = checkClear(x)
    return ("The difference is:%d The summation is:%d The summation of all input is:%d The number of even numbers is:%d The values in the list are: %s" % (difference,addition,summation,numEven,finalList))



try:
    #Check valid number of arguments
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: calculator.py [value1,value2,value3,...]")
    passedValues = sys.argv[1].split(',')
    #Validation of passed values, conversion into int
    for i in range(len(passedValues)):
        passedValues[i] = int(passedValues[i])
    print calculate(passedValues)
except ValueError:
    print "Please enter valid integers."
    sys.exit("Please only enter numbers for the values.")
