from tkinter import *
import TestDataBase as db
import GUIEntryFrame

database = db.JobSearchDataBaseComms()

def on_closing():
    database.CloseConnection()
    window.quit()

def NewEntry():
    companyName = addEntryFrame.txtCompanyName.get()
    jobTitle = addEntryFrame.txtJobTitle.get()
    dateApplied = addEntryFrame.txtDateApplied.get()
    result = addEntryFrame.txtResult.get()
    dateResult = addEntryFrame.txtDateResult.get()
    if companyName != "" and jobTitle != "" and dateApplied != "":
        database.AddJobEntry(companyName, jobTitle, dateApplied, result, dateResult)
        addEntryFrame.txtCompanyName.delete(0,END)
        addEntryFrame.txtJobTitle.delete(0,END)
        addEntryFrame.txtDateApplied.delete(0,END)
        addEntryFrame.txtResult.delete(0,END)
        addEntryFrame.txtDateResult.delete(0,END)
        ReloadEntries()

def ReloadEntries():
    list.delete(0,END)
    for entry in database.LoadEntries():
        list.insert(END, "{} - {}".format(entry[1], entry[2]))

def DeleteEntry():
    for entry in list.curselection():
        database.DeleteEntry(entry)
    ReloadEntries()

def CreateUpdateWindow():
    if len(list.curselection()) == 1:
        # Create New Frame
        updateFrame = GUIEntryFrame.EntryFrame()
        newWindow = updateFrame.CreateEntryFrame(window=window, editPage=True)
        # Throw In Button
        btnUpdateEntry = Button(newWindow, text='Update Entry', width=40)
        btnUpdateEntry.grid(row=5, columnspan=2)
        # Set Title
        newWindow.title("Update Window")
        # Set Up Entry Boxes
        entryData = database.RetrieveEntry(list.curselection()[0])
        entryEID = entryData[0]
        updateFrame.txtCompanyName.insert(0, entryData[1])
        updateFrame.txtJobTitle.insert(0, entryData[2])
        updateFrame.txtDateApplied.insert(0, entryData[3])
        updateFrame.txtResult.insert(0, entryData[4])
        updateFrame.txtDateResult.insert(0, entryData[5])

window = Tk()
window.title("List of Job Applications Submitted")
# Top Menu
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=lambda : on_closing)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

# Top Left
scrollbar = Scrollbar(window)
scrollbar.grid(row=0, column=1, sticky=NS)
list = Listbox(window, yscrollcommand = scrollbar.set, width=50)
ReloadEntries()
list.grid(row=0, column=0)
scrollbar.config( command = list.yview )

# Top Right
addEntryFrame = GUIEntryFrame.EntryFrame()
topRightFrame = addEntryFrame.CreateEntryFrame(window=window, width=110)
topRightFrame.grid(row=0, column=2, sticky=N)

btnAddEntry = Button(topRightFrame, text='Add Entry', width=40, command=lambda : NewEntry())
btnAddEntry.grid(row=5, columnspan=2)

#Middle Row
btnEditEntry = Button(window, text='Edit Entry', width=40, command=lambda : CreateUpdateWindow())
btnEditEntry.grid(row=1, columnspan=2, pady=5)

btnEditEntry = Button(window, text='Delete Entry', width=40, command=lambda : DeleteEntry())
btnEditEntry.grid(row=1, column=2, columnspan=2)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()