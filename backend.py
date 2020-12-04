from scipy.io import wavfile
import numpy as np


def getAudio(location):
    samplerate, data = wavfile.read(location)

    if len(data.shape) == 1:
        return samplerate, data

    return samplerate, data.sum(axis=1)/data.shape[0]


def power_spectrum(array):
    return (np.abs(array) ** 2)


def furiour(array):
    return np.fft.rfft(array)


def get_cutoff_value(min, slope, p):
    return min + slope * p


def get_last_non_zero_index(array):
    threshold = max(array)/100
    for i in reversed(range(len(array))):
        if array[i] > threshold:
            return i+1
    return 0


def export(filename, rate, data):
    wavfile.write(filename, rate, np.array(data, dtype="uint8"))
