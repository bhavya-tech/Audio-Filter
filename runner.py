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
        self.figure = Figure()#figsize=(6, 4), dpi=100)
        self.axes = self.figure.add_subplot(111)
        t,s = engine.get_input_plot()
        self.axes.plot(t,s)
        # Add it to the panel created in wxFormBuilder
        self.canvas = FigCanvas(self.m_panel2, wx.ID_ANY, self.figure) 

        return

def main():
    app = wx.App()
    frame = Runner(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()