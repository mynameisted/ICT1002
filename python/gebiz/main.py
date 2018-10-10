from Tkinter import *
import ttk
import sys
import os
from threading import Thread
import function1
import function2
import function3
import function4
import function5
import function6

#Dictionary of color schemes
colors = {"blue":"#3598dc","red":"#c1392d","green":"#27ae61","lightgray":"#d6d8d9","darkgray":"#58606b","darkblue":"#202b3d","tinteddarkblue":"#2e3d55"}
#Function 1 returned results - {'path':filePath,'filename':fileName}
f1gebizCSV = {}
#Function 1 returned results - {'path':filePath,'relativeFolder':filePathSemi,'filename':fileName}
f1regConCSV = {}
#Function 2 returned results - {"path":relativePath,"folder":newFolder,"agencies":dAgency,"gebizData":gebizDataDict}
f2gebizData = {}
#Function 3 returned results - [(Agency Name,Total Spending)..]
f3gebizSortedSpending = []
#Function 4 returned results - {'masteraward': masterawarddata, 'mastercont': mastercontdata, 'regcont': regcontnames,'awdregcontnames': regcontnamesawarded, 'awdnotregcontnames': contnames_awarded_notreg,'dictregconts': dictregcontractors_awarded, 'dictnotregconts': dictnotregcontractors_awarded}
f4conData = {}
#Function 5 returned results - {"regConAwards":regconAmt, "unregConAwards":nonregconAmt, "regConAwardsDesc":descregconAmt,"unregConAwardsDesc":descnonregconAmt,"top5Reg":top5Regi, "top5Unreg":top5Nonregi}
f5ConAwardData = {}

#===== Project Functions =====#

#Quits the entire program immediately.
def quit(reason="Error Occured. Please try again."):
	sys.exit(reason)

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

#===== Project Classes =====#

#Creates a new tkinter frame within a pre-declared parent TK Window 
class newFrame(Frame):
	def __init__(self, parent, w, h, windowTitle="GeBIZ Analyzer V1.0 - 2018"):
		#Initialise frame with basic settings
		Frame.__init__(self, parent, background=colors['darkblue'])
		self.parent = parent
		#Set Title of the parent window
		self.parent.title(windowTitle)
		#Decide if window will be resizable or not
		#self.parent.resizable(width=resize, height=resize)
		#Set parent icon bitmap
		self.parent.iconbitmap('gebiz.ico')
		self.style = ttk.Style()
		self.style.theme_use("default")
		self.option_add("*Font", "Arial 11")
		self.option_add("*background", colors['darkblue'])
		self.option_add("*foreground", "white")
		#Call function to set the height and width of the window against the screen dimensions, and position it centralised
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

#Creates a new tkinter treeView for displaying multi-column data
class treeView():
	def __init__(self,frame,parent,headers,data):
		frame.pack(side=TOP, fill=BOTH, expand=Y)
		frame.rowconfigure(0, weight=1)
		frame.columnconfigure(0, weight=1)
		style = ttk.Style(frame)
		style.theme_use("clam")
		style.configure("Treeview", background=colors['darkblue'], foreground="white", fieldbackground=colors['darkblue'])
		#Create new Treeview for displaying sorted data
		tree = ttk.Treeview(frame,columns=headers,show ='headings')
		#Create vertical scrollbar
		ysb = ttk.Scrollbar(frame,orient=VERTICAL, command= tree.yview)
		tree['yscroll'] = ysb.set
		#Grid the treeview and scrollbar to frame
		tree.grid(row=0, column=0, sticky="NESW")
		ysb.grid(row=0, column=1, sticky=NS)
		#Insert header data into treeview header
		for header in headers:
			tree.heading(header, text=header.title())
		#Insert data into treeview
		for row in data:
			tree.insert('', 'end', values=row, tags="row")
		#Configure the colors of the rows in the treeView
		#tree.tag_configure('row',background=colors['darkblue'], foreground="white")
		#frame.configure(background=colors['darkblue'])====================================
		#Execute an update to the main window	
		parent.update()
		#Set the minimum size of the window to the current width and height
		parent.minsize(parent.winfo_width(), parent.winfo_height())

