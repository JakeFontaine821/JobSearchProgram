import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

import TestDataBase as db

class Graphs():
    def __init__(self, databaseOBJ):
        self.databaseOBJ = databaseOBJ
        self.currentGraph = "EntriesPerDay"
        print("init Graphs")

################################################################################################
    def Graph_EntriesPerDay(self, figure):
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

        plot1 = figure.add_subplot(111)
        plot1.bar(default_x_ticks, y)
        
        custom_x_ticks = default_x_ticks[::3]
        custom_x_labels = [x[i] for i in custom_x_ticks]
        plot1.set_xticks(custom_x_ticks)
        plot1.set_xticklabels(custom_x_labels)
        
        max_y = max(y)
        y_ticks = np.arange(0, max_y + 1, 1)
        plot1.set_yticks(y_ticks)

        plot1.set_title("Entries Per Day")
        plot1.set_xlabel("Date")
        plot1.set_ylabel("Number of Entries")

################################################################################################
    def Graph_ResultsPerDay(self, figure):
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

        plot1 = figure.add_subplot(111)
        plot1.bar(default_x_ticks, y)
        
        custom_x_ticks = default_x_ticks[::3]
        custom_x_labels = [x[i] for i in custom_x_ticks]
        plot1.set_xticks(custom_x_ticks)
        plot1.set_xticklabels(custom_x_labels)
        max_y = max(y)
        y_ticks = np.arange(0, max_y + 1, 1)
        plot1.set_yticks(y_ticks)

        plot1.set_title("Results Per Day")
        plot1.set_xlabel("Date")
        plot1.set_ylabel("Number of Results")

################################################################################################
    def Graph_Placeholder(self, figure):
        y = [i**2 for i in range(101)]
        plot1 = figure.add_subplot(111)
        plot1.plot(y)
        plot1.set_title("Placeholder Graph")

################################################################################################
    def LoadGraph(self, figure, graph):
        if graph == "Placeholder":
            self.currentGraph = "Placeholder"
            self.Graph_Placeholder(figure)
        elif graph == "EntriesPerDay":
            self.currentGraph = "EntriesPerDay"
            self.Graph_EntriesPerDay(figure)
        elif graph == "ResultsPerDay":
            self.currentGraph = "ResultsPerDay"
            self.Graph_ResultsPerDay(figure)