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
        cls.min = 0
        cls.max = np.amax(cls.power)
        cls.slope = (cls.max - cls.min) / 100

        cls.truncated_power = cls.power[:backend.get_last_non_zero_index(
            cls.power)+1]
        cls.truncated_frequency = np.linspace(
            1, len(cls.truncated_power), len(cls.truncated_power))

    @classmethod
    def load_output(cls, threshold):

        ifft_freq = [0]

        for i in range(len(cls.power)):
            if cls.power[i] >= threshold:
                ifft_freq.append(cls.fft[i+1])
            else:
                ifft_freq.append(0)

        temp = np.array(ifft_freq)
        cls.ifft = np.fft.irfft(temp, n=len(cls.time))

    @classmethod
    def export(cls):
        backend.export("audio_filter_output.wav", cls.fs, cls.ifft)

    @classmethod
    def add_noise(cls):
        rand = np.random.rand(len(cls.input_sound)) * max(cls.input_sound)
        cls.input_sound = cls.input_sound + rand
        cls.fft = backend.furiour(cls.input_sound)
        cls.ifft = cls.input_sound
