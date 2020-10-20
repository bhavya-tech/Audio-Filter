import numpy as np
import backend


class Data:
    def __init__(self):
        return

    @classmethod
    def loadSound(cls,location):
        fs, cls.input_sound = backend.getAudio(location)

        cls.time = np.arange(0, len(cls.input_sound)/fs, fs)
