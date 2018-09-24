import csv

#agencyList = ['Accounting And Corporate Regulatory Authority', 'Agency for Science, Technology and Research', 'Agri-food and Veterinary Authority', 'Assumption Pathway School', "Attorney-General's Chambers", "Auditor-General's Office", 'Building and Construction Authority', 'Casino Regulatory Authority', 'Central Provident Fund Board', 'Centre for Public Project Management', 'Civil Aviation Authority of Singapore', 'Civil Service College', 'Competition Commission of Singapore', 'Council for Estate Agencies', 'Council for Private Education', 'Defence Science and Technology Agency', 'Duke-NUS Medical School', 'Economic Development Board', 'Energy Market Authority of Singapore', 'Government Technology Agency (GovTech)', 'Health Promotion Board', 'Health Sciences Authority', 'Housing and Development Board', 'ISEAS - Yusof Ishak Institute', 'Info-communications Media Development Authority', 'Inland Revenue Authority of Singapore', 'Institute of Technical Education', 'Intellectual Property Office of Singapore', 'International Enterprise Singapore', 'Istana', 'Judiciary-State Courts', 'Judiciary-Supreme Court', 'Jurong Town Corporation', 'Land Transport Authority', 'Majlis Ugama Islam Singapura', 'Maritime and Port Authority of Singapore', "Methodist Girls' School (Secondary)", 'Ministry of Communications and Information', 'Ministry of Culture, Community and Youth - Ministry Headquarter', 'Ministry of Culture, Community and Youth - National Youth Council', 'Ministry of Defence', 'Ministry of Defence 5', 'Ministry of Education', 'Ministry of Education - Schools', 'Ministry of Finance - Singapore Customs', 'Ministry of Finance - Vital', "Ministry of Finance-Accountant-General's Department", 'Ministry of Finance-Ministry Headquarter', 'Ministry of Foreign Affairs', 'Ministry of Health-Ministry Headquarter', 'Ministry of Home Affairs-Ministry Headquarter', 'Ministry of Law-Ministry Headquarter', 'Ministry of Manpower - Foreign Manpower Management Division', 'Ministry of Manpower - Occupational Safety & Health Division', 'Ministry of Manpower - Work Pass Division', 'Ministry of Manpower-Information Systems & Technology Department', 'Ministry of Manpower-Labour Relations Department', 'Ministry of Manpower-Ministry Headquarter', 'Ministry of National Development-Ministry Headquarter', 'Ministry of Social and Family Development - Early Childhood Development Agency', 'Ministry of Social and Family Development - Family Development Group', 'Ministry of Social and Family Development - Ministry Headquarter', 'Ministry of Social and Family Development - Rehabilitation and Protection', 'Ministry of Trade & Industry-Department of Statistics', 'Ministry of Trade & Industry-Ministry Headquarter', 'Ministry of Transport - Ministry Headquarter', 'Ministry of the Environment and Water Resources', 'Monetary Authority of Singapore', 'NUS HIGH SCHOOL OF MATHEMATICS AND SCIENCE', 'Nanyang Polytechnic', 'Nanyang Technological University', 'National Arts Council', 'National Council of Social Service', 'National Environment Agency', 'National Heritage Board', 'National Institute of Education', 'National Library Board', 'National Parks Board', 'National University of Singapore', 'Ngee Ann Polytechnic', 'Northlight School', 'Parliament', "People's Association", "Prime Minister's Office - National Research Foundation", "Prime Minister's Office - National Security Co-ordination Secretariat", "Prime Minister's Office - Smart Nation and Digital Government Office", "Prime Minister's Office - Strategy Group", "Prime Minister's Office-Corrupt Practices Investigation Bureau", "Prime Minister's Office-Elections Department", "Prime Minister's Office-Ministry Headquarter", "Prime Minister's Office-Public Service Division", 'Productivity Fund Administration Board', 'Public Transport Council', 'Public Utilities Board', "Raffles Girls' School (Secondary)", 'Republic Polytechnic', 'SPRING Singapore', 'School of Science and Technology, Singapore', 'Science Centre Board', 'Sentosa Development Corporation', "Singapore Chinese Girls' School", 'Singapore Corporation of Rehabilitative Enterprises', 'Singapore Examinations and Assessment Board', 'Singapore Labour Foundation', 'Singapore Land Authority', 'Singapore Polytechnic', 'Singapore Sports Council', 'Singapore Tourism Board', 'SkillsFuture Singapore', 'Temasek Polytechnic', 'Tote Board', 'Urban Redevelopment Authority', 'Workforce Singapore']
#fileDir = "./GovernmentAgencies/"
#fileType = ".txt"

#Dictionary variable creation
agencyTotalSpending = {}
#{'dir':directory,'agencies':dAgency, 'filetype':".txt"}
def sortTotalAward(directory,agencies,filetype,sortOrder="asc"):
	#Loop through each agency
	for agency in agencies:
		#Reset variable to 0 for each agency
		totalSpending = 0.00
		#Set the path of the file and opens the file
		with open(directory+agency+filetype) as csvfile:
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
	if sortOrder == 'asc':
		pass
	#Reverses the list to be in descending order
	elif sortOrder == 'desc':
		sortAgency.reverse()
	return {'totalSpending':sortAgency,'sortOrder':sortOrder}

#print sortTotalAward(fileDir,agencyList,fileType,'desc')
