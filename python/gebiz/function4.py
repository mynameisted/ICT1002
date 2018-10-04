import csv
'''(get master contract data AND registered contract data first), get master award data'''


def get_contractor_data(regconfilepath):
    mastercontdata = []  # blank list to store dicts of master contractor data
    with open('regconfilepath','rU') as f:  # read one line at a time from registered-contractors.csv
        reader = csv.DictReader(f)  # dictionary initialized
        for row in reader:  # for every row in reader
            row['company_name'] = row['company_name'].replace('.', '').replace('  ', ' ').upper()
            mastercontdata.append(row)
    return mastercontdata


def get_award_data(awardfilepath):
    with open('awardfilepath', 'rU') as f:  # read one line at a time from awarded-contractors.csv
        reader = csv.DictReader(f)  # dictionary initialized
        masterawardData = [] # blank list to store master award data
        i = 1
        for row in reader:  # for every row in reader
            row['supplier_name'] = row['supplier_name'].replace('.','').replace('  ',' ').upper()
            if row['supplier_name'] in regcontdata:
                masterawardData.append(row)
    return masterawardData


def splitconts(masterawardData, mastercontdata):
        listAwdRegConts = []  # list for awarded registered contractors
        listNotRegConts = []  # list for non registered contractors
        for i in range(len(mastercontdata)):  # append listAwdRegConts with contractor names found in both lists
            if mastercontdata[i]['company_name'] in masterawardData:
                if mastercontdata[i]['company_name'] not in listAwdRegConts:
                    listAwdRegConts.append(mastercontdata[i]['company_name'])
                else: # company name already exists in listAwdRegConts
                    continue
            else:  # append listNotRegConts if contractor name not found in both lists
                listNotRegConts.append(mastercontdata[i]['company_name'])
        return listAwdRegConts, listNotRegConts


def listawardedregisteredcontractors(listAwdRegConts):
        if len(listAwdRegConts) == 0:  # no awarded registered contractors
            print "There are no awarded registered contractors."
        else:  # print out all awarded registered contractors in order
            print "Names of awarded registered contractors:"
            for i in range(len(listAwdRegConts)):
                print "%d." % (i+1) + listAwdRegConts[i]
        print "No. of awarded registered contractors: %d" % len(listAwdRegConts)