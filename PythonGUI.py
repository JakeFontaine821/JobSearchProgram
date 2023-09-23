from tkinter import *
import TestDataBase as db

database = db.JobSearchDataBaseComms()

def on_closing():
    database.CloseConnection()
    window.quit()

def NewEntry():
    companyName = txtCompanyName.get()
    jobTitle = txtJobTitle.get()
    dateApplied = txtDateApplied.get()
    result = txtResult.get()
    dateResult = txtDateResult.get()
    if companyName != "" and jobTitle != "" and dateApplied != "":
        database.AddJobEntry(companyName, jobTitle, dateApplied, result, dateResult)
        txtCompanyName.delete(0,END)
        txtJobTitle.delete(0,END)
        txtDateApplied.delete(0,END)
        txtResult.delete(0,END)
        txtDateResult.delete(0,END)
        ReloadEntries()

def ReloadEntries():
    list.delete(0,END)
    for entry in database.LoadEntries():
        list.insert(END, "{} - {}".format(entry[1], entry[2]))

def DeleteEntry():
    for entry in list.curselection():
        database.DeleteEntry(entry)
    ReloadEntries()

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
topRightFrame = Frame(window, width=110)
topRightFrame.grid(row=0, column=2, sticky=N)

lblCompanyName = Label(topRightFrame, text='Company Name:')
lblCompanyName.grid(row=0, column=0, pady=5)
txtCompanyName = Entry(topRightFrame, width=30)
txtCompanyName.grid(row=0, column=1, padx=10)

lblJobTitle = Label(topRightFrame, text='Job Title:')
lblJobTitle.grid(row=1, column=0, pady=5)
txtJobTitle = Entry(topRightFrame, width=30)
txtJobTitle.grid(row=1, column=1)

lblDateApplied = Label(topRightFrame, text='Date Applied:')
lblDateApplied.grid(row=2, column=0, pady=5)
txtDateApplied = Entry(topRightFrame, width=30)
txtDateApplied.grid(row=2, column=1)

lblResult = Label(topRightFrame, text='Result:')
lblResult.grid(row=3, column=0, pady=5)
txtResult = Entry(topRightFrame, width=30)
txtResult.grid(row=3, column=1)

lblDateResult = Label(topRightFrame, text='Date Result Received:')
lblDateResult.grid(row=4, column=0, pady=5)
txtDateResult = Entry(topRightFrame, width=30)
txtDateResult.grid(row=4, column=1)

btnAddEntry = Button(topRightFrame, text='Add Entry', width=40, command=lambda : NewEntry())
btnAddEntry.grid(row=5, columnspan=2)

#Middle Row
btnEditEntry = Button(window, text='Edit Entry', width=40)
btnEditEntry.grid(row=1, columnspan=2, pady=5)

btnEditEntry = Button(window, text='Delete Entry', width=40, command=lambda : DeleteEntry())
btnEditEntry.grid(row=1, column=2, columnspan=2)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()