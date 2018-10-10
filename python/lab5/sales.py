import sys

def calculateSales(data,scale):
	return "The scaled number is: %s The sorted sales numbers are: %s The good sales numbers are: %s" % (map(lambda x:x*scale, data),sorted(data,key=lambda x:str(x)[-1]),filter(lambda x:x > reduce(lambda x,y:x+y, data) / len(data),data))

def checkFloat(value):
	value = float(value)
	if value % 1 == 0:
		value = int(value)
	return value

try:
	if len(sys.argv) != 3:
		print "Invalid number of arguments! Usage: sales.py [integer,integer,integer...] [scale]"
		sys.exit()
	else:

		valueList,scaleValue =  map(checkFloat, sys.argv[1].split(',')),checkFloat(sys.argv[2])
		print calculateSales(valueList,scaleValue)
except ValueError:
	print "Please enter valid integers!"
	sys.exit()