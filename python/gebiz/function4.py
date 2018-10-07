import csv


def initializeexceldata(awardfilepath, regconfilepath):
    # initialize master data, name lists
    masterawarddata = []  # blank list for dictionaries of award data
    mastercontdata = []  # blank list for dictionaries of contractor data

    regcontnames = []  # blank list for registered contractor names
    regcontnamesawarded = []  # blank list for awarded registered contractor names
    contnames_awarded_notreg = []  # blank list for awarded, but not registered contractor names

    dictregcontractors_awarded = []  # blank list for dictionaries of awarded registered contractors
    dictnotregcontractors_awarded = []  # blank list for dictionaries of awarded, but not registered contractors
    print "Function 4: Analyzing contractor data.."
    with open(regconfilepath, 'rU') as f:  # read contractor csv file row by row
        reader = csv.DictReader(f)  # initialize a temporary dict
        for row in reader:  # read every row in reader
            # modify the names to a standardized format
            row['company_name'] = row['company_name'].replace('.', '').replace('  ', ' ').upper()
            mastercontdata.append(row)  # insert row into master contractor data dict
            if row['company_name'] not in regcontnames:  # store unique names into regcontnames
                regcontnames.append(row['company_name'])

    with open(awardfilepath, 'rU') as f:
        reader = csv.DictReader(f)  # initialize a temporary dict
        for row in reader:  # read every row in reader
            # modify the names to a standardized format
            row['supplier_name'] = row['supplier_name'].replace('.', '').replace('  ', ' ').upper()
            masterawarddata.append(row)  # insert row of data into master award data dict
            if row['supplier_name'] in regcontnames:  # awarded supplier is a registered contractor
                dictregcontractors_awarded.append(row)
                if row['supplier_name'] not in regcontnamesawarded:
                    # store unique names into regcontnamesawarded
                    regcontnamesawarded.append(row['supplier_name'])
            elif row['supplier_name'] != 'NA':  # awarded supplier is not a registered contractor
                dictnotregcontractors_awarded.append(row)
                if row['supplier_name'] not in contnames_awarded_notreg:
                    # store unique names into contnames_awarded_notreg
                    contnames_awarded_notreg.append(row['supplier_name'])
    print "Function 4: Completed.."
    return {'masteraward': masterawarddata, 'mastercont': mastercontdata, 'regcont': regcontnames,
            'awdregcontnames': regcontnamesawarded, 'awdnotregcontnames': contnames_awarded_notreg,
            'dictregconts': dictregcontractors_awarded, 'dictnotregconts': dictnotregcontractors_awarded}