#Creates a new tkinter list for displaying single-column data
class tkList():
	def __init__(self,frame,parent,header,data):
		frame.pack(side=TOP, fill=BOTH, expand=Y)
		frame.rowconfigure(0, weight=1)
		frame.columnconfigure(0, weight=1)
		#Create the tkinter Listbox
		tkListElement = Listbox(frame, activestyle="none")
		#Grid the list to the frame
		tkListElement.grid(row=0,column=0,sticky="NESW")
		#Create vertical scrollbar
		scrollbar = Scrollbar(frame, orient="vertical")
		scrollbar.config(command=tkListElement.yview)
		scrollbar.grid(row=0, column=1, sticky=NS)
		tkListElement.config(yscrollcommand=scrollbar.set)
		#Insert data into list
		for row in data:
		    tkListElement.insert(END, str(row))

#Fatal Error Popup Window - Creates a tkinter popup and cLoses the program when called. 
def errorDialog(message="Unexpected Error encountered!\nPlease try again later!"):
	#Initialise new Error Window frame
	tkError = Tk()
	#Initialise new GUI frame
	error_window = newFrame(tkError,5,5)
	error_window.grid_columnconfigure(0, weight=1)
	error_window.grid_rowconfigure(0, weight=1)
	error_window.grid_rowconfigure(1, weight=1)
	#Create the error message label
	errorMsg = tkLabel(error_window, message)
	#Wrap the message to the window width in case of overflow
	errorMsg.config(wraplength=tkError.winfo_reqwidth())
	tkGrid(errorMsg,0,0)
	#Create the button to close the program.
	exitBtn = tkLabel(error_window,"Exit Program","red")
	tkGrid(exitBtn,1,0)
	#Bind function to exit entire program to button
	exitBtn.bind("<Button-1>", lambda x:quit(message))
	#Bind function to exit entire program if user closes the error window instead
	tkError.protocol("WM_DELETE_WINDOW", lambda x:quit(message))
	#All GUI code for the window shall be above this line.
	ringBell()
	error_window.mainloop()

#Regular Informational pop-up window - Able to pass a message in, and clicks continue to dismiss window.
def popupDialog(message):
	#Initialise new Error Window frame
	tkPopupWindow = Tk()
	#Initialise new GUI frame
	popupFrame = newFrame(tkPopupWindow,5,5)
	popupFrame.grid_columnconfigure(0, weight=1)
	popupFrame.grid_rowconfigure(0, weight=1)
	popupFrame.grid_rowconfigure(1, weight=1)
	#Create the label with the message
	popupMsg = tkLabel(popupFrame, message)
	#Wrap text to window width in case of overflow
	popupMsg.config(wraplength=tkPopupWindow.winfo_reqwidth())
	tkGrid(popupMsg,0,0)
	#Create the continue button
	continueBtn = tkLabel(popupFrame,"Continue","blue")
	tkGrid(continueBtn,1,0)
	#Bind function to destroy the popup window when the user clicks the button
	continueBtn.bind("<Button-1>", lambda x:tkPopupWindow.destroy())
	#All GUI code for the window shall be above this line.
	ringBell()
	tkPopupWindow.mainloop()

#Informational Explorer pop-up window - Able to pass a message in, with the option to open specified directories in the file explorer
def popUpExplorerDialog(message, relativeFolder,directory):
	#Initialise new Error Window frame
	tkExplorerWindow = Tk()
	#Initialise new GUI frame
	tkExplorerFrame = newFrame(tkExplorerWindow,4.5,4.5)
	tkExplorerFrame.grid_columnconfigure(0, weight=1)
	tkExplorerFrame.grid_columnconfigure(1, weight=1)
	tkExplorerFrame.grid_rowconfigure(0, weight=1)
	tkExplorerFrame.grid_rowconfigure(1, weight=1)
	#Create the label with the message
	feedbackMsg = tkLabel(tkExplorerFrame, message)
	#Wrap text to window width in case of overflow
	feedbackMsg.config(wraplength=tkExplorerWindow.winfo_reqwidth())
	tkGrid(feedbackMsg,0,0,cs=2)
	#Create the open directory button
	openDirBtn = tkLabel(tkExplorerFrame,"View Folder","blue")
	tkGrid(openDirBtn,1,0,sticky="EW")
	#Bind function to open a folder location in the file explorer
	openDirBtn.bind("<Button-1>", lambda x: os.startfile(relativeFolder+directory))
	#Create the continue button
	continueBtn = tkLabel(tkExplorerFrame,"Close","blue")
	tkGrid(continueBtn,1,1,sticky="EW")
	#Bind function to destroy the popup window when the user clicks the button
	continueBtn.bind("<Button-1>", lambda x:tkExplorerWindow.destroy())
	#All GUI code for the window shall be above this line.
	ringBell()
	tkExplorerWindow.mainloop()

