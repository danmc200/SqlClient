#!/usr/bin/python
import sqlite3 as lite
import os

class SqlDriver():
                   
    def __init__(self, dbname):
        self.con = self.connect(dbname)
        self.cur = self.con.cursor()

    def get_csv_headers(self):
        headers = ""
        if(self.cur.description == None):
            return None
        for x in range (0, len(self.cur.description)):
            headers += self.cur.description[x][0] + ','
        return headers[:-1]

    def to_csv(self, csv, data):
        for row in data:
            csv += '\n'
            for col in row:
                csv += str(col) + ','
            csv = csv[:-1]
        return csv

    def get_metadata(self, table_name):
        self.cur.execute('PRAGMA table_info(' + table_name + ')')
        data = self.cur.fetchall()
        return self.to_csv("", data)

    def get_tables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        data = self.cur.fetchall()
        return self.to_csv("", data)

    def connect(self, dbname):
        return lite.connect(dbname)

    def close(self):
        test_close(self.cur)
        self.con.close()

def test(driver):
    driver.cur.execute("create table songs(id int(10), track_name varchar(100))")
    filename = os.path.dirname(os.path.realpath(__file__)) + "/songs.csv"
    test_fle = open(filename, 'r')
    for line in test_fle.readlines():
        driver.cur.execute("insert into songs values(" + line + ")")
def test_close(cur):
    try:
        cur.execute('drop table songs')
    except:
        print "already dropped"
