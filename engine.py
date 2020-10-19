import numpy as np

def get_input_plot():
    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(2 * np.pi * t)
    return t,s

