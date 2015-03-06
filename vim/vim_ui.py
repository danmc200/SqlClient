import vim_sql_complete
window_editor=0
window_viewer=1

class Ui():

    def __init__(self, vim):
        self.vim = vim

    def set_driver(self, driver):
        self.driver = driver
        self.complete = vim_sql_complete.Complete(self.vim, self.driver)

    def get_query(self):
        query = self.vim.eval('g:query')
        return query

    def complete(self):
        cur_win = self.vim.current.window
        cursor = cur_win.cursor
        chars = cur_win.buffer[cursor[0]-1]
        omni = chars.split(' ')[-1]
        self.complete.set_complete(omni)

    def select(self):
        cw = self.vim.current.window
        win_list = list(self.vim.windows)
        i = win_list.index(cw)
        if(i == window_editor):
            query = self.get_query()
            try:
                results = self.driver.cur.execute(query)
                self.show_results(results)
            except:
                print "error executing"
            
    def show_results(self, data):
        results = self.driver.to_csv(self.driver.get_csv_headers(), data)
        results = results.split('\n')
        cb = self.vim.windows[window_viewer].buffer
        cb[:] = None
        cb[:len(results)] = results

    def close(self):
        self.driver.close()
        self.vim.command('qa!')
