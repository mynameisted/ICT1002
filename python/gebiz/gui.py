from Tkinter import *
import openFile
import splitRaw
import sortValue

#   Calls the openFile function 1 and stores the returned values {'dir':filePath,'filename':fileName}
#chosenFilePath = openFile.chooseFile()
#   Calls the splitfile function 2 and stores the returned values {'dir':directory,'agencies':dAgency, 'filetype':".txt"}.
#agencyList = splitRaw.splitFile(chosenFilePath['dir'])
#   Calls the sortTotalAward function 3 and stores the returned values {}
#sortedValueList = sortValue.sortTotalAward(agencyList['dir'],agencyList['agencies'],agencyList['filetype'],'desc')
#print sortedValueList



##################################   GUI STUFF   ###########################################



#Create tk window.
my_window = Tk()
my_window.title("GeBIZ Analyzer v1.0")
#my_window.geometry(str(windowWidth)+"x"+str(windowHeight)+"+"+str(windowOffsetX)+"+"+str(windowOffsetY))
my_window.iconbitmap('gebiz.ico')
my_window.config(background="lightcyan2")

#label_1= Label(my_window,width='20',height='3',bg='red')
#label_2= Label(my_window,width='20',height='3',bg='green')

welcomeText = "Welcome to the GeBIZ Historical Analyser!\n To proceed, please select a CSV file below."
tkWelcomeMsg = Message(my_window, text=welcomeText)

tkChooseCSVBtn = Label(my_window, text="Choose File")

tkWelcomeMsg.grid(row=0,column=0)
tkChooseCSVBtn.grid(row=2,column=0)
#label_1.grid(row=0,column=0)
#label_2.grid(row=0,column=1)
tkChooseCSVBtn.bind('<Button-1>',lambda event: openFile.chooseFile())


my_window.mainloop()


