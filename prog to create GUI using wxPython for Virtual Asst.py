import wx   #for creating GUI Interface

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame. __init__ (self, None, pos=wx.DefaultPosition, size=wx.Size(450,100), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title='YOUR VIRTUAL ASSISTANT')

        panel=wx.Panel(self)      #initial panel setup
        my_sizer=wx.BoxSizer(wx.VERTICAL)   #size of the box
        lbl=wx.StaticText(panel,label = ' Hello, Im Your Digital Assistant..How can I Help You ? ')     #label to be displayed

        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,300))       #size of panel

        self.txt.SetFocus()  #to focus the text
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter) #combining the OnEnter func
        my_sizer.Add(self.txt,0,wx.ALL,5)

        panel.SetSizer(my_sizer)

        self.Show()

    def OnEnter(self, event):
        n=self.txt.GetValue()    #getting input from the user
        n=n.lower()              #converting into lowercase
        print ('IT WORKED !')


#run the app:

if __name__ == '__main__':
    app=wx.App(True)
    frame=MyFrame()
    app.MainLoop()
        
