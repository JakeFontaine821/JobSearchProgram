import mysql.connector
import yaml

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

    def AddJobEntry(self, companyName, jobTitle, dateApplied, result, dateResult):
        self.cursor.execute("SELECT count(*) from job_entries")
        newEID = self.cursor.fetchone()

        query = "insert into job_entries (eid, company_name, job_title, date_applied, result, date_result) values ({}, '{}', '{}', '{}', '{}', '{}')".format(newEID[0], companyName, jobTitle, dateApplied, result, dateResult)

        self.cursor.execute(query)
        self.mydb.commit()

    def LoadEntries(self):
        query = "SELECT * FROM job_entries"
        self.cursor.execute(query)
        entries = self.cursor.fetchall()
        return entries

    def CloseConnection(self):
        print("Connection Closed")
        self.mydb.close()