import numpy as np
from data import Data
from backend import export

data1= Data
data1.load_sound("./test_audio/audiocheck.net_sin_3Hz_-3dBFS_1s (1).wav")

ra = np.random.rand(len(data1.input_sound)) * max(data1.input_sound)
print(ra.shape)
temp = data1.input_sound + ra

print(temp)

export("noise_sound.wav",data1.fs,temp)
