import csv
#======================POINTS TO NOTE======================
# masterGebiz will be a list of dictionaries, where each dictionary is every row in the gebiz CSV file.
# masterCon will be a list of dictionairies, where each dictionary is every row in the registered contractor CSV file.
# regConNames will be a list of unique company names found in the registered contractors. Essentially, a list of registered contractors.
# regConNamesAwarded is a list of all awarded registered company names 
# unregConNamesAwarded is a list of all awarded unregistered company names 
# gebizRegisteredAwards is a list of all awarded details for registered companies.
# gebizUnregisteredAwards is a list of all awarded details for unregistered companies.

def sortRegistered(gebizpath, regconpath):
    #Create empty lists
    masterGebiz = []
    masterCon = []
    regConNames = []
    regConNamesAwarded = []
    unregConNamesAwarded = []
    gebizRegisteredAwards = []
    gebizUnregisteredAwards = []
    #Open Registered Contractors CSV file
    with open(regconpath) as oFile:
        reader = csv.DictReader(oFile)
        #Loop through every row in the file
        for row in reader:
            #Replace 'company_name' data with normalised data (Uppercase, remove fullstops and double spaces)
            row['company_name'] = row['company_name'].replace(".","").replace("  "," ").upper();
            #Append the company name into regConNames (This list only holds the contractor names)
            if row['company_name'] not in regConNames:
                regConNames.append(row['company_name'])
            #Append the full row of data into masterCon
            masterCon.append(row)

    with open(gebizpath) as gFile:
        #Open geBiz CSV file
        reader = csv.DictReader(gFile)
        #Loop through every row in the file
        for row in reader:
            #Replace 'supplier_name' data with normalised data (Uppercase, remove fullstops and double spaces)
            row['supplier_name'] = row['supplier_name'].replace(".","").replace("  "," ").upper();
            #Check if current row's supplier_name is found in the list of registered contractors
            if row['supplier_name'] in regConNames:
                #Append the row into a consolidated list    
                gebizRegisteredAwards.append(row)
                #Ensure no duplicates in the list of names
                if row['supplier_name'] not in regConNamesAwarded:
                    regConNamesAwarded.append(row['supplier_name'])
            #Else if current row's supplier name is not found in the list of registered contractors (meaning unregistered)
            else:
                if row['supplier_name'] != 'NA':
                    #Append the row into a consolidated list
                    gebizUnregisteredAwards.append(row)
                    #Ensure no duplicates in the list of names
                    if row['supplier_name'] not in unregConNamesAwarded:
                        unregConNamesAwarded.append(row['supplier_name'])
            #Append the full row of data into masterGebiz
            masterGebiz.append(row)
    return {'masterGebiz':masterGebiz,'masterCon':masterCon,'regConNames':regConNames,'regConNamesAwarded':regConNamesAwarded,'unregConNamesAwarded':unregConNamesAwarded,'gebizRegisteredAwards':gebizRegisteredAwards,'gebizUnregisteredAwards':gebizUnregisteredAwards}
#data = sortRegistered("government-procurement/government-procurement-via-gebiz.csv","listing-of-registered-contractors/listing-of-registered-contractors.csv")
