from scipy.io import wavfile
import numpy as np


def getAudio(location):
    samplerate, data = wavfile.read(location)
    return samplerate, data

def furiour(array):
    return np.fft.fft(array)