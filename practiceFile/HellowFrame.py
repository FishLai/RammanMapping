'''
Created on 2018/7/31/

@author: quan_
'''
import wx

class HelloFrame(wx.Frame):
    '''
    classdocs
    '''


    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super(HelloFrame, self).__init__(*args, **kwargs)
        
        pnl = wx.Panel(self)
        
        st = wx.StaticText(pnl, label="Hello World!", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        
        self.makeMenuBar()
        
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
        
    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", "Help string show in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
    def OnExit(self, event):
        self.Close(True)
    def OnHello(self, event):
        wx.MessageBox("Hello again from wxPython")
    def OnAbout(self, event):
        wx.MessageBox("I don't have anything to say", "About Hello", wx.OK|wx.ICON_INFORMATION)
        
if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Hello World 2')
    frm.Show()
    app.MainLoop()