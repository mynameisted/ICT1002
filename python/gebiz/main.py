import openFile
import splitRaw
import sortValue

#Calls the openFile function 1 and stores the returned values {'dir':filePath,'filename':fileName}
chosenFilePath = openFile.chooseFile()
#Calls the splitfile function 2 and stores the returned values {'dir':directory,'agencies':dAgency, 'filetype':".txt"}.
agencyList = splitRaw.splitFile(chosenFilePath['dir'])
#Calls the sortTotalAward function 3 and stores the returned values {}
sortedValueList = sortValue.sortTotalAward(agencyList['dir'],agencyList['agencies'],agencyList['filetype'],'desc')
#print sortedValueList

