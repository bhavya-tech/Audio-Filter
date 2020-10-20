from matplotlib.backend_bases import Event
from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigCanvas, \
    NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure
import wx
from wx.core import wxEVT_SIZE
import noname
import engine
from wxmplot import PlotPanel
import numpy as np
import backend
import data

import matplotlib
matplotlib.use('WXAgg')


class Runner(noname.MyFrame1):

    power_rendered = False
    data = data.Data

    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)

    def render(self, event):

        if wx.Event.GetEventType(event) == 10084 or wx.Event.GetEventType(event) == 10161:

            self.m_panel2.Refresh()
            # Add it to the panel created in wxFormBuilder
            self.canvas1 = PlotPanel(
                self.m_panel2, size=(self.m_panel2.GetSize()))
            self.canvas1.plot(self.data.time, self.data.input_sound)

            return

        else:
            self.canvas1.update_line(
                0, self.data.time, self.data.input_sound, draw=True)
            self.render_power(event)

            return

    def render_power(self, event):
        t, s = engine.power_plot()
        if wx.Event.GetEventType(event) == 10084:

            min_p = int(np.amin(s))
            max_p = int(np.amax(s))

            self.m_slider1.SetMax(max_p)
            self.m_slider1.SetMin(min_p)
            self.m_slider1.SetValue(min_p)

            if(self.power_rendered):
                self.canvas2.update_line(0, t, s, draw=True)
            else:
                self.canvas2 = PlotPanel(
                    self.m_panel3, size=(self.m_panel3.GetSize()))
                self.canvas2.plot(t, s, 'r')
                self.canvas2.oplot(t, np.full((len(t)), min_p, 'g'))
                self.power_rendered = True

            return

        else:
            p = self.m_slider1.GetValue()
            self.canvas2.update_line(1, t, np.full((len(t)), p), draw=True)
            self.render_output(event)
            return

    def render_output(self, event):

        if wx.Event.GetEventType(event) == 10084:
            t, s = engine.output_plot()
            self.m_panel4.Refresh()

            self.canvas3 = PlotPanel(
                self.m_panel4, size=(self.m_panel4.GetSize()))
            self.canvas3.plot(t, s)

            return

        else:

            cutoff = self.m_slider1.GetValue()

            t, s = engine.output_plot(cutoff=cutoff)

            self.canvas3.update_line(0, t, s, draw=True)
            return

    def loadAudio(self, event):
        self.data.loadSound(location=self.m_filePicker1.GetPath())
        # Fire screen refresh event
        self.render(event)
        # fft
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
