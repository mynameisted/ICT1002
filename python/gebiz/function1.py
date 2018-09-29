import tkFileDialog
import generalFunctions

def selectFile():
    fileName = tkFileDialog.askopenfilename(title="Select file", filetypes=[("CSV Files", "*.csv")])
    filePath = fileName
    fileName = filePath.split("/")[-1]
    generalFunctions.selectedFile = {'path':filePath,'filename':fileName}
    return {'path':filePath,'filename':fileName}
    print generalFunctions.selectedFile
