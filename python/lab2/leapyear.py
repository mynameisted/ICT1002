import sys
try:
    #Check valid number of arguments
    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: leapyear.py [start year] [end year]")
    elif int(sys.argv[1]) <= 0 or int(sys.argv[2]) <=0:
        print "Your input is invalid!"
        sys.exit("Please only input integer values for the start year and end year")
    else:
        startYear = int(sys.argv[1])
        endYear = int(sys.argv[2])
except ValueError:
    print "Your input is invalid!"
    sys.exit("Please only enter numbers for the values.")

tempYear = float(startYear)
leapYears = []

def leapCondition(year):
	"Checks for leap year conditions and appends to list of leap years if conditions are met"
	if (year/4).is_integer():
		if (year/100).is_integer() and ((year/400).is_integer() == False):
			pass
		else:
			leapYears.append(int(year))

#Runs each year though the leap year validator
for i in range(endYear - startYear + 1):
	leapCondition(tempYear)
	tempYear +=1

#Joining the finalized leap year list into a string for output
strLeapYears = ", ".join(str(x) for x in leapYears)
#If there are no leap years, then print [null]
if len(strLeapYears) == 0:
	strLeapYears = '[null]'
#Printing final output
print "The number of Leap Years is %s, the Leap Years are %s" % (len(leapYears), strLeapYears)

