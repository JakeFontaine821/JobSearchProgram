import TestDataBase as db

class Graphs():
    def __init__(self, databaseOBJ):
        self.databaseOBJ = databaseOBJ
        print("init Graphs")

    def Graph_EntriesPerDay(self, figure):
        self.databaseOBJ.GetEntriesFromLastThirtyDays()
        y = [i**2 for i in range(101)]
        plot1 = figure.add_subplot(111)
        plot1.plot(y)
        print("Will put actual graph here")

    def Graph_Placeholder(self, figure):
        self.databaseOBJ.GetEntriesFromLastThirtyDays()
        y = [i**2 for i in range(101)]
        plot1 = figure.add_subplot(111)
        plot1.plot(y)