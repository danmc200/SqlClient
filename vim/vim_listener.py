import threading, time
import sqlite3_complete

class VimListener(threading.Thread):

    def __init__(self, vim, ui, dbname):
        super(VimListener, self).__init__()
        self.vim =  vim
        self.ui = ui
        self.dbname = dbname
        self.kill = False
        self.actions = {
            'quit': self.quit,
            'select': self.ui.select}

    def quit(self):
        self.kill = True

    def run(self):
        driver = sqlite3_complete.SqlDriver(self.dbname)
        self.ui.set_driver(driver)
        sqlite3_complete.test(driver)
        while(not self.kill):
            action = self.vim.eval('g:action')
            if(action in self.actions):
                self.vim.command('let g:action=""')
                self.actions[action]()
            time.sleep(.1)
        self.ui.close()
