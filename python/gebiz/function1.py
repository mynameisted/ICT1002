"""This module initializes a popup file chooser using tkFileDialog's askopenfilename."""
import tkFileDialog

#Function to select CSV File via a file explorer dialog
def selectFile():
	"""Return value structure:{'path':filePath,'filename':fileName}"""
	#Initialize the file explorer dialog
	filePath = tkFileDialog.askopenfilename(title="Select file", filetypes=[("CSV Files", "*.csv")])
	#Split the selected file path
	filePathSplit = filePath.split("/")
	#Store the file name only in another variable
	fileName = filePathSplit[len(filePathSplit)-1]
	return {'path':filePath,'filename':fileName}