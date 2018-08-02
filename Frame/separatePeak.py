'''
2017/08/01
by FishLai
'''
import TemplateWx as tw
import wx
from wx.lib.sized_controls import border

ID_Button = 100
ID_DefaultText = 101
class SeparatePeak(tw.TemplateWx):

	def __init__(self, *args, **kws):
		super(SeparatePeak, self).__init__(*args, **kws)
		
		self.makeMenuBar()
		self.extendMenuBar()
		self.exButton()
		self.Face()
	'''
	some guide word 
	'''
	def Face(self):
		pnl = wx.Panel(self)
		st_name = wx.StaticText(pnl, ID_DefaultText, label = "Try to divide peak", pos = (25, 25))
		font = st_name.GetFont()
		font.PointSize += 10
		font = font.Bold()
		st_name.SetFont(font)
		st_name.Style = wx.TE_LEFT
		
		st_IBfile = wx.StaticText(pnl, ID_DefaultText, "File direction : ", style = wx.TE_LEFT)
		font_IBfile = st_IBfile.GetFont().Bold()	
		inputBox_file = wx.TextCtrl(pnl, -1, value ="fuck", style = wx.TE_LEFT)
		
		
		bsizer_top = wx.BoxSizer(wx.VERTICAL)
		bsizer_center = wx.BoxSizer(wx.HORIZONTAL)
		bsizer_bottom = wx.BoxSizer(wx.HORIZONTAL)
		
		bsizer_top.Add(st_name, proportion = 0, flag =wx.EXPAND | wx.ALL, border = 5)
		bsizer_center.Add(st_IBfile, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		bsizer_center.Add(inputBox_file, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 5)
		
		bsizer_all = wx.BoxSizer(wx.VERTICAL)
		bsizer_all.Add(bsizer_top, proportion = 0, flag = wx.EXPAND | wx.ALL, border =5)
		bsizer_all.Add(bsizer_center, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		
		pnl.SetSizer(bsizer_all)
	'''
	Buttons start
	'''	
	def exButton(self):
		pass
	
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
	frm = SeparatePeak(None, title = "uncomplete_panelContent", size = (1280, 720))
	frm.Show()
	app.MainLoop()
		