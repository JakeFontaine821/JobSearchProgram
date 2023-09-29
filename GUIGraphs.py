import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import TestDataBase as db

class Graphs():
    def __init__(self, databaseOBJ):
        self.databaseOBJ = databaseOBJ
        self.graphFigure = Figure(figsize=(7.5, 4), dpi=100)
        print("init Graphs")

    def CreateCanvas(self, master):
        self.canvas = FigureCanvasTkAgg(self.graphFigure, master=master)
        # canvas.draw()
        self.canvas.get_tk_widget().grid(columnspan=3)

################################################################################################
    def Graph_EntriesPerDay(self):
        print("Switch to Entries per day graph")

        self.graphFigure.clear()

        today = datetime.today()
        x = []
        y = []        
        for i in range(31):
            date = today - timedelta(days=i)
            x.append(date.strftime("%m-%d"))
            numberOfEntries = self.databaseOBJ.GetEntryWithDate(date.strftime("%Y-%m-%d"))
            y.append(len(numberOfEntries))

        x = list(reversed(x))
        y = list(reversed(y))
        default_x_ticks = range(len(x))

        self.plot1 = self.graphFigure.add_subplot(111)
        self.plot1.bar(default_x_ticks, y)
        
        custom_x_ticks = default_x_ticks[::3]
        custom_x_labels = [x[i] for i in custom_x_ticks]
        self.plot1.set_xticks(custom_x_ticks)
        self.plot1.set_xticklabels(custom_x_labels)
        
        max_y = max(y)
        y_ticks = np.arange(0, max_y + 1, 1)
        self.plot1.set_yticks(y_ticks)

        self.plot1.set_title("Entries Per Day")
        self.plot1.set_xlabel("Date")
        self.plot1.set_ylabel("Number of Entries")

        self.canvas.draw()

################################################################################################
    def Graph_ResultsPerDay(self):
        print("Switch to Results per day graph")

        self.graphFigure.clear()

        today = datetime.today()
        x = []
        y = []
        
        for i in range(31):
            date = today - timedelta(days=i)
            x.append(date.strftime("%m-%d"))
            numberOfEntries = self.databaseOBJ.GetResultWithDate(date.strftime("%Y-%m-%d"))
            y.append(len(numberOfEntries))

        x = list(reversed(x))
        y = list(reversed(y))
        default_x_ticks = range(len(x))

        self.plot1 = self.graphFigure.add_subplot(111)
        self.plot1.bar(default_x_ticks, y)
        
        custom_x_ticks = default_x_ticks[::3]
        custom_x_labels = [x[i] for i in custom_x_ticks]
        self.plot1.set_xticks(custom_x_ticks)
        self.plot1.set_xticklabels(custom_x_labels)
        max_y = max(y)
        y_ticks = np.arange(0, max_y + 1, 1)
        self.plot1.set_yticks(y_ticks)

        self.plot1.set_title("Results Per Day")
        self.plot1.set_xlabel("Date")
        self.plot1.set_ylabel("Number of Results")

        self.canvas.draw()

################################################################################################
    def Graph_Placeholder(self):
        print("Switch to Placeholder graph")
        self.graphFigure.clear()

        y = [i**2 for i in range(101)]
        self.plot1 = self.graphFigure.add_subplot(111)
        self.plot1.plot(y)
        self.plot1.set_title("Placeholder Graph")

        self.canvas.draw()