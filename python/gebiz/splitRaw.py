import csv, os
from itertools import groupby


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

dictList = []
dAgency = []
def splitFile(selectedFilePath):
    with open(selectedFilePath) as gFile:
        reader = csv.DictReader(gFile)
        for row in reader:
            dictList.append(row)

    dictList.sort(key=lambda x:x['agency'])

    directory = './GovernmentAgencies/'
    createFolder(directory)

    print"Extracting data, please wait..."
    for k, v in groupby(dictList, key=lambda x: x['agency']):
        dAgency.append(k)
        strPath = directory + k + '.txt'
        oFile = open(strPath, 'w')
        #oFile.write("%s\n" % list(v))

        newList = list(v)
        keys = newList[0].keys()
        dict_writer = csv.DictWriter(oFile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(newList)
    print"Data extracted!"
    gFile.close()
    oFile.close()
    return {'dir':directory,'agencies':dAgency, 'filetype':".txt"}
