import mysql.connector
import yaml
from datetime import datetime, timedelta

with open("./ConfigurationFiles/databaseconfig.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

class JobSearchDataBaseComms():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = cfg['mysql']['host'],
            user = cfg['mysql']['username'],
            password = cfg['mysql']['password'],
            database = cfg['mysql']['database']
        )
        print(self.mydb)
        self.cursor = self.mydb.cursor()

    def AddJobEntry(self, entryData):
        self.cursor.execute("SELECT count(*) from job_entries")
        newEID = self.cursor.fetchone()

        if entryData[2] == '':
            self.query = "INSERT INTO job_entries (eid, company_name, job_title, date_applied, result, date_result) VALUES ({}, '{}', '{}', CURDATE(), '{}', NULL)".format(newEID[0], entryData[0], entryData[1], entryData[3])
        else:
            self.query = "INSERT INTO job_entries (eid, company_name, job_title, date_applied, result, date_result) VALUES ({}, '{}', '{}', '{}', '{}', NULL)".format(newEID[0], entryData[0], entryData[1], entryData[2], entryData[3])

        self.cursor.execute(self.query)
        self.mydb.commit()
        print("Entry complete")

    def LoadEntries(self):
        self.query = "SELECT * FROM job_entries"
        self.cursor.execute(self.query)
        entries = self.cursor.fetchall()
        return entries
    
    def DeleteEntry(self, eid):
        self.query = "DELETE FROM job_entries WHERE eid= {}".format(eid)
        self.cursor.execute(self.query)
        self.mydb.commit()
        print("Entry Deleted")

    def RetrieveEntry(self, eid):
        self.query = "SELECT * FROM job_entries WHERE eid= {}".format(eid)
        self.cursor.execute(self.query)
        result = self.cursor.fetchone()
        print(result)
        return result

    def UpdateEntry(self, eid, entryData):
        if entryData[4] == 'None':
            self.query = "UPDATE job_entries SET company_name='{}', job_title='{}', date_applied='{}', result='{}' WHERE eid={};".format(entryData[0], entryData[1], entryData[2], entryData[3], eid)
        else:
            self.query = "UPDATE job_entries SET company_name='{}', job_title='{}', date_applied='{}', result='{}', date_result='{}' WHERE eid={};".format(entryData[0], entryData[1], entryData[2], entryData[3], entryData[4], eid)
        self.cursor.execute(self.query)
        self.mydb.commit()
        print("Entry Updated")

    def GetEntriesFromLastThirtyDays(self):
        thirty_days_ago = datetime.now() - timedelta(days=30)
        thirty_days_ago = thirty_days_ago.strftime("%Y-%m-%d")
        self.query = "SELECT * FROM job_entries WHERE DATEDIFF(CURDATE(),date_applied) <= 30"
        self.cursor.execute(self.query)
        result = self.cursor.fetchall()
        print(result)

    def GetEntryWithDate(self, date):
        self.query = "SELECT * FROM job_entries WHERE date_applied='{}'".format(date)
        self.cursor.execute(self.query)
        result = self.cursor.fetchall()
        return result

    def CloseConnection(self):
        print("Connection Closed")
        self.mydb.close()