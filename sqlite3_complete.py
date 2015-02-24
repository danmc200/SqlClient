#!/usr/bin/python
import sqlite3 as lite
import sys
import wx
import sql_gui

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

    def get_meta_data(self, table_name):
        self.cur.execute('PRAGMA table_info(' + table_name + ')')
        data = self.cur.fetchall()
        return self.to_csv("Metadata:", data)

    def get_tables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        data = self.cur.fetchall()
        return self.to_csv("Tables:", data)

    def connect(self, dbname):
        return lite.connect(dbname)

    def read_test(self):
        test_fle = open('songs.csv', 'r')
        return test_fle

    def test(self):
        self.cur.execute("create table songs(id int(10), track_name varchar(100))")
        test_fle = self.read_test()
        for line in test_fle.readlines():
            self.cur.execute("insert into songs values(" + line + ")")
        self.cur.execute('select * from songs')
        data = self.cur.fetchall()
        headers = self.get_csv_headers()

        print "data: \n" + self.to_csv(headers, data)
        print self.get_meta_data('songs')
        print self.get_tables()

    def close(self):
        try:
            self.cur.execute('drop table songs')
        except:
            print "already dropped"
        self.con.close()

if __name__ == "__main__":
    try:
        dbname = sys.argv[1]
    except:
        print "usage: command (dbname)"
        sys.exit(1)

    app = wx.App()
    gui = sql_gui.Gui(None)
    driver = SqlDriver(dbname)
    gui.init_gui(driver)
    driver.test()
    app.MainLoop()