#Plays a bell sound when called.
def ringBell():
	print "\a"

#Main Function
def main():

	#Main Menu GUI - Pre-processing of GeBiz Data
	def mainMenu():
		#Destroy the initial landing page GUI frame
		landingFrame.destroy()
		#Initialise new GUI frame in the window
		mainMenuFrame = newFrame(tkWindow,1.25,1.25)
		mainMenuFrame.grid_columnconfigure(0, weight=1)
		mainMenuFrame.grid_columnconfigure(1, weight=1)
		mainMenuFrame.grid_columnconfigure(2, weight=1)
		mainMenuFrame.grid_columnconfigure(3, weight=1)
		#Header message - Main Menu
		mainMenuMsg = tkLabel(mainMenuFrame, "MAIN MENU")
		mainMenuMsg.config(font=("Arial 14"))
		tkGrid(mainMenuMsg,0,0,cs=4,pady=20)

		#Create section header for Gebiz Functions
		gebizSectionHeader = tkLabel(mainMenuFrame, "GeBiz Procurement Data","tinteddarkblue")
		tkGrid(gebizSectionHeader, 1,0,cs=4,pady=10,sticky="EW")

		#Create and grid the label for function 2 - Split CSV, write to file
		f2SplitAgencyMsg = tkLabel(mainMenuFrame, "Analyse GeBiz awarded data")
		tkGrid(f2SplitAgencyMsg,2,0)
		#Create and grid the button for function 2 - Split CSV, write to file
		f2SplitAgencyBtn = tkLabel(mainMenuFrame, "Process File","blue")
		tkGrid(f2SplitAgencyBtn,2,1,sticky="EW")
		#Bind function 2 to the button.
		f2SplitAgencyBtn.bind("<Button-1>", lambda x: f2processCSV(f1gebizCSV['path'],mainMenuFrame))

		#Create section header for Contractor Functions
		conSectionHeader = tkLabel(mainMenuFrame, "Registered/Unregistered Contractor Data","tinteddarkblue")
		tkGrid(conSectionHeader, 5,0,cs=4,pady=15,sticky="EW")
		#Create and grid the label for function 4 - Process contractor data, and list registered contractors
		processConMsg = tkLabel(mainMenuFrame, "Analyze contractor data")
		tkGrid(processConMsg,6,0)
		#Create and grid the button for function 4 - Process contractor data, and list registered contractors
		processConBtn = tkLabel(mainMenuFrame, "Process File","blue")
		tkGrid(processConBtn,6,1,sticky="EW")
		#Bind function 4 - Process Registered/Unregistered contractor data, and list registered contractors
		processConBtn.bind("<Button-1>", lambda x: f4PreProcessCon(f1gebizCSV['path'],f1regConCSV['path'],mainMenuFrame))
	
	#Main Menu GUI Part 2 - Gebiz Functions (After processing Gebiz Data)
	def mainMenuGebiz(mainMenuFrame):
		#Grid the rest of the main menu

		#Create and grid the labels and buttons for function 3 - View total spending of each agency
		f3agencySpendingLabel = tkLabel(mainMenuFrame,"View total tender value issed by every agency")
		tkGrid(f3agencySpendingLabel,3,0)
		f3agencySpendingSortAsc = tkLabel(mainMenuFrame,"Sort Ascending",'blue')
		tkGrid(f3agencySpendingSortAsc,3,1,sticky="EW")
		f3agencySpendingSortDsc = tkLabel(mainMenuFrame,"Sort Descending",'blue')
		tkGrid(f3agencySpendingSortDsc,3,2,sticky="EW")
		#Bind Function 3 to button - Sort Total Spending by ascending 
		f3agencySpendingSortAsc.bind("<Button-1>", lambda x: f3sortData(f2gebizData['gebizData'],"asc"))
		#Bind Function 3 to button - Sort Total Spending by descending 
		f3agencySpendingSortDsc.bind("<Button-1>", lambda x: f3sortData(f2gebizData['gebizData'],"desc"))

		#Create and grid the labels and buttons for function 6 - Categorize gov sector
		f6viewGroupedSpendingMsg = tkLabel(mainMenuFrame,"View total tender value issued by Government Sector")
		tkGrid(f6viewGroupedSpendingMsg,4,0)
		f6viewGroupedSpendingBtn = tkLabel(mainMenuFrame,"View Chart",'blue')
		tkGrid(f6viewGroupedSpendingBtn,4,1,sticky="EW")
		#Bind Function 6 to button - Group gov sectors and display a graph.
		f6viewGroupedSpendingBtn.bind("<Button-1>", lambda x: f6categorizeAgency(f1gebizCSV['path']))

	#Main Menu GUI Part 2 - Contractor Functions (After processing Contractor Data)
	def mainMenuCon(mainMenuFrame):
		#Create and grid the labels and buttons for function 4 - Process and list registered contractors
		f4listRegConMsg = tkLabel(mainMenuFrame,"View names of awarded registered contractors")
		tkGrid(f4listRegConMsg,7,0)
		f4listRegConBtn = tkLabel(mainMenuFrame,"View List",'blue')
		tkGrid(f4listRegConBtn,7,1,sticky="EW")
		#Bind Function 4 to button - View Registered Contractors
		f4listRegConBtn.bind("<Button-1>", lambda x: f4DisplayRegCon(f4conData['awdregcontnames']))

		#Create and grid the labels and buttons for function 5 - View Registered Contractor Award data
		f5regConAwardMsg = tkLabel(mainMenuFrame,"View total awarded tender value to registered contractors")
		tkGrid(f5regConAwardMsg,8,0)
		f5regConAwardBtn = tkLabel(mainMenuFrame,"View All",'blue')
		tkGrid(f5regConAwardBtn,8,1,sticky="EW")
		#Bind Function 5 to button - View Registered Contractor awarded data
		f5regConAwardBtn.bind("<Button-1>", lambda x: f5sumSpendingCon(f4conData['awdregcontnames'],f4conData['awdnotregcontnames'],f4conData['masteraward'],"viewReg",mainMenuFrame))
		f5regConAwardTop5Btn = tkLabel(mainMenuFrame,"View Top 5",'blue')
		tkGrid(f5regConAwardTop5Btn,8,2,sticky="EW")
		#Bind Function 5 to button - View Top 5 Registered Contractor awarded data
		f5regConAwardTop5Btn.bind("<Button-1>", lambda x: f5sumSpendingCon(f4conData['awdregcontnames'],f4conData['awdnotregcontnames'],f4conData['masteraward'],"viewRegTop5",mainMenuFrame))

		#Create and grid the labels and buttons for function 5 - View Unregistered Contractor Award data		
		f5unregConAwardMsg = tkLabel(mainMenuFrame,"View total awarded tender value to unregistered contractors")
		tkGrid(f5unregConAwardMsg,9,0)
		f5unregConAwardBtn = tkLabel(mainMenuFrame,"View All",'blue')
		tkGrid(f5unregConAwardBtn,9,1,sticky="EW")
		#Bind Function 5 to button - View Unregistered Contractor awarded data
		f5unregConAwardBtn.bind("<Button-1>", lambda x: f5sumSpendingCon(f4conData['awdregcontnames'],f4conData['awdnotregcontnames'],f4conData['masteraward'],"viewUnreg",mainMenuFrame))
		f5unregConAwardTop5Btn = tkLabel(mainMenuFrame,"View Top 5",'blue')
		tkGrid(f5unregConAwardTop5Btn,9,2,sticky="EW")
		#Bind Function 5 to button - View Top 5 Unregistered Contractor awarded data
		f5unregConAwardTop5Btn.bind("<Button-1>", lambda x: f5sumSpendingCon(f4conData['awdregcontnames'],f4conData['awdnotregcontnames'],f4conData['masteraward'],"viewUnregTop5",mainMenuFrame))

	#Main Menu GUI Part 3 - Function 5 Display Chart (After processing Contractor Data)
	def mainMenuConChart(mainMenuFrame):
		#Create and grid the labels and buttons for function 5 - View spending chart
		f4listRegConMsg = tkLabel(mainMenuFrame,"View proportion of smaller value tenders (< $100k)")
		tkGrid(f4listRegConMsg,10,0)
		f4listRegConBtn = tkLabel(mainMenuFrame,"View Chart",'blue')
		tkGrid(f4listRegConBtn,10,1,sticky="EW")
		#Bind Function 5 to button - View spending chart
		f4listRegConBtn.bind("<Button-1>", lambda x: f5showChart(f5ConAwardData['regConAwards']))



	#Function 1 - Choose CSV file
	def f1chooseCSV(source):
		global f1gebizCSV, f1regConCSV
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
				f1gebizCSV = f1chosenFileGebiz

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
				f1regConCSV = f1chosenFileRegCon
		#If both files have been selected, create the next button
		if (f1gebizCSV and f1regConCSV):
			csvProceedBtn = tkLabel(landingFrame,"Next","blue")
			tkGrid(csvProceedBtn,r=11,c=1,pady=(20,0),sticky="EW")
			#Binds the Main Menu function to run on click.
			csvProceedBtn.bind("<Button-1>", lambda x: mainMenu())

	#Function 2 - Process CSV. This exports the data into individual txt files by agency. 
	def f2processCSV(path,mainMenuFrame):
		try:
			#Global variable to store returned results of the function
			global f2gebizData
			#Execute Function 2 - Split files
			f2gebizData = function2.sortGovAgency(path)
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error processing the Gebiz Procurement CSV file. Please select the right file and try again later.")
		#Use multi-threading to asynchronously execute two functions at the same time
		#Create and display the extended functions for the Gebiz section
		mmThread = Thread(target = mainMenuGebiz(mainMenuFrame)).start()
		#Create a popup for files created and the directory, and let user click to open the folder.
		splitFeedbackThread =Thread(target = popUpExplorerDialog(str(len(f2gebizData['agencies']))+' agency-level data files created successfully at the following location:\n\n'+f2gebizData['folder'],f2gebizData['path'],f2gebizData['folder'])).start()
		#Start both threads 
		#mmThread.start()
		#splitFeedbackThread.start()

	#Function 3 - Sort Total Spending. This calculates the total spending of each agency, and sorts the data. 
	def f3sortData(data,order):
		try:
			#Global variable to store returned results of the function
			global f3gebizSortedSpending
			#Execute Function 3 - Sort Total Awards
			f3gebizSortedSpending = function3.sortTotalAward(data,order)
			#Initialise a new window and frame for displaying the sorted data
			sortDataWindow = Tk()
			#Initialise new frame for the data
			sortDataFrame = newFrame(sortDataWindow,2,2)
			#Initialise new treeView for displaying multi-column data
			sortedDataTree = treeView(sortDataFrame,sortDataWindow,["Agency","Total Spending($)"], f3gebizSortedSpending)
			#All GUI code for the window shall be above this line.
			sortDataWindow.mainloop()
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error displaying the sorted GeBiz Procurement information. Please try again later.")

	#Function 4a - Process registered contractors 
	def f4PreProcessCon(gebizPath,regConPath,mainMenuFrame):
		try:
			#Global variable to store returned results of the function
			global f4conData
			#Execute Function 4 - Process contractor data, lists registered contractors
			f4conData = function4.initializeexceldata(gebizPath,regConPath)
			#Create and display the extended functions for the Contractor section		
			mainMenuCon(mainMenuFrame)
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error processing the Gebiz & Registered Contractors CSV file. Please select the right files and try again later.")

	#Function 4b - Displays the list of registered contractors' names. 
	def f4DisplayRegCon(data):
		try:
			#Initialise a new window and frame for displaying the registered contractors
			regConWindow = Tk()
			#Initialise new frame for the data
			regConFrame = newFrame(regConWindow,2,2)
			#Initialise new listbox for displaying single-column data
			regConTree = tkList(regConFrame,regConWindow,['Awarded Registered Contractors'],data)
			#All GUI code for the window shall be above this line.
			regConWindow.mainloop()
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error displaying the registered contractors. Please try again later.")

	#Function 5 - Calculates total spending of registered/unregistered contractors
	def f5sumSpendingCon(awardedRegConNames, awardedUnregConNames, masterAwarded,requestType,mainMenuFrame):
		try:
			#Global variable to store returned results of the function
			global f5ConAwardData
			#If data is empty (aka first time running)
			if len(f5ConAwardData) ==0:
				#Execute Function 5 - Process Award data for registered and unregistered contractors
				f5ConAwardData = function5.top5(awardedRegConNames, awardedUnregConNames, masterAwarded)
				mainMenuConChart(mainMenuFrame)

			def f5CreateTree(headers,data):
				#Initialise a new window and frame for displaying the data
				f5TreeWindow = Tk()
				#Initialise new frame for the data
				f5TreeFrame = newFrame(f5TreeWindow,2,2)
				#Initialise new treeView for displaying multi-column data
				f5AllRegConTree = treeView(f5TreeFrame,f5TreeWindow,headers,data)
				#All GUI code for the window shall be above this line.
				f5TreeWindow.mainloop()

			#If request type is to view all registered contractor awards
			if requestType == "viewReg":
				f5CreateTree(["Registered Contractors","Total Spending($)"], f5ConAwardData['regConAwards'])
			#If request type is to view all non-registered contractor awards
			elif requestType == "viewUnreg":
				f5CreateTree(["Non-Registered Contractors","Total Spending($)"], f5ConAwardData['unregConAwards'])
			#If request type is to view Top 5 registered contractor awards
			elif requestType == "viewRegTop5":
				f5CreateTree(["Registered Contractors","Total Spending($)"], f5ConAwardData['top5Reg'])
			#If request type is to Top 5 non-registered contractor awards
			elif requestType == "viewUnregTop5":
				f5CreateTree(["Non-Registered Contractors","Total Spending($)"], f5ConAwardData['top5Unreg'])
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error processing the total awarded value of contractors. Please try again later.")

	def f5showChart(awardedRegConData):
		#Execute function 5 - Show chart on spending
		try:
			function5.regconStatistic(awardedRegConData)
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error displaying the chart on smaller value tenders. Please try again later.")

	#Function 6 - Sort Total Spending. This calculates the total spending of each agency, and sorts the data. 
	def f6categorizeAgency(path):
		try:
			#Execute function 6 - Categorize government sectors spendings and displays a chart
			function6.recategorize(path)
		except:
			#If Error, trigger errorDialog popup GUI.
			errorDialog("Error categorizing the government sectors. Please try again later.")



