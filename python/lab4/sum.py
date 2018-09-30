import sys

try:
    #Check valid number of arguments
    if len(sys.argv) != 2:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: sumCalculator.py [integer]")
    elif int(sys.argv[1]) < 0:
    	print "Please enter positive integers."
    	sys.exit("Please only enter positive integers.")
    else:
    	passedValue = int(sys.argv[1])
except ValueError:
    print "Please enter valid integers."
    sys.exit("Please only enter numbers for the values.")


def sum_recursive(n):
    if n== 0:
        return 0
    else:
        return n + sum_recursive(n-1)

def sum_iterative(n):
	baseSum = 0
	for i in range(1,n+1):
		baseSum += i
	return baseSum

print "The SUM value calculated by recursive is %d and by iterative is %d." % (sum_recursive(passedValue), sum_iterative(passedValue))