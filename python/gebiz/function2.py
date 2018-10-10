"""This module accepts in the file path from Function1 and processes each government agency's procurement data into one text file in a folder."""
import csv
import os
from itertools import groupby

gebizDataDict ={}
#Function to create a new folder for the output of text files.
def createFolder(directory):
    """Create folder in the given path"""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
#Function to group the data by agency and output each agency data to text files.
def sortGovAgency(path):
    """Read CSV file from given path, group the data by 'agency' and output each agency's data to one text file."""
    dictList = []
    dAgency = []
    fType = ".txt"
    #Opens the CSV file from user.
    with open(path, 'r') as gFile:
        #Insert the data extracted into a list.
        reader = csv.DictReader(gFile)
        for row in reader:
            dictList.append(row)
    dictList.sort(key=lambda x: x['agency'])
    #Folder creation.
    newFolder = './GovernmentAgencies/'
    createFolder(newFolder)

    print"Extracting data, please wait..."
    #Grouping of the data by 'agency'.
    for k, v in groupby(dictList, key=lambda x: x['agency']):
        strPath = newFolder + k + fType
        oFile = open(strPath, 'w')
        newList = list(v)
        #Store all Agency names into list: dAgency.
        dAgency.append(k)
        #Store all the grouped data into dictionary: gebizDataDict.
        gebizDataDict[k] = newList
        #Writes the grouped data into each .txt file.
        keys = newList[0].keys()
        dict_writer = csv.DictWriter(oFile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(newList)

    print"Data extracted!"
    gFile.close()
    oFile.close()
    relativePath = os.path.dirname(os.path.abspath(__file__))
    #Returns variables that can be used by other functions.
    return {"path":relativePath,"folder":newFolder,"agencies":dAgency,"gebizData":gebizDataDict}