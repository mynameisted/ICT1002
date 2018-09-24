import Tkinter as tk
import ttk
#from Tkinter import *
import tkFileDialog
import csv

fileDataRaw = "Selected File: ";

#tk root window parameters
windowWidth = 600
windowHeight = 420
windowOffsetX = 50
windowOffsetY = 50

def openFile(event):
	#Open input file selector gui
    chosenFile = tkFileDialog.askopenfilename(filetypes=(("CSV File - Comma Delimited","*.csv"), ("All file types","*")))
    #Print selected file name to user.
    filePath = chosenFile.split('/')
    fileName = filePath[len(filePath)-1]
    fileNameMsg.config(text = fileDataRaw+fileName)
	#Open selected file and print first row
    with open(chosenFile) as csvfile:
	reader = csv.DictReader(csvfile)
	#for row in reader:
	#	print(row['agency'], row['tender_no.'])

#Create tk root window.
root = tk.Tk()
root.title("GeBIZ Analyzer v1.0")
root.geometry(str(windowWidth)+"x"+str(windowHeight)+"+"+str(windowOffsetX)+"+"+str(windowOffsetY))
root.iconbitmap('gebiz.ico')
root.config(background="lightcyan2")

#Root window landing page.
welcomeMsg = "Welcome to the GeBIZ Historical Analyser!\n To proceed, please select a CSV file below."
msg = tk.Message(root, text = welcomeMsg)
msg.config(font=('Futura',12),width=400,background="lightcyan2")
msg.pack(ipadx = 40, ipady = 10)

#Root window file name message placeholder
fileNameMsg = tk.Message(root, text='')
fileNameMsg.config(font=('Futura',8),width=400, background="lightcyan2")
fileNameMsg.pack(ipady = 10)

#Button for selecting file.
chooseFileButton = tk.Label(root, text='Choose File', width=15, relief='raised')
chooseFileButton.pack()
chooseFileButton.bind('<Button-1>', openFile)

#Placeholder for file details
#loadingMsg = tk.Label(root,text='')
#loadingMsg.config(font=('Futura',8),width=550, background="lightcyan2")
#loadingMsg.pack(pady =10, padx = 10)


#Initialise root window. All codes for tk window has to be before this line.
root.mainloop()


'''
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()




import tkFileDialog

selectedFile = tkFileDialog.askopenfilename()
RawgovProcGebiz = open(selectedFile, 'r')
for i in range(10):
    currentLine = RawgovProcGebiz.readline()
    currentLine = currentLine.split(',')
    print currentLine
'''