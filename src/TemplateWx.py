'''
Created on 2018年7月31日

@author: quan_
'''
import wx

class TemplateWx(wx.Frame):
    '''
    For All FishLai create window
    '''


    def __init__(self, *args, **kw):
        #ensure the parent's __init__ is called
        super(TemplateWx, self).__init__(*args, **kw)
        #create a panel
        #pnl = wx.Panel(self)
        
        #create a menu bar
        self.makeMenuBar()
        #and a status bar
        self.CreateStatusBar()
    def makeMenuBar(self):
        #Make a file menu
        fileMenu = wx.Menu()
        exitItem =fileMenu.Append(wx.ID_EXIT)
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File')
    
        #give the menu bar to the frame
        self.SetMenuBar(menuBar)
        #Associate a handler function with the EVT_MENU event for each of the menu item
        #That means that when that menu item is activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
    def OnExit(self, event):
        self.Close(True)
'''        
if __name__ == '__main__':
    app = wx.App()
    frm = TemplateWx(None, title='test')
    frm.Show()
    app.MainLoop()
'''