import wx
class Window(wx.Frame):
    def __init__(self, parent, title):
        super(Window,self).__init__(parent, title=title,size=(1024, 800))
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL)

        # First graph
        hiPan = wx.Panel(panel)
        hiPan.SetBackgroundColour('#0000ee')
        vbox.Add(hiPan, wx.ID_ANY,wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)


        # Second graph
        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')
        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND| wx.ALL, border=10)
        panel.SetSizer(vbox)

        loPan = wx.Panel(panel)
        loPan.SetBackgroundColour('#ededed')
        vbox.Add(loPan, wx.ID_ANY, wx.EXPAND| wx.ALL, border=10)
        panel.SetSizer(vbox)
        

def main():

    app = wx.App()
    window = Window(None, title='Sizing')
    window.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()