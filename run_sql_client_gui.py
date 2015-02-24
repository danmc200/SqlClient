#!/usr/bin/python
import drivers.sqlite3_complete as sqlite3_complete
import sql_gui
import wx

if __name__ == "__main__":
    try:
        dbname = sys.argv[1]
    except:
        dbname = raw_input("Enter Database name: ")

    app = wx.App()
    gui = sql_gui.Gui(None)
    driver = sqlite3_complete.SqlDriver(dbname)
    gui.init_gui(driver)
    sqlite3_complete.test(driver)
    app.MainLoop()
