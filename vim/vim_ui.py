window_editor=0
window_viewer=1

class Ui():

    def __init__(self, vim):
        self.vim = vim

    def set_driver(self, driver):
        self.driver = driver

    def get_query(self):
        self.vim.command('norm ^yf;')
        self.vim.command("let query=getreg('\"')")
        query = self.vim.eval('query')
        return query

    def select(self):
        cw = self.vim.current.window
        win_list = list(self.vim.windows)
        i = win_list.index(cw)
        if(i == window_editor):
            query = self.get_query()
            try:
                results = self.driver.cur.execute(query)
            except:
                print "error executing"
            self.show_results(results)
            
    def show_results(self, data):
        results = self.driver.to_csv("", data)
        results = results.split('\n')
        cb = self.vim.windows[window_viewer].buffer
        cb[:] = None
        cb[:len(results)] = results

    def close(self):
        self.driver.close()
        self.vim.command('qa!')
