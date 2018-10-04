import tkFileDialog

def selectFile():
    fileName = tkFileDialog.askopenfilename(title="Select file", filetypes=[("CSV Files", "*.csv")])
    filePath = fileName
    fileName = filePath.split("/")[-1]
    return {'path':filePath,'filename':fileName}