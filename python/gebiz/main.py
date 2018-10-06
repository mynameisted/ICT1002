from Tkinter import *
import ttk,sys,os
import function1, function2, function3,function4

#Dictionary of color schemes
colors = {"blue":"#3598dc","red":"#c1392d","green":"#27ae61","lightgray":"#d6d8d9","darkgray":"#58606b","darkblue":"#202b3d"}
gebizCSV = {}
regConCSV = {}
gebizData = {}
gebizSortedSpending = []
f4conData = {}

#Functions
def quit(reason="Error Occured. Please try again."):
	sys.exit(reason)


#Class Definition
class newFrame(Frame):
	def __init__(self, parent, w, h):
		#Initialise frame with basic settings
		Frame.__init__(self, parent, background=colors['darkblue'])
		self.parent = parent
		self.parent.title("GeBIZ Analyzer V1.0 - 2018")
#		self.parent.resizable(width=FALSE, height=FALSE)
		self.parent.iconbitmap('gebiz.ico')
		self.style = ttk.Style()
#		self.style.theme_use("default")
		self.option_add("*Font", "Arial 11")
		self.option_add("*background", colors['darkblue'])
		self.option_add("*foreground", "white")
		self.centreWindow(w,h)
		self.pack(fill=BOTH, expand=1)

	#Function to define window size and positioning
	def centreWindow(self, scaleX=2, scaleY=2):
		userScreenWidth = self.parent.winfo_screenwidth()
		userScreenHeight = self.parent.winfo_screenheight()
		frameWidth = userScreenWidth / scaleX
		frameHeight = userScreenHeight / scaleY
		frameOffsetX = (userScreenWidth - frameWidth) / 2
		frameOffsetY = (userScreenHeight - frameHeight) / 2
		self.parent.geometry('%dx%d+%d+%d' % (frameWidth, frameHeight, frameOffsetX, frameOffsetY))

#Function to create tkinter Labels
def tkLabel(parent,text,color=None):
	if color:
		label = Label(parent,text=text, background=colors[color])
	else:
		label = Label(parent,text=text)
	return label

#Function to grid tkinter elements with basic parameters
def tkGrid(target,r,c=None,cs=None,padx="5",pady="10",ipadx="10",ipady="5",sticky=None):
	target.grid(row=r,column=c,columnspan=cs,padx=padx,pady=pady,ipadx=ipadx,ipady=ipady, sticky=sticky)

#Error Popup Window
def errorDialog(message="Unexpected Error encountered!\nPlease try again later!"):
	#Initialise new Error Window frame
	tkError = Tk()
	#Initialise new GUI frame
	error_window = newFrame(tkError,5,5)
	error_window.grid_columnconfigure(0, weight=1)
	error_window.grid_rowconfigure(0, weight=1)
	error_window.grid_rowconfigure(1, weight=1)
	errorMsg = tkLabel(error_window, message)
	errorMsg.config(wraplength=tkError.winfo_reqwidth())
	tkGrid(errorMsg,0,0)
	exitBtn = tkLabel(error_window,"Exit Program","red")
	tkGrid(exitBtn,1,0)
	#Bind function to exit entire program to button
	exitBtn.bind("<Button-1>", quit)
	#Bind function to exit entire program if user closes the window
	tkError.protocol("WM_DELETE_WINDOW", quit)
	error_window.mainloop()

#Error Popup Window
def popupDialog(message):
	#Initialise new Error Window frame
	tkPopup = Tk()
	#Initialise new GUI frame
	popup_Window = newFrame(tkPopup,5,5)
	popup_Window.grid_columnconfigure(0, weight=1)
	popup_Window.grid_rowconfigure(0, weight=1)
	popup_Window.grid_rowconfigure(1, weight=1)
	popupMsg = tkLabel(popup_Window, message)
	popupMsg.config(wraplength=tkPopup.winfo_reqwidth())
	tkGrid(popupMsg,0,0)
	continueBtn = tkLabel(popup_Window,"Continue","blue")
	tkGrid(continueBtn,1,0)
	#Bind function to exit entire program to button
	continueBtn.bind("<Button-1>", lambda x:tkPopup.destroy())
	popup_Window.mainloop()

#Error Popup Window
def splitFeedback(message):
	#Initialise new Error Window frame
	tkSplitFeedback = Tk()
	#Initialise new GUI frame
	splitFeedbackWindow = newFrame(tkSplitFeedback,5,5)
	splitFeedbackWindow.grid_columnconfigure(0, weight=1)
	splitFeedbackWindow.grid_columnconfigure(1, weight=1)
	splitFeedbackWindow.grid_rowconfigure(0, weight=1)
	splitFeedbackWindow.grid_rowconfigure(1, weight=1)
	feedbackMsg = tkLabel(splitFeedbackWindow, message)
	feedbackMsg.config(wraplength=tkSplitFeedback.winfo_reqwidth())
	tkGrid(feedbackMsg,0,0,cs=2)
	openDirBtn = tkLabel(splitFeedbackWindow,"View Folder","blue")
	tkGrid(openDirBtn,1,0,sticky="EW")
	openDirBtn.bind("<Button-1>", lambda x: os.startfile(gebizCSV['semiPath']+gebizData['directory']))
	continueBtn = tkLabel(splitFeedbackWindow,"Close","blue")
	tkGrid(continueBtn,1,1,sticky="EW")
	#Bind function to exit entire program to button
	continueBtn.bind("<Button-1>", lambda x:tkSplitFeedback.destroy())
	splitFeedbackWindow.mainloop()





