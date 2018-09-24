import sys
import collections


inputStringRaw = ""
try:
    #Check valid number of arguments
    if len(sys.argv) <= 1:
        print "Your input is invalid!"
        sys.exit("Invalid number of arguments.\nUsage: countchars.py [word1,word2,word3,...]")
    else:
    	for i in range(len(sys.argv)):
    		if i == 0:
    			pass
    		else:
	    		inputStringRaw = inputStringRaw + str(sys.argv[i])
		inputString = inputStringRaw.replace(',', '')    		
except ValueError:
    print "Your input is invalid!"
    sys.exit("Your input is invalid.")



def variousCount(value):
	inputStringDict= collections.Counter(value)
	return sorted(inputStringDict.items(), reverse=True)

finalStr = []
counted = variousCount(inputString)
for i in range(len(counted)):
	finalStr.append(str(counted[i][0])+":"+str(counted[i][1]))
print ", ".join(finalStr)


#for i in range(len(top5)):
#    top5Str.append(str(top5[i][0])+":"+str(top5[i][1]))
#print ",".join(top5Str)
