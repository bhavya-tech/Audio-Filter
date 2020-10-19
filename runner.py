import wx
from wx.core import wxEVT_SIZE
import noname
import engine
from wxmplot import PlotPanel
import numpy as np

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar

class Runner(noname.MyFrame1):
    power_rendered=False
    
    def __init__(self,parent):
        noname.MyFrame1.__init__(self,parent)

    def render(self, event):
        
        t,s = engine.get_input_plot()

        self.m_panel2.Refresh()
        # Add it to the panel created in wxFormBuilder
        self.canvas1 = PlotPanel(self.m_panel2,size = (self.m_panel2.GetSize())).plot(t,s)

        return
        
    
    def render_power(self,event):

        if wx.Event.GetEventType(event) == 10084:
            t,s = engine.power_plot()
            min_p = int(np.amin(s))
            max_p = int(np.amax(s))        

            self.m_slider1.SetMax(int(max_p))
            self.m_slider1.SetMin(int(min_p))

            if(self.power_rendered):
                self.canvas2.update_line(0,t,s,draw=True)
            else:
                self.canvas2 = PlotPanel(self.m_panel3,size = (self.m_panel3.GetSize()))
                self.canvas2.plot(t,s,'r')
                self.canvas2.oplot(t,np.full((len(t)), int((max_p+min_p)/2)), 'g')
                self.power_rendered = True
            
            return
        
        else:
            print("IN else")
            return

    def render_output(self,event):
        self.m_panel4.Refresh()

        t,s = engine.output_plot()

        self.canvas3 = PlotPanel(self.m_panel4,size = (self.m_panel4.GetSize())).plot(t,s)


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