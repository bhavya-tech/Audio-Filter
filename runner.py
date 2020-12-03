import wx
import noname
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
            self.canvas1.plot(
                self.data.time, self.data.input_sound, linewidth=1)

            return

        else:
            self.canvas1.update_line(
                0, self.data.time, self.data.input_sound,   linewidth=1, draw=True)
            return

    def render_power(self, event):
        if wx.Event.GetEventType(event) == 10084 or wx.Event.GetEventType(event) == 10161:

            if(self.power_rendered):
                self.canvas2.update_line(
                    0, self.data.truncated_frequency, self.data.truncated_power, draw=True)
            else:
                self.canvas2 = PlotPanel(
                    self.m_panel3, size=(self.m_panel3.GetSize()))

                self.canvas2.plot(self.data.truncated_frequency, self.data.truncated_power, 'r')
                self.canvas2.oplot(self.data.truncated_frequency, np.full(
                    (len(self.data.truncated_frequency)), self.data.min))
                self.power_rendered = True

            return

        # For slider
        else:

            p = backend.get_cutoff_value(
                self.data.min, self.data.slope, self.m_slider1.GetValue())
            if(self.power_rendered):
                self.canvas2.update_line(1, self.data.truncated_frequency, np.full(
                    (len(self.data.truncated_frequency)), p), draw=True)

            else:
                self.canvas2 = PlotPanel(
                    self.m_panel3, size=(self.m_panel3.GetSize()))
                self.canvas2.plot(self.data.truncated_frequency, self.data.truncated_power, 'r')
                self.canvas2.oplot(self.data.truncated_frequency, np.full(
                    (len(self.data.truncated_frequency)), self.data.min))
                self.power_rendered = True

            return

    def render_output(self, event):

        if wx.Event.GetEventType(event) == 10084 or wx.Event.GetEventType(event) == 10161:

            self.m_panel4.Refresh()

            self.canvas3 = PlotPanel(
                self.m_panel4, size=(self.m_panel4.GetSize()))
            t, s = self.data.time, self.data.ifft
            self.canvas3.plot(t, s)

            return

        else:
            t, s = self.data.time, self.data.ifft

            self.canvas3.update_line(0, t, s, draw=True)
            return

    def loadAudio(self, event):
        ''' 
        Loads audio from path and calls render functions.\n
        wx event: 10161
        '''

        self.data.loadSound(location=self.m_filePicker1.GetPath())
        # print("sound loaded")
        self.data.load_power_graph()
        # print("fft done")
        # Fire screen refresh event
        self.render(event)
        self.render_power(event)
        self.render_output(event)

        return

    def slider_move(self, event):
        self.render_power(event)

        self.data.load_output(backend.get_cutoff_value(
            self.data.min, self.data.slope, self.m_slider1.GetValue()))

        self.render_output(event)


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
