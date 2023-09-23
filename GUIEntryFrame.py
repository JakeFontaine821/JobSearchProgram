from tkinter import *

class EntryFrame():
    def __init__(self):
        print("init")

    def CreateEntryFrame(self, window, width=None, height=None, editPage=None):
        if editPage:
            newFrame = Toplevel(window, width=width, height=height)
        else:
            newFrame = Frame(window, width=width, height=height)

        self.lblCompanyName = Label(newFrame, text='Company Name:')
        self.lblCompanyName.grid(row=0, column=0, pady=5)
        self.txtCompanyName = Entry(newFrame, width=30)
        self.txtCompanyName.grid(row=0, column=1, padx=10)

        self.lblJobTitle = Label(newFrame, text='Job Title:')
        self.lblJobTitle.grid(row=1, column=0, pady=5)
        self.txtJobTitle = Entry(newFrame, width=30)
        self.txtJobTitle.grid(row=1, column=1)

        self.lblDateApplied = Label(newFrame, text='Date Applied:')
        self.lblDateApplied.grid(row=2, column=0, pady=5)
        self.txtDateApplied = Entry(newFrame, width=30)
        self.txtDateApplied.grid(row=2, column=1)

        self.lblResult = Label(newFrame, text='Result:')
        self.lblResult.grid(row=3, column=0, pady=5)
        self.txtResult = Entry(newFrame, width=30)
        self.txtResult.grid(row=3, column=1)

        self.lblDateResult = Label(newFrame, text='Date Result Received:')
        self.lblDateResult.grid(row=4, column=0, pady=5)
        self.txtDateResult = Entry(newFrame, width=30)
        self.txtDateResult.grid(row=4, column=1)
        return newFrame