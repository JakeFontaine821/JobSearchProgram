from tkinter import *

class EntryFrame():
    def __init__(self):
        print("init")

    def CreateEntryFrame(self, window, width=None, height=None, editPage=None):
        if editPage:
            self.newFrame = Toplevel(window, width=width, height=height)
        else:
            self.newFrame = Frame(window, width=width, height=height)

        self.lblCompanyName = Label(self.newFrame, text='Company Name:')
        self.lblCompanyName.grid(row=0, column=0, pady=5)
        self.txtCompanyName = Entry(self.newFrame, width=30)
        self.txtCompanyName.grid(row=0, column=1, padx=10)

        self.lblJobTitle = Label(self.newFrame, text='Job Title:')
        self.lblJobTitle.grid(row=1, column=0, pady=5)
        self.txtJobTitle = Entry(self.newFrame, width=30)
        self.txtJobTitle.grid(row=1, column=1)

        self.lblDateApplied = Label(self.newFrame, text='Date Applied:(YYYY-MM-DD)')
        self.lblDateApplied.grid(row=2, column=0, pady=5)
        self.txtDateApplied = Entry(self.newFrame, width=30)
        self.txtDateApplied.grid(row=2, column=1)

        self.lblResult = Label(self.newFrame, text='Result:')
        self.lblResult.grid(row=3, column=0, pady=5)
        self.txtResult = Entry(self.newFrame, width=30)
        self.txtResult.grid(row=3, column=1)

        self.lblDateResult = Label(self.newFrame, text='Date Result Received:(YYYY-MM-DD)')
        self.lblDateResult.grid(row=4, column=0, pady=5)
        self.txtDateResult = Entry(self.newFrame, width=30)
        self.txtDateResult.grid(row=4, column=1)
        return self.newFrame