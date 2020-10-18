import wx
def main():
    app = wx.App()
    window = wx.Frame(None, title = "wxPython Frame", size = (1024,800)) 
    panel = wx.Panel(window) 
    label = wx.StaticText(panel, label = "Hello World", pos = (100,50)) 
    window.Show(True) 
    app.MainLoop()

if __name__ == '__main__':
    main()