from tkinter import *
import tkinter.messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import TestDataBase as db
import GUIEntryFrame
import GUIGraphs

database = db.JobSearchDataBaseComms()

mainFrame = GUIEntryFrame.EntryFrame()
updateFrame = GUIEntryFrame.EntryFrame()

graphManager = GUIGraphs.Graphs(database)

def on_closing():
    database.CloseConnection()
    window.quit()

def GetText(frame):
    companyName = frame.txtCompanyName.get()
    jobTitle = frame.txtJobTitle.get()
    dateApplied = frame.txtDateApplied.get()
    result = frame.txtResult.get()
    dateResult = frame.txtDateResult.get()
    return [companyName, jobTitle, dateApplied, result, dateResult]

def ClearEntryBoxes(frame):
    frame.txtCompanyName.delete(0,END)
    frame.txtJobTitle.delete(0,END)
    frame.txtDateApplied.delete(0,END)
    frame.txtResult.delete(0,END)
    frame.txtDateResult.delete(0,END)

def NewEntry(frame):
    newEntry = GetText(frame)
    today = datetime.today()
    date_format = '%Y-%m-%d'
    if newEntry[0] == "" or newEntry[1] == "":
        tkinter.messagebox.showerror("Error", "Company Name and Job Title MUST have entries")
        return    
    if newEntry[2] == '':
        database.AddJobEntry(newEntry)
        ClearEntryBoxes(frame)
        ReloadEntries()
    else:
        try:
            date_obj = datetime.strptime(newEntry[2], date_format)
            if date_obj < today:
                database.AddJobEntry(newEntry)
                ClearEntryBoxes(frame)
                ReloadEntries()
            else:
                tkinter.messagebox.showerror("Error", "Date Applied hasn't happened yet")
        except ValueError:
            tkinter.messagebox.showerror("Error", "Date Applied must be blank or follow YYYY-MM-DD")

def ReloadEntries():
    list.delete(0,END)
    for entry in database.LoadEntries():
        list.insert(END, "{}. {} | {} ----- {}".format(entry[0], entry[1], entry[2], entry[4]))

def DeleteEntry():
    for index in list.curselection():
        entry = list.get(index)
        database.DeleteEntry(entry[0])
    ReloadEntries()

def UpdateEntry(eid, frame):
    newEntry = GetText(frame)
    if newEntry[0] != "" and newEntry[1] != "" and newEntry[2] != "":
        database.UpdateEntry(eid, newEntry)
        ReloadEntries()
        frame.newFrame.destroy()

def CreateUpdateWindow():
    if len(list.curselection()) == 1:
        # Create New Frame
        newWindow = updateFrame.CreateEntryFrame(window=window, editPage=True)
        newWindow.title("Update Window")
        # Set Up Entry Boxes
        entry = list.get(list.curselection()[0])
        entryData = database.RetrieveEntry(entry[0])
        entryEID = entryData[0]
        updateFrame.txtCompanyName.insert(0, entryData[1])
        updateFrame.txtJobTitle.insert(0, entryData[2])
        updateFrame.txtDateApplied.insert(0, entryData[3])
        updateFrame.txtResult.insert(0, entryData[4])
        updateFrame.txtDateResult.insert(0, str(entryData[5]))
        # Throw In Button
        btnUpdateEntry = Button(newWindow, text='Update Entry', width=40, command=lambda : UpdateEntry(entryEID, updateFrame))
        btnUpdateEntry.grid(row=5, columnspan=2)        

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
list = Listbox(window, yscrollcommand = scrollbar.set, width=60)
ReloadEntries()
list.grid(row=0, column=0, padx=5)
scrollbar.config( command = list.yview )

# Top Right
topRightFrame = mainFrame.CreateEntryFrame(window=window, width=110)
topRightFrame.grid(row=0, column=2, sticky=N)

btnAddEntry = Button(topRightFrame, text='Add Entry', width=40, command=lambda : NewEntry(mainFrame))
btnAddEntry.grid(row=5, columnspan=2)

#Middle Row
btnEditEntry = Button(window, text='Edit Entry', width=40, command=lambda : CreateUpdateWindow())
btnEditEntry.grid(row=1, columnspan=2, pady=5)

btnDeleteEntry = Button(window, text='Delete Entry', width=40, command=lambda : DeleteEntry())
btnDeleteEntry.grid(row=1, column=2, columnspan=2)

# Middle Section
middleFrame = Frame(window)
middleFrame.grid(row=2, column=0, columnspan=3, pady=5)

graphFigure = Figure(figsize=(7.5, 4), dpi=100)

Button(middleFrame, text="Applications Per Day", width=33).grid(row=0, column=0)
Button(middleFrame, text="Results Per Day", width=33).grid(row=0, column=1)
Button(middleFrame, text="Placeholder", width=33).grid(row=0, column=2)
######################## Actual graph section
graphManager.Graph_EntriesPerDay(graphFigure)
########################
canvas = FigureCanvasTkAgg(graphFigure, master=middleFrame)
canvas.draw()
canvas.get_tk_widget().grid(columnspan=3)


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()