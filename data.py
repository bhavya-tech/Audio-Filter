import numpy as np
import backend


class Data:
    def __init__(self):
        return

    @classmethod
    def loadSound(cls,location):
        print("in load sound")
        
        fs, cls.input_sound = backend.getAudio(location)
        print(fs)
        print(len(cls.input_sound))

        cls.time = np.arange(0, len(cls.input_sound)/fs, 1/fs)
