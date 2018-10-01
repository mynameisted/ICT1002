import csv
import os
from itertools import groupby
import generalFunctions

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)

def sortGovAgency(path):
    dictList = []
    dAgency = []
    fType = ".txt"
    with open(path) as gFile:
        reader = csv.DictReader(gFile)
        for row in reader:
            dictList.append(row)
    dictList.sort(key=lambda x: x['agency'])

    newFolder = './GovernmentAgencies/'
    createFolder(newFolder)

    print"Extracting data, please wait..."
    for k, v in groupby(dictList, key=lambda x: x['agency']):
        strPath = newFolder + k + fType
        oFile = open(strPath, 'w')
        newList = list(v)
        dAgency.append(k)                  #Store all Agency names into list: dAgency
        generalFunctions.gebizData[k] = newList
        keys = newList[0].keys()
        dict_writer = csv.DictWriter(oFile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(newList)
    print"Data extracted!"
    generalFunctions.gebizKeys = dAgency
    gFile.close()
    oFile.close()
    return {'dir': newFolder, 'agencies': dAgency, 'filetype': fType}