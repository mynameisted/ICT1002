import function1
import function2
import function3
import generalFunctions
from Tkinter import *
import ttk
import sys


colors = {"blue":"#3598dc","red":"#c1392d","green":"#27ae61","lightgray":"#d6d8d9","darkgray":"#58606b","darkblue":"#202b3d"}

#Class Defition
class newFrame(Frame):
    def __init__(self, parent, w, h):
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

    def centreWindow(self, scaleX=2, scaleY=2):
        userScreenWidth = self.parent.winfo_screenwidth()
        userScreenHeight = self.parent.winfo_screenheight()
        frameWidth = userScreenWidth / scaleX
        frameHeight = userScreenHeight / scaleY
        frameOffsetX = (userScreenWidth - frameWidth) / 2
        frameOffsetY = (userScreenHeight - frameHeight) / 2
        self.parent.geometry('%dx%d+%d+%d' % (frameWidth, frameHeight, frameOffsetX, frameOffsetY))


def tkLabel(parent,text,color=None):
    if color:
        label = Label(parent,text=text, background=colors[color])
    else:
        label = Label(parent,text=text)
    return label

def tkGrid(target,r,c=None,cs=None,padx="5",pady="5",ipadx="10",ipady="5",sticky=None):
    if sticky:
        target.grid(row=r,column=c,columnspan=cs,padx=padx,pady=pady,ipadx=ipadx,ipady=ipady, sticky=sticky)
    else:
        target.grid(row=r,column=c,columnspan=cs,padx=padx,pady=pady,ipadx=ipadx,ipady=ipady)

#Error Popup Window
def errorDialog(self):
    tkError = Tk()
    error_window = newFrame(tkError,5,5)
    error_window.grid_columnconfigure(0, weight=1)
    error_window.grid_rowconfigure(0, weight=1)
    error_window.grid_rowconfigure(1, weight=1)
    errorMsg = tkLabel(error_window,"Unexpected Error Encountered!\nPlease try again later!")
    tkGrid(errorMsg,0,0)
    exitBtn = tkLabel(error_window,"Exit Program","red")
    tkGrid(exitBtn,1,0)
    exitBtn.bind("<Button-1>", generalFunctions.quit)
    tkError.protocol("WM_DELETE_WINDOW", generalFunctions.quit)
    error_window.mainloop()
#Main Window
def main():
    

    def f1chooseCSV(self):
        f1chosenFile = function1.selectFile()
        if f1chosenFile['path']:
            chooseCSVBtn.config(text="Choose Another File",background=colors['lightgray'],fg=colors['darkblue'])
            chosenFileName = f1chosenFile['filename']
            if len(chosenFileName) > 36: 
                chosenFileName = chosenFileName[:36]+"..."
            selectedFileMsg.config(text="Selected File: " + chosenFileName,wraplength=landingFrame.winfo_reqwidth())
            tkGrid(selectedFileMsg,r=1,cs=3, pady=(0,10))
            tkGrid(chooseCSVBtn,r=2,c=1,sticky="EW")
            processFileBtn = tkLabel(landingFrame,"Process File","blue")
            processFileBtn.bind("<Button-1>", f2processCSV)
            tkGrid(processFileBtn,r=3,c=1,sticky="EW")
        return f1chosenFile
    def f2processCSV(self):
        try:
            f2splitAgencies = function2.sortGovAgency(generalFunctions.selectedFile['path'])
            landingFrame.destroy()
            frame2 = newFrame(tkWindow,2,2)
            frame2.grid_columnconfigure(0, weight=1)
            frame2.grid_columnconfigure(3, weight=1)
    #        frame2.grid_columnconfigure(2, weight=1)
            #dataSet = tkLabel(frame2,"Total Agencies: "+str(len(f2splitAgencies['agencies'])))
            #tkGrid(dataSet,0,0,3)
            headerMsg = tkLabel(frame2,"View spending by Agency")
            tkGrid(headerMsg,0,0, pady=(20,0))
            sortAsc = tkLabel(frame2,"Sort Ascending",'blue')
            tkGrid(sortAsc,0,1,pady=(20,0))
            sortAsc.bind("<Button-1>", lambda x: f3sortData(generalFunctions.gebizData,"asc"))
            sortDsc = tkLabel(frame2,"Sort Descending",'blue')
            tkGrid(sortDsc,0,2,pady=(20,0))
            sortDsc.bind("<Button-1>", lambda x: f3sortData(generalFunctions.gebizData,"desc"))
        except:
            errorDialog(self)

    def f3sortData(path,order):
        f3sortedData = function3.sortTotalAward(path,order)
        sortDataWindow = Tk()
        treeFrame = newFrame(sortDataWindow,2,2)
        treeFrame.pack(side=TOP, fill=BOTH, expand=Y)
        treeFrame.rowconfigure(0, weight=1)
        treeFrame.columnconfigure(0, weight=1)
        sortDataWindow.protocol("WM_DELETE_WINDOW", sortDataWindow.destroy)
        # create the tree and scrollbars
        treeHeaders = ('Agency', 'Total Spending')        
        tree = ttk.Treeview(treeFrame,columns=treeHeaders,show = 'headings',selectmode='none')
        ysb = ttk.Scrollbar(treeFrame,orient=VERTICAL, command= tree.yview)
        tree['yscroll'] = ysb.set
        # add tree and scrollbars to frame
        tree.grid(row=0, column=0, sticky=NSEW)
        ysb.grid(row=0, column=1, sticky=NS)
        # configure column headings
        for header in treeHeaders:
            tree.heading(header, text=header.title())            
        # add data to the tree 
        for row in f3sortedData:
            tree.insert('', 'end', values=row, tags="row")
        tree.tag_configure('row',background=colors['darkblue'], foreground="white")
        treeFrame.configure(background=colors['darkblue'])
        sortDataWindow.mainloop()
        

        


    tkWindow = Tk()
    landingFrame = newFrame(tkWindow,2,2)
    landingFrame.grid_columnconfigure(0, weight=1)
    landingFrame.grid_columnconfigure(2, weight=1)
    welcomeMsg = tkLabel(landingFrame,"Welcome to the GeBIZ Analyser! To proceed, please select a CSV file below.")
    tkGrid(welcomeMsg,0,cs=3,pady=(90,10))
    chooseCSVBtn = tkLabel(landingFrame,"Choose File", "blue")
    tkGrid(chooseCSVBtn,r=2,c=1)
    chooseCSVBtn.bind("<Button-1>", f1chooseCSV)
    selectedFileMsg = tkLabel(landingFrame,"Selected File: ",'darkgray')


    landingFrame.mainloop()


if __name__ == '__main__':
    print "Being run directly!"
    main()
else:
    print "Being imported!"

