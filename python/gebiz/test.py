import csv
import splitRaw

#Calls the splitfile function 2 by Najib and stores the returned values {'dir':directory,'agencies':dAgency, 'filetype':".txt"}.
agencyList = splitRaw.splitFile('government-procurement-via-gebiz.csv')

#Dictionary variable creation
agencyTotalSpending = {}

#Loop through each agency
for agency in agencyList['agencies']:
	#Reset variable to 0 for each agency
	totalSpending = 0.00
	#Set the path of the file and opens the file
	with open(agencyList['dir']+agency+agencyList['filetype']) as csvfile:
		#Stores the values into a dictionary
		reader = csv.DictReader(csvfile)
		#For each record in the file, add up the awarded amount to get the total amount
		for row in reader:
				amount = float(row['awarded_amt'])
				totalSpending += amount
		#Format the total amount floating point precision to 2 and add to the dictionary
		agencyTotalSpending[agency] = float(format(totalSpending, '.2f'))
		#Close the file after we are done
		csvfile.close()

#Do a 1 time ascending sort based on the dictionary's value(total spending).
sortAgency = sorted(agencyTotalSpending.items(), key=lambda k: k[1])

#Function definition - If no parameter is passed, defaults to ascending
def printSpending(direction='asc'):
	#Do nothing as the list is already in ascending order
	if direction == 'asc':
		pass
	#Reverses the list to be in descending order
	elif direction == 'desc':
		sortAgency.reverse()
#	for i in range(len(sortAgency)):
#		print sortAgency[i]
	return (sortAgency)
	
print printSpending('desc')