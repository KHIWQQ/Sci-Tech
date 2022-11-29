import wx
import pymysql

class MyApp(wx.Frame):
    def __init__(self,parent,id,title):
        super(MyApp,self).__init__(parent,id,title,size=(600,400))
        self.basicGui()
    def basicGui(self):
        panel=wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        wx.StaticText(panel, -1, "คลังอาวุธ", pos=(280, 10))
        #box1
        hbox1 = wx.BoxSizer()
        #l1 = wx.StaticText(panel, -1, "คืนอาวุธ", pos=(470,55))
        #hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1 = wx.Button(panel, label="คืนอาวุธ", pos=(450,50),size=(70,40))
        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1.Bind(wx.EVT_BUTTON, self.Btn1)
        vbox.Add(hbox1)
        #box2
        hbox2 = wx.BoxSizer()
        #l2 = wx.StaticText(panel, -1, "เบิกอาวุธ", pos=(340, 55))
        #hbox2.Add(l2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2 = wx.Button(panel, label="เบิกอาวุธ", pos=(320, 50),size=(70,40))
        hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2.Bind(wx.EVT_BUTTON, self.Btn2)
        vbox.Add(hbox2)
        #box3
        hbox3 = wx.BoxSizer()
        #l3 = wx.StaticText(panel, -1, "แจ้งอาวุธชำรุด", pos=(325, 255))
        #hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t3 = wx.Button(panel, label="แจ้งอาวุธชำรุด", pos=(320, 250),size=(80, 50))
        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t3.Bind(wx.EVT_BUTTON, self.Btn3)
        vbox.Add(hbox3)
        #box4
        hbox4 = wx.BoxSizer()
        l4 = wx.StaticText(panel, -1, "ติดต่อเจ้าหน้าที่", pos=(20,300))
        hbox4.Add(l4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t4 = wx.TextCtrl(panel, value="นนร.เอกดนัย อินกาสุข เบอร์โทรศัพท์ 0863172022", style=wx.TE_READONLY, pos=(18,320), size=(240,20))
        hbox4.Add(self.t4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox4)
        #display
        wx.StaticBox()
        wx.StaticBox(panel, id=1, label="", pos=(20, 20), size=(200, 150), style=0)
        wx.StaticText(panel, -1, "ยอดเดิม", pos=(30, 40))
        wx.StaticText(panel, -1, "เบิก", pos=(30, 60))
        wx.StaticText(panel, -1, "คงเหลือ", pos=(30, 80))
        wx.StaticText(panel, -1, "ชำรุด", pos=(30, 100))
        wx.StaticText(panel, -1, "สูญหาย", pos=(30, 120))
        wx.StaticText(panel, -1, "251", pos=(140, 40))
        wx.StaticText(panel, -1, "กระบอก", pos=(170, 40))
        wx.StaticText(panel, -1, "กระบอก", pos=(170, 60))
        wx.StaticText(panel, -1, "กระบอก", pos=(170, 80))
        wx.StaticText(panel, -1, "กระบอก", pos=(170, 100))
        wx.StaticText(panel, -1, "กระบอก", pos=(170, 120))

        self.Centre()
        self.Show()
        self.Fit()

    def Btn1(self, dlg1):
        frame = wx.Frame(None, -1, 'win.py')
        dlg1 = wx.TextEntryDialog(frame, 'กรอกเลขปืน', 'คืนอาวุธ')
        dlg1.SetValue("")
        if dlg1.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % dlg1.GetValue())
            return dlg1.Destroy()

    def Btn2(self, dlg2):
        frame = wx.Frame(None, -1, 'aaa.py')
        dlg2 = wx.TextEntryDialog(frame, 'กรอกเลขปืน', 'เบิกอาวุธ')
        dlg2.SetValue("")
        if dlg2.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % dlg2.GetValue())
            return dlg2.Destroy()

    def Btn3(self, dlg3):
        frame = wx.Frame(None, -1, 'bbb.py')
        dlg3 = wx.TextEntryDialog(frame, 'กรอกเลขปืน', 'ชำรุด')
        dlg3.SetValue("")
        if dlg3.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % dlg3.GetValue())
            return dlg3.Destroy()

    def Btn4(self, dlg4):
        frame = wx.Frame(None, -1, 'ccc.py')
        dlg4 = wx.TextEntryDialog(frame, 'กรอกเลขปืน', 'ชำรุด')
        dlg4.SetValue("")
        if dlg4.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % dlg4.GetValue())
            return dlg4.Destroy()

if __name__=="__main__":
    app = wx.App()
    obj = MyApp(parent=None, id=-1, title="คลังอาวุธ")
    obj.Show()
    app.MainLoop()