import sys

def double(x):
	return 2*x
def square(x):
	return x*x
def cube(x,square=square):
	return square(x)*x
def doTwice(doFunc,x):
	return doFunc(doFunc(x))

try:
	if len(sys.argv) != 3:
		print "Invalid number of arguments! Usage: doTwice.py [integer] [requestCode]"
		sys.exit()
	else:
		passedValue,requestType = map(int,[sys.argv[1],sys.argv[2]])
		requestMapping = {1:double,2:square,3:cube}
		print doTwice(requestMapping[requestType],passedValue)
except ValueError:
	print "Please enter valid integers!"
	sys.exit()
except (IndexError,KeyError):
	print "It cannot be supported!"
	sys.exit("Valid inputs: [1: Double, 2: Square, 3: Cube]")
