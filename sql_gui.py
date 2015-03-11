import drivers.sqlite3_complete as sqlite3_complete
import wx

class Gui(wx.Frame):

    def __init__(self, *args, **kw):
        super(Gui, self).__init__(*args, **kw)  

    def init_gui(self, sql_driver):
        self.sql_driver = sql_driver
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        margin = 20
        pos = (20,20)
        size = list(wx.DisplaySize())
        size[1] /= 2
        size[0] -= margin * 2
        size[1] -= margin
        self.editor = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE, pos=(20,20), size=size)
        self.editor.SetInsertionPoint(0)
        self.editor.SetFocus()
        self.editor.Bind(wx.EVT_KEY_UP, self.query)

        size2 = list(size)
        pos = list(size2)
        pos[0] = margin
        pos[1] += margin * 2
        size2[1] -= margin * 4
        self.grid = wx.ListCtrl(self, -1, pos=pos, size=size2, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.grid.Show(True)

        self.SetSize(wx.DisplaySize())
        self.SetTitle('sql client')
        self.SetBackgroundColour('black')
        self.Centre()
        self.Show(True)

    def query(self, e):
        if(e.GetKeyCode() == wx.WXK_RETURN):
            lastPos = self.editor.GetLastPosition()
            x, y = self.editor.PositionToXY(lastPos)
            query_text = self.editor.GetLineText(y-1)
            self.sql_driver.cur.execute(query_text)
            data = self.sql_driver.cur.fetchall()
            headers = self.sql_driver.get_csv_headers()
            if(headers == None):
                return
            headers = headers.split(',')
            col_num = 0
            for header in headers:
                print header
                self.grid.InsertColumn(col_num, header)
                col_num += 1
            if(len(data) > 0):
                for row in data:
                    pos = self.grid.InsertStringItem(col_num, str(row[0])) 
                    for col in range(1, len(row)):
                        self.grid.SetStringItem(pos, col, str(row[col]))

    def OnCloseWindow(self, e):
        self.sql_driver.close() 
        self.Destroy()
