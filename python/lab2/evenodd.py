import sys

try:
    #Check valid number of arguments
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: evenodd.py [value1,value2,value3,...]")
    rawValues = sys.argv[1].split(',')
    i = 0
    #Validation of passed values, conversion into int
    while i < len(rawValues):
        if int(rawValues[i]) <= 0:
            print("Please enter valid integers.")
            sys.exit("Please input positive integers for the values.")
        else:
            rawValues[i]=int(rawValues[i])
        i += 1
except ValueError:
    print "Please enter valid integers."
    sys.exit("Please only enter numbers for the values.")

def evenOdd(values):
    sumEven, sumOdd, countEven, countOdd = 0,0,0,0
    for i in range(len(values)):
        if values[i] % 2 == 0:
            sumEven += values[i]
            countEven += 1
        else:
            sumOdd += values[i]
            countOdd += 1
    return (sumEven,sumOdd,countEven,countOdd)    

evenOddResults = evenOdd(rawValues)

rawValues.sort()
centeredSum = 0
#Getting the summation of centered values (ignore smallest and largest value).
for i in range(len(rawValues)):
    if i == 0 or i == len(rawValues)-1:
        pass
    else:
        centeredSum += rawValues[i]

#Consoldation of common variables assignment that will be used in the final output.
sumEven = evenOddResults[0]
sumOdd = evenOddResults[1]
bigSmallDifference = rawValues[len(rawValues)-1] - rawValues[0]
countEven = evenOddResults[2]
countOdd = evenOddResults[3]
centeredAvrg = centeredSum / (len(rawValues)-2)

#Print final output
print "The sum of all even numbers is %s, the sum of all odd numbers is %s, the difference between the biggest and smallest number is %s, the total number of even numbers is %s, the total number of odd numbers is %s, the centered average is %s." % (sumEven, sumOdd, bigSmallDifference, countEven, countOdd, centeredAvrg)
