from Tkinter import *
import tkFileDialog

def chooseFile():
	#Open input file selector gui
	filePath = tkFileDialog.askopenfilename(filetypes=(("CSV File - Comma Delimited","*.csv"), ("All file types","*")))
    #Print selected file name to user.
	filePathList = filePath.split('/')
	fileName = filePathList[len(filePathList)-1]
	return {'dir':filePath,'filename':fileName}
