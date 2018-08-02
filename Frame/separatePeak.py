'''
2017/08/01
by FishLai
'''
import TemplateWx as tw
import wx

class SeparatePeak(tw.TemplateWx):
	ID_Button = 100
	
	def __init__(self, *args, **kws):
		super(SeparatePeak, self).__init__(*args, **kws)
		self.makeMenuBar()
		self.extendMenuBar()
		self.exButton()
	'''
	Buttons start
	'''	
#	def exButton(self):
		
	
	'''
	Menus start
	'''		
	def extendMenuBar(self):
		#insert 'File' item
		loadFileItem = wx.MenuItem(None, id = 111, text = "loadFile", helpString="feed me data file")
		self.Bind(wx.EVT_MENU, self.OnloadFile, loadFileItem)
		self.GetMenuBar().GetMenu(0).Insert(0, loadFileItem);
		
	def OnloadFile(self, event):
		wx.MessageBox("hi")
	


if __name__ == "__main__":
	app = wx.App()
	frm = SeparatePeak(None, title = "uncomplete_panelContent")
	frm.Show()
	app.MainLoop()
		