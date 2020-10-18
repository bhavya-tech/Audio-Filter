import matplotlib as mpl
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

def get_input_plot():
    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(2 * np.pi * t)
    return t,s

