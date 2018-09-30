import generalFunctions

#Dictionary variable creation
agencyTotalSpending = {}

#Define the function, set default argument to 'asc' if not given
def sortTotalAward(sortOrder="asc"):
	#Loop through each agency in the full list of agencies
	for agency in generalFunctions.gebizKeys:
		#Reset variable to 0
		totalSpending = 0
		#Looping through every record for current agency
		for row in range(len(generalFunctions.gebizData[agency])):
			#Add each awarded amount to get the cumulative total spending for the agency
			totalSpending += float(generalFunctions.gebizData[agency][row]['awarded_amt'])
		#Format total spending to 2 decimal point precision and append into dictionary
		agencyTotalSpending[agency] = float(format(totalSpending, '.2f'))
	#Do a 1 time sort of the dictionary into a list of tuples.
	sortedSpending = sorted(agencyTotalSpending.items(), key=lambda k:k[1])
	if sortOrder == 'asc':
		#Do nothing as list is already asc order by default
		pass
	elif sortOrder == 'desc':
		#Reverse the list of tuples
		sortedSpending.reverse()
	else:
		generalFunctions.quit("Invalid argument passed for Function 3.")
	generalFunctions.sortedSpending = sortedSpending
	return (sortedSpending)
