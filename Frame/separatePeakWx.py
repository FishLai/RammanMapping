'''
2017/08/01
by FishLai
'''
import TemplateWx as tw
import wx
from wx.lib.sized_controls import border
import doIt

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
		self.pnl = wx.Panel(self)
		pnl = self.pnl
		
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
		self.IB_lowerFloor = wx.TextCtrl(pnl, -1, "", style = wx.TE_LEFT)
		IB_lowerFloor = self.IB_lowerFloor
		st_to = wx.StaticText(pnl, -1, " to ", style = wx.TE_LEFT)
		self.IB_ceiling = wx.TextCtrl(pnl, -1, "", style = wx.TE_LEFT)
		IB_ceiling = self.IB_ceiling
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
		self.inputBox_file = wx.TextCtrl(pnl, -1, value ="the data directory", style = wx.TE_LEFT)
		inputBox_file = self.inputBox_file
		bsizer_center.Add(inputBox_file, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 5)
		#load file button
		btn_load = wx.Button(pnl, ID_Btn, "&folder...")
		btn_load.Bind(wx.EVT_BUTTON, self.OnloadDir)
		bsizer_center.Add(btn_load, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 5)
		
		self.bsizer_bottom = wx.BoxSizer(wx.HORIZONTAL)
		bsizer_bottom = self.bsizer_bottom
		# Button for start convert
		btn_start = wx.Button(pnl, ID_Btn, "Divide")
		btn_start.Bind(wx.EVT_BUTTON, self.sendValue)
		bsizer_bottom.Add(btn_start, proportion = 0, border = 5)
		self.st_finish = wx.StaticText(self.pnl, -1, "", style = wx.TE_LEFT)
		st_finish = self.st_finish
		bsizer_bottom.Add(st_finish, proportion = 0, border = 5)
		

		
		self.bsizer_all = wx.BoxSizer(wx.VERTICAL)
		bsizer_all = self.bsizer_all
		bsizer_all.Add(bsizer_title, proportion = 0, flag = wx.EXPAND | wx.ALL, border =5)
		bsizer_all.Add(bsizer_top, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		bsizer_all.Add(bsizer_center, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		bsizer_all.Add(bsizer_bottom, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
		
		
		pnl.SetSizer(bsizer_all)

		
	
	'''
	event in menu
	'''		
	def extendMenuBar(self):
		#insert 'File' item
		loadFileItem = wx.MenuItem(None, id = 111, text = "loadFile", helpString="feed me data file")
		self.Bind(wx.EVT_MENU, self.OnloadDir, loadFileItem)
		self.GetMenuBar().GetMenu(0).Insert(0, loadFileItem);
	
	'''
	event in menu and face
	'''	
	def OnloadDir(self, event):
		dlg = wx.DirDialog(self, "choose a directory", style = wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			#print("Your chose %s" % dlg.GetPath())
			pth = dlg.GetPath()
			self.inputBox_file.SetValue(pth)					
		dlg.Destroy()
	'''
	event in face
	'''
	def sendValue(self, event):
		self.st_finish.SetLabel("")
		wnFloor = int(self.IB_lowerFloor.GetValue())
		wnCeiling = int(self.IB_ceiling.GetValue())
		directory = self.inputBox_file.GetValue()
		params = [wnFloor, wnCeiling, directory]
		print(params)
		doIt.doIt(params)
		
		self.st_finish.SetLabel("finished divide data")
		return True
		


if __name__ == "__main__":
	app = wx.App()
	frm = SeparatePeak(None, title = "divideData.ver1", size = (1280, 720))
	frm.Show()
	app.MainLoop()
		