import wx
import noname
import engine

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar

class Runner(noname.MyFrame1):
    
    def __init__(self,parent):
        noname.MyFrame1.__init__(self,parent)

    def render(self, event):
        dpi = getDpi()
        w, h = self.m_panel2.GetSize()
        
        self.figure = Figure(figsize=(w/dpi,h/dpi))
        self.axes = self.figure.add_subplot(111)
        t,s = engine.get_input_plot()
        self.axes.plot(t,s)
        # Add it to the panel created in wxFormBuilder
        self.canvas = FigCanvas(self.m_panel2, wx.ID_ANY, self.figure) 

        return

def getDpi():
    px = float(wx.GetDisplaySize()[1])
    mm = float(wx.GetDisplaySizeMM()[1])
    return (px/(mm*0.0393701))

def main():
    app = wx.App()
    frame = Runner(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()