#Main Window
def main():

	#Function 1 - Choose CSV.
	def f1chooseCSV(source):
		global gebizCSV, regConCSV
		#Select CSV For Gebiz Procurement
		if source == "gebiz":
			#Execute Function 1 - Select File
			f1chosenFileGebiz = function1.selectFile()
			#If a file is selected
			if f1chosenFileGebiz['path']:
				#Update GUI 
				chooseCSVBtnGebiz.config(text="Choose Another File",background=colors['lightgray'],fg=colors['darkblue'])
				chosenFileName = f1chosenFileGebiz['filename']
				#If file name is greater than 37 hcaracters, suffix with '...'
				if len(chosenFileName) > 37: 
					chosenFileName = chosenFileName[:37]+"..."
					#Display chosen file name
				selectedFileMsgGebiz.config(text="Selected File: " + chosenFileName,wraplength=landingFrame.winfo_reqwidth())
				tkGrid(chooseCSVBtnGebiz,r=5)
				tkGrid(selectedFileMsgGebiz,r=4,cs=3, pady=(0,10))
				gebizCSV = f1chosenFileGebiz

		#Select CSV for Registered Contractors
		elif source == "regcon":
			#Execute Function 1 - Select File
			f1chosenFileRegCon = function1.selectFile()
			#If a file is selected
			if f1chosenFileRegCon['path']:
				#Update GUI 
				chooseCSVBtnRegCon.config(text="Choose Another File",background=colors['lightgray'],fg=colors['darkblue'])
				chosenFileName = f1chosenFileRegCon['filename']
				#If file name is greater than 37 characters, suffix with '...'
				if len(chosenFileName) > 37: 
					chosenFileName = chosenFileName[:37]+"..."
					#Display chosen file name
				selectedFileMsgRegCon.config(text="Selected File: " + chosenFileName,wraplength=landingFrame.winfo_reqwidth())
				tkGrid(chooseCSVBtnRegCon,r=8)
				tkGrid(selectedFileMsgRegCon,r=7,cs=3, pady=(0,10))
				regConCSV = f1chosenFileRegCon
		if (gebizCSV and regConCSV):
			processFileBtn = tkLabel(landingFrame,"Next","blue")
			tkGrid(processFileBtn,r=11,c=1,pady=(20,0),sticky="EW")
			#Bind Function 2 to button
			processFileBtn.bind("<Button-1>", lambda x: mainMenu())


	#Main Menu 
	def mainMenu():
			#Destroy the initial landing page GUI frame
			landingFrame.destroy()
			#Initialise new GUI frame
			mainMenuFrame = newFrame(tkWindow,1.5,1.5)
			mainMenuFrame.grid_columnconfigure(0, weight=1)
			mainMenuFrame.grid_columnconfigure(1, weight=1)
			mainMenuFrame.grid_columnconfigure(2, weight=1)
			mainMenuFrame.grid_columnconfigure(3, weight=1)
			mainMenuMsg = tkLabel(mainMenuFrame, "MAIN MENU")
			mainMenuMsg.config(font=("Arial 14"))

			tkGrid(mainMenuMsg,0,0,cs=4,pady=30)

			f2SplitAgencyMsg = tkLabel(mainMenuFrame, "Analyse GeBiz awarded data")
			tkGrid(f2SplitAgencyMsg,1,0)
			f2SplitAgencyBtn = tkLabel(mainMenuFrame, "Process File","blue")
			tkGrid(f2SplitAgencyBtn,1,1,sticky="EW")
			f2SplitAgencyBtn.bind("<Button-1>", lambda x: f2processCSV(gebizCSV['path'],mainMenuFrame))


	#Function 2 - Process CSV. This exports the data into individual txt files by agency. 
	def f2processCSV(path,mainMenuFrame):
		try:
			global gebizData
			#Execute Function 2 - Split files
			gebizData = function2.sortGovAgency(path)
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error processing the Gebiz Procurement CSV file. Please ensure you select the right file, and try again later.")

		#Grid the rest of the main menu
		f3agencySpendingLabel = tkLabel(mainMenuFrame,"View GeBiz total spending by Agency")
		tkGrid(f3agencySpendingLabel,2,0)
		f3agencySpendingSortAsc = tkLabel(mainMenuFrame,"Sort Ascending",'blue')
		tkGrid(f3agencySpendingSortAsc,2,1,sticky="EW")
		f3agencySpendingSortDsc = tkLabel(mainMenuFrame,"Sort Descending",'blue')
		tkGrid(f3agencySpendingSortDsc,2,2,sticky="EW")
		#Bind Function 3 - Sort Total Spending by ascending to button
		f3agencySpendingSortAsc.bind("<Button-1>", lambda x: f3sortData(gebizData['gebizData'],"asc"))
		#Bind Function 3 - Sort Total Spending by descending to button
		f3agencySpendingSortDsc.bind("<Button-1>", lambda x: f3sortData(gebizData['gebizData'],"desc"))

		f4listRegConMsg = tkLabel(mainMenuFrame,"View Awarded Registered Contractors")
		tkGrid(f4listRegConMsg,3,0)
		f4listRegConBtn = tkLabel(mainMenuFrame,"Sort Ascending",'blue')
		tkGrid(f4listRegConBtn,3,1,sticky="EW")
		#Bind Function 3 - Sort Total Spending by ascending to button
		f4listRegConBtn.bind("<Button-1>", lambda x: f4ProcessRegCon(gebizCSV['path'],regConCSV['path']))

		splitFeedback('Agency-level data files created successfully the following location:\n\n'+gebizData['directory'])
		
	#Function 3 - Sort Total Spending. This calculates the total spending of each agency, and sorts the data. 
	def f3sortData(data,order):
		try:
			global gebizSortedSpending
			#Execute Function 3 - Sort Total Awards
			gebizSortedSpending = function3.sortTotalAward(data,order)
			#Initialise a new window and frame for displaying the sorted data
			sortDataWindow = Tk()