#====================== Main - Landing GUI ======================#
	#Initialise base GUI Window
	tkWindow = Tk()
	#Initialise new GUI frame
	landingFrame = newFrame(tkWindow,1.25,1.25)
	landingFrame.grid_columnconfigure(0, weight=1)
	landingFrame.grid_columnconfigure(2, weight=1)

	#Create the top heading welcome message
	welcomeMsg = tkLabel(landingFrame,"Welcome to the GeBIZ Analyser! To proceed, please select the CSV files below.")
	tkGrid(welcomeMsg,0,cs=3,pady=(40,10))

	#Gebiz Procurement Label
	gebizCSVMsg = tkLabel(landingFrame,"Choose the GeBiz Procurement CSV file.")
	tkGrid(gebizCSVMsg,r=3,c=1)
	#Gebiz Procurement Choose File Button
	chooseCSVBtnGebiz = tkLabel(landingFrame,"Choose File", "blue")
	tkGrid(chooseCSVBtnGebiz,r=4,c=1)
	#Gebiz Button - Bind Function 1 to select CSV
	chooseCSVBtnGebiz.bind("<Button-1>", lambda x: f1chooseCSV("gebiz"))
	#Gebiz Selected File Label
	selectedFileMsgGebiz = tkLabel(landingFrame,"Selected File: ",'darkgray')

	#Registered Contractors Label, button and selected file message
	regconCSVMsg = tkLabel(landingFrame,"Choose the Registered Contractors CSV file.")
	tkGrid(regconCSVMsg,r=6,c=1, pady=(10,0))
	#Registered Contractors Procurement Choose File Button
	chooseCSVBtnRegCon = tkLabel(landingFrame,"Choose File", "blue")
	tkGrid(chooseCSVBtnRegCon,r=7,c=1)
	#Registered Contractors Button - Bind Function 1 to select CSV
	chooseCSVBtnRegCon.bind("<Button-1>", lambda x: f1chooseCSV("regcon"))
	#Registered Contractors Selected File Label
	selectedFileMsgRegCon = tkLabel(landingFrame,"Selected File: ",'darkgray')

	#Execute an update to the main window
	tkWindow.update()
	#Set the minimum size of the window to the current width and height
	tkWindow.minsize(tkWindow.winfo_width(), tkWindow.winfo_height())

	#All GUI code for tkWindow shall be above this line.
	tkWindow.mainloop()


#If this file is run directly, call the main function to run.
if __name__ == '__main__':
	main()
#Else if it is being imported to another file, do nothing
else:
	pass
