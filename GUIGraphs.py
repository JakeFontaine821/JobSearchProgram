import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import TestDataBase as db

class Graphs():
    def __init__(self, databaseOBJ):
        self.databaseOBJ = databaseOBJ
        print("init Graphs")

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
        
        custom_x_ticks = default_x_ticks[::5]
        custom_x_labels = [x[i] for i in custom_x_ticks]
        plot1.set_xticks(custom_x_ticks)
        plot1.set_xticklabels(custom_x_labels)

    def Graph_Placeholder(self, figure):
        self.databaseOBJ.GetEntriesFromLastThirtyDays()
        y = [i**2 for i in range(101)]
        plot1 = figure.add_subplot(111)
        plot1.plot(y)