#			style = ttk.Style(sortDataWindow)
#			style.configure("Treeview", background="black", 
#                fieldbackground="black", foreground="white")
			treeFrame = newFrame(sortDataWindow,2,2)
			treeFrame.pack(side=TOP, fill=BOTH, expand=Y)
			treeFrame.rowconfigure(0, weight=1)
			treeFrame.columnconfigure(0, weight=1)
			#Declare header information for the sorted data.
			treeHeaders = ('Agency', 'Total Spending ($)')		
			#Create new Treeview for displaying sorted data
			tree = ttk.Treeview(treeFrame,columns=treeHeaders,show ='headings',selectmode='none')
			ysb = ttk.Scrollbar(treeFrame,orient=VERTICAL, command= tree.yview)
			tree['yscroll'] = ysb.set
			#Grid the treeview and scrollbar to frame
			tree.grid(row=0, column=0, sticky=NSEW)
			ysb.grid(row=0, column=1, sticky=NS)
			#Insert header data into treeview header
			for header in treeHeaders:
				tree.heading(header, text=header.title())			
			#Insert sorted Total Spending into treeview
			for row in gebizSortedSpending:
				tree.insert('', 'end', values=row, tags="row")
			tree.tag_configure('row',background=colors['darkblue'], foreground="white")
			treeFrame.configure(background=colors['darkblue'])
			sortDataWindow.update()
			sortDataWindow.minsize(sortDataWindow.winfo_width(), sortDataWindow.winfo_height())
			sortDataWindow.mainloop()

		except:
			errorDialog("Error displaying the sorted GeBiz Procurement information. Please try again later.")

	def f4ProcessRegCon(gebizPath,regConPath):
		global f4conData
		f4conData = function4.initializeexceldata(gebizPath,regConPath)




#====================== Main =====================================================
	#Initialise base GUI Window
	tkWindow = Tk()
	#Initialise new GUI frame
	landingFrame = newFrame(tkWindow,1.5,1.5)
	landingFrame.grid_columnconfigure(0, weight=1)
	landingFrame.grid_columnconfigure(2, weight=1)
	welcomeMsg = tkLabel(landingFrame,"Welcome to the GeBIZ Analyser! To proceed, please select the CSV files below.")
	tkGrid(welcomeMsg,0,cs=3,pady=(40,10))

	#Gebiz Procurement Items
	gebizCSVMsg = tkLabel(landingFrame,"Choose the GeBiz Procurement CSV file.")
	tkGrid(gebizCSVMsg,r=3,c=1)
	chooseCSVBtnGebiz = tkLabel(landingFrame,"Choose File", "blue")
	tkGrid(chooseCSVBtnGebiz,r=4,c=1)
	#Bind Function 1 - Choose CSV to button
	chooseCSVBtnGebiz.bind("<Button-1>", lambda x: f1chooseCSV("gebiz"))
	selectedFileMsgGebiz = tkLabel(landingFrame,"Selected File: ",'darkgray')

	#Registered Contractors Items
	regconCSVMsg = tkLabel(landingFrame,"Choose the Registered Contractors CSV file.")
	tkGrid(regconCSVMsg,r=6,c=1, pady=(10,0))
	chooseCSVBtnRegCon = tkLabel(landingFrame,"Choose File", "blue")
	tkGrid(chooseCSVBtnRegCon,r=7,c=1)
	#Bind Function 1 - Choose CSV to button
	chooseCSVBtnRegCon.bind("<Button-1>", lambda x: f1chooseCSV("regcon"))
	selectedFileMsgRegCon = tkLabel(landingFrame,"Selected File: ",'darkgray')
	tkWindow.update()
	tkWindow.minsize(tkWindow.winfo_width(), tkWindow.winfo_height())
	tkWindow.mainloop()


if __name__ == '__main__':
	main()
else:
	pass
