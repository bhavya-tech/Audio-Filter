import wx
import noname
import engine
from wxmplot import PlotPanel

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
        t,s = engine.get_input_plot()

        # Add it to the panel created in wxFormBuilder
        self.canvas1 = PlotPanel(self.m_panel2,size = (self.m_panel2.GetSize())).plot(t,s)

        return


# def getDpi():
    # px = float(wx.GetDisplaySize()[1])
    # mm = float(wx.GetDisplaySizeMM()[1])
    # return (px/(mm*0.0393701))

def main():
    app = wx.App()
    frame = Runner(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()