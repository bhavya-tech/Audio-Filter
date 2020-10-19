import numpy as np

def get_input_plot():
    t = np.arange(0.0, 10.0, 0.01)
    s = np.sin(2 * np.pi * t)
    return t,s

def power_plot():
    t = np.arange(0.0, 7.0, 0.01)
    s = np.sin(2 * np.pi * t)
    return t,s

def output_plot():
    t = np.arange(0.0, 4.0, 0.01)
    s = np.sin(2 * np.pi * t)
    return t,s

