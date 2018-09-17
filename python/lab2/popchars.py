import sys
import collections

try:
    #Check valid number of arguments
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: popchars.py [inputvalue]")
    else:
        inputString = str(sys.argv[1])

except ValueError:
    print "Your input is invalid!"
    sys.exit("Please only enter numbers for the values.")


inputString = inputString.lower()
inputStringList = sorted(list(inputString))
inputStringDict= collections.Counter(inputStringList)
top5 = list(inputStringDict.most_common(5))
top5Str = []
for i in range(len(top5)):
    top5Str.append(str(top5[i][0])+":"+str(top5[i][1]))

print ",".join(top5Str)
