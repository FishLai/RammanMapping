'''
2017/08/01
by FishLai
'''
import TemplateWx as tw
import wx
from wx.lib.sized_controls import border

ID_Btn = 100
ID_DefaultText = 101
class SeparatePeak(tw.TemplateWx):

	def __init__(self, *args, **kws):
		super(SeparatePeak, self).__init__(*args, **kws)
		self.makeMenuBar()
		self.extendMenuBar()
		self.Face()
	'''
	some guide word 
	'''
	def Face(self):
		pnl = wx.Panel(self)
		
		bsizer_title = wx.BoxSizer(wx.VERTICAL)
		#simple Title
		st_name = wx.StaticText(pnl, ID_DefaultText, label = "Try to divide peak", pos = (25, 25))
		font = st_name.GetFont()
		font.PointSize += 10
		font = font.Bold()
		st_name.SetFont(font)
		st_name.Style = wx.TE_LEFT				
		bsizer_title.Add(st_name, proportion = 0, flag =wx.EXPAND | wx.ALL, border = 5)
		
		bsizer_top = wx.BoxSizer(wx.HORIZONTAL)
		#tip for range set
		st_range = wx.StaticText(pnl, -1, "set range : ", style = wx.TE_LEFT)
		IB_lowerFloor = wx.TextCtrl(pnl, -1, "", style = wx.TE_LEFT)
		st_to = wx.StaticText(pnl, -1, " to ", style = wx.TE_LEFT)
		IB_ceiling = wx.TextCtrl(pnl, -1, "", style = wx.TE_LEFT)
		bsizer_top.Add(st_range, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5) 	
		bsizer_top.Add(IB_lowerFloor, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		bsizer_top.Add(st_to, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		bsizer_top.Add(IB_ceiling, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		
		
		
		bsizer_center = wx.BoxSizer(wx.HORIZONTAL)
		#tip text for load direction
		st_IBfile = wx.StaticText(pnl, ID_DefaultText, "File directory : ", style = wx.TE_LEFT)
		font_IBfile = st_IBfile.GetFont()
		font_IBfile = font_IBfile.Bold()
		bsizer_center.Add(st_IBfile, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		#input textBox for load direction
		inputBox_file = wx.TextCtrl(pnl, -1, value ="the data directory", style = wx.TE_LEFT)
		bsizer_center.Add(inputBox_file, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 5)
		#load file button
		btn_load = wx.Button(pnl, ID_Btn, "&folder...")
		btn_load.Bind(wx.EVT_BUTTON, self.OnloadDir)
		bsizer_center.Add(btn_load, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 5)
		
		bsizer_bottom = wx.BoxSizer(wx.HORIZONTAL)
		# Button for start convert
		btn_start = wx.Button(pnl, ID_Btn, "Divide")
		bsizer_bottom.Add(btn_start, proportion = 0, border = 5)
		

		
		bsizer_all = wx.BoxSizer(wx.VERTICAL)
		bsizer_all.Add(bsizer_title, proportion = 0, flag = wx.EXPAND | wx.ALL, border =5)
		bsizer_all.Add(bsizer_top, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		bsizer_all.Add(bsizer_center, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		bsizer_all.Add(bsizer_bottom, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		
		
		pnl.SetSizer(bsizer_all)

		
	
	'''
	Menus start
	'''		
	def extendMenuBar(self):
		#insert 'File' item
		loadFileItem = wx.MenuItem(None, id = 111, text = "loadFile", helpString="feed me data file")
		self.Bind(wx.EVT_MENU, self.OnloadDir, loadFileItem)
		self.GetMenuBar().GetMenu(0).Insert(0, loadFileItem);
		
	def OnloadDir(self, event):
		dlg = wx.DirDialog(self, "choose a directory:", style = wx.DD_DEFAULT_STYLE)
		
		if dlg.ShowModal() == wx.ID_OK:
			print("Your chose %s" % dlg.GetPath())
		dlg.Destroy()
	


if __name__ == "__main__":
	app = wx.App()
	frm = SeparatePeak(None, title = "uncomplete_panelContent", size = (1280, 720))
	frm.Show()
	app.MainLoop()
		