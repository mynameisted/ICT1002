import sys

try:
    #Check valid number of arguments
    if len(sys.argv) != 2:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: digit.py [integer]")
    elif int(sys.argv[1]) < 0:
        print "Please enter positive integers."
        sys.exit("Please only enter positive integers.")
    else:
        passedValue = int(sys.argv[1])
except ValueError:
    print "Please enter valid integers."
    sys.exit("Please only enter numbers for the values.")


def digit(n):
    if n == 0:
        return 0
    else:
        return 1 + digit(n / 10)

#print sum_recursive(passedValue)
def digit_iterative(n):
    base = 0
    while n > 0:
        n = n/10
        base +=1
    return base
print "The number of digit(s) calculated by recursive is %d and by iterative is %d." % (digit(passedValue), digit_iterative(passedValue))