import numpy as np
import backend


class Data:
    def __init__(self):
        return

    @classmethod
    def loadSound(cls, location):

        cls.fs, cls.input_sound = backend.getAudio(location)
        cls.time = np.arange(0, len(cls.input_sound)/cls.fs, 1/cls.fs)
        cls.fft = backend.furiour(cls.input_sound)

    @classmethod
    def load_power_graph(cls, input_sound):

        cls.power = backend.power_spectrum(cls.fft)
        cls.frequency = np.linspace(0, cls.fs/2, len(cls.power))
        cls.min = np.amin(cls.power)
        cls.max = np.amax(cls.power)
        cls.slope = (cls.max - cls.min) // 100
