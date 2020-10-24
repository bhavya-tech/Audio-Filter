from scipy.io import wavfile
import numpy as np


def getAudio(location):
    samplerate, data = wavfile.read(location)
    return samplerate, data

# https://www.kite.com/python/answers/how-to-plot-a-power-spectrum-in-python
def power_spectrum(array):
    return (np.abs(array))

def furiour(array):
    return np.fft.rfft(array)

def get_cutoff_value(min, slope, p):
    return min + slope * p