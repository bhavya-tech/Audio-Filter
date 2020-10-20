import numpy as np
import backend


class Data:
    def __init__(self):
        return

    @classmethod
    def loadSound(cls,location): 

        fs, cls.input_sound = backend.getAudio(location)
        cls.time = np.arange(0, len(cls.input_sound)/fs, 1/fs)
    
    @classmethod
    def load_power_graph(cls, input_sound):
        
        cls.power = backend.furiour(input_sound)
        cls.frequency = np.arange(len(cls.power))

    
        
