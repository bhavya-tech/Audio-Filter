import numpy as np
import backend


class Data:
    def __init__(self):
        return

    @classmethod
    def loadSound(cls, location):

        cls.fs, cls.input_sound = backend.getAudio(location)
        cls.ifft = cls.input_sound
        cls.time = np.arange(0, len(cls.input_sound)/cls.fs, 1/cls.fs)
        cls.fft = backend.furiour(cls.input_sound)

    @classmethod
    def load_power_graph(cls):

        cls.power = backend.power_spectrum(cls.fft)[1:]
        cls.frequency = np.linspace(0, cls.fs, len(cls.power))
        cls.min = np.amin(cls.power)
        cls.max = np.amax(cls.power)
        cls.slope = (cls.max - cls.min) / 100
        # print("Slope" + str(cls.slope))

    @classmethod
    def load_output(cls, threshold):

        # First element kept true to always take zero Hz freq
        filter_index = [True]

        for element in cls.power:
            if element >= threshold:
                filter_index.append(True)
            else:
                filter_index.append(False)
                
        temp = cls.fft[filter_index]
        cls.ifft = np.fft.irfft(temp, n=len(cls.time))
