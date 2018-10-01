import function1
import function2
import function3
import generalFunctions
from Tkinter import *
import ttk
import sys

#Dictionary of color schemes
colors = {"blue":"#3598dc","red":"#c1392d","green":"#27ae61","lightgray":"#d6d8d9","darkgray":"#58606b","darkblue":"#202b3d"}

#Class Defition
class newFrame(Frame):
    def __init__(self, parent, w, h):
        #Initialise frame with basic settings
        Frame.__init__(self, parent, background=colors['darkblue'])
        self.parent = parent
        self.parent.title("GeBIZ Analyzer V1.0 - 2018")
        self.parent.resizable(width=FALSE, height=FALSE)
        self.parent.iconbitmap('gebiz.ico')
        self.style = ttk.Style()
        self.style.theme_use("default")
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
def tkGrid(target,r,c=None,cs=None,padx="5",pady="5",ipadx="10",ipady="5",sticky=None):
    target.grid(row=r,column=c,columnspan=cs,padx=padx,pady=pady,ipadx=ipadx,ipady=ipady, sticky=sticky)

#Error Popup Window
def errorDialog(self):
    #Initialise new Error Window frame
    tkError = Tk()
    #Initialise new GUI frame
    error_window = newFrame(tkError,5,5)
    error_window.grid_columnconfigure(0, weight=1)
    error_window.grid_rowconfigure(0, weight=1)
    error_window.grid_rowconfigure(1, weight=1)
    errorMsg = tkLabel(error_window,"Unexpected Error Encountered!\nPlease try again later!")
    tkGrid(errorMsg,0,0)
    exitBtn = tkLabel(error_window,"Exit Program","red")
    tkGrid(exitBtn,1,0)
    #Bind function to exit entire program to button
    exitBtn.bind("<Button-1>", generalFunctions.quit)
    #Bind function to exit entire program if user closes the window
    tkError.protocol("WM_DELETE_WINDOW", generalFunctions.quit)
    error_window.mainloop()

#Main Window
def main():

    #Function 1 - Choose CSV.
    def f1chooseCSV(self):
        #Execute Function 1 - Select File
        f1chosenFile = function1.selectFile()
        #If a file is selected
        if f1chosenFile['path']:
            #Update GUI 
            chooseCSVBtn.config(text="Choose Another File",background=colors['lightgray'],fg=colors['darkblue'])
            chosenFileName = f1chosenFile['filename']
            #If file name is greater than 37 characters, suffix with '...'
            if len(chosenFileName) > 37: 
                chosenFileName = chosenFileName[:37]+"..."
            #Display chosen file name
            selectedFileMsg.config(text="Selected File: " + chosenFileName,wraplength=landingFrame.winfo_reqwidth())
            tkGrid(selectedFileMsg,r=1,cs=3, pady=(0,10))
            tkGrid(chooseCSVBtn,r=2,c=1,sticky="EW")
            processFileBtn = tkLabel(landingFrame,"Process File","blue")
            #Bind Function 2 to button
            processFileBtn.bind("<Button-1>", f2processCSV)
            tkGrid(processFileBtn,r=3,c=1,sticky="EW")


    #Function 2 - Process CSV. This exports the data into individual txt files by agency. 
    def f2processCSV(self):
        try:
            #Execute Function 2 - Split files
            f2splitAgencies = function2.sortGovAgency(generalFunctions.selectedFile['path'])
            #Destroy the initial landing page GUI frame
            landingFrame.destroy()
            #Initialise new GUI frame
            frame2 = newFrame(tkWindow,2,2)
            frame2.grid_columnconfigure(0, weight=1)
            frame2.grid_columnconfigure(3, weight=1)
            headerMsg = tkLabel(frame2,"View spending by Agency")
            tkGrid(headerMsg,0,0, pady=(20,0))
            sortAsc = tkLabel(frame2,"Sort Ascending",'blue')
            tkGrid(sortAsc,0,1,pady=(20,0))
            sortDsc = tkLabel(frame2,"Sort Descending",'blue')
            tkGrid(sortDsc,0,2,pady=(20,0))
            #Bind Function 3 - Sort Total Spending by ascending to button
            sortAsc.bind("<Button-1>", lambda x: f3sortData(generalFunctions.gebizData,"asc"))
            #Bind Function 3 - Sort Total Spending by descending to button
            sortDsc.bind("<Button-1>", lambda x: f3sortData(generalFunctions.gebizData,"desc"))
        except:
            #If Error, trigger errorDialog popup GUI.
            errorDialog(self)

    #Function 3 - Sort Total Spending. This calculates the total spending of each agency, and sorts the data. 
    def f3sortData(path,order):
        #Execute Function 3 - Sort Total Awards
        f3sortedData = function3.sortTotalAward(path,order)
        #Initialise a new window and frame for displaying the sorted data
        sortDataWindow = Tk()
        treeFrame = newFrame(sortDataWindow,2,2)
        treeFrame.pack(side=TOP, fill=BOTH, expand=Y)
        treeFrame.rowconfigure(0, weight=1)
        treeFrame.columnconfigure(0, weight=1)
        #Declare header information for the sorted data.
        treeHeaders = ('Agency', 'Total Spending ($)')        
        #Create new Treeview for displaying sorted data
        tree = ttk.Treeview(treeFrame,columns=treeHeaders,show = 'headings',selectmode='none')
        ysb = ttk.Scrollbar(treeFrame,orient=VERTICAL, command= tree.yview)
        tree['yscroll'] = ysb.set
        #Grid the treeview and scrollbar to frame
        tree.grid(row=0, column=0, sticky=NSEW)
        ysb.grid(row=0, column=1, sticky=NS)
        #Insert header data into treeview header
        for header in treeHeaders:
            tree.heading(header, text=header.title())            
        #Insert sorted Total Spending into treeview
        for row in f3sortedData:
            tree.insert('', 'end', values=row, tags="row")
        tree.tag_configure('row',background=colors['darkblue'], foreground="white")
        treeFrame.configure(background=colors['darkblue'])
        sortDataWindow.mainloop()

    #Initialise base GUI Window
    tkWindow = Tk()
    #Initialise new GUI frame
    landingFrame = newFrame(tkWindow,2,2)
    landingFrame.grid_columnconfigure(0, weight=1)
    landingFrame.grid_columnconfigure(2, weight=1)
    welcomeMsg = tkLabel(landingFrame,"Welcome to the GeBIZ Analyser! To proceed, please select a CSV file below.")
    tkGrid(welcomeMsg,0,cs=3,pady=(90,10))
    chooseCSVBtn = tkLabel(landingFrame,"Choose File", "blue")
    tkGrid(chooseCSVBtn,r=2,c=1)
    #Bind Function 1 - Choose CSV to button
    chooseCSVBtn.bind("<Button-1>", f1chooseCSV)
    selectedFileMsg = tkLabel(landingFrame,"Selected File: ",'darkgray')

    landingFrame.mainloop()


if __name__ == '__main__':
    main()
else:
    pass
