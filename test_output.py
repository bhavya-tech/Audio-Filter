""" Testing if output is same as input with thershold 0 """

from data import Data
import numpy as np
import matplotlib.pyplot as plt


data= Data
data.loadSound("./test_audio/audiocheck.net_sin_3Hz_-3dBFS_1s (1).wav")
data.load_power_graph()

temp = max(data.truncated_power)

print("\nFrequency - Power fraction\n")

for i in range(len(data.truncated_frequency)):
    print(str(data.truncated_frequency[i]) + " - " + str(data.truncated_power[i]/temp))

data.load_output(1e-7)
plt.plot(data.time,data.ifft)
plt.show()

print("\n")
