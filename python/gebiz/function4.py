import csv

#======================POINTS TO NOTE======================
# masterGebiz will be a list of dictionaries, where each dictionary is every row in the gebiz CSV file.
# masterCon will be a list of dictionairies, where each dictionary is every row in the registered contractor CSV file.
# regCon will be a list of unique company names found in the registered contractors. Essentially, a list of registered contractors.
# You'll have to ensure that the regCon list is unique (no duplicated company names)
#When you run this file, nothing will be shown in the console/terminal. You'll have to print certain values if necessary for troubleshooting/development

def sortRegistered(gebizpath, regconpath):
    #Create empty lists
    masterGebiz = []
    masterCon = []
    regCon = []
    #Open Registered Contractors CSV file
    with open(regconpath) as oFile:
        reader = csv.DictReader(oFile)
        #Loop through every row in the file
        for row in reader:
            #Replace 'company_name' data with normalised data (Uppercase, remove fullstops and double spaces)
            row['company_name'] = row['company_name'].replace(".","").replace("  "," ").upper();
            #Append the company name into regCon (This list only holds the contractor names)
            regCon.append(row['company_name'])
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
            if row['supplier_name'] in regCon:
                #Put whatever code you want to execute
                #print "Supplier is a registered contractor"
                pass
            #Else if current row's supplier name is not found in the list of registered contractors (meaning unregistered)
            else:
                #Put whatever code you want to execute
                #print "Supplier is not a registered contractor"
                pass
            #Append the full row of data into masterGebiz
            masterGebiz.append(row)


#Call the function to execute with selected file paths (Will vary depending on your folder structure)
sortRegistered("government-procurement/government-procurement-via-gebiz.csv","listing-of-registered-contractors/listing-of-registered-contractors.csv")
