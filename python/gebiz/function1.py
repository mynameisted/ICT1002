import tkFileDialog

def selectFile():
    filePath = tkFileDialog.askopenfilename(title="Select file", filetypes=[("CSV Files", "*.csv")])
    filePathSplit = filePath.split("/")
    filePathSemi = "/".join(filePathSplit[0:len(filePathSplit)-1])
    fileName = filePathSplit[len(filePathSplit)-1]
#    fileName = filePath.split("/")[-1]
    return {'path':filePath,'semiPath':filePathSemi,'filename':fileName}