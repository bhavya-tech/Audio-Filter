""" Testing if output is same as input with thershold 0 """

from data import Data
import numpy as np


data= Data
data.loadSound("./a.wav")
data.load_power_graph()
data.load_output(0)

temp = data.ifft
temp2 = data.input_sound

for i in range(len(temp)):
    if abs(temp[i] - temp2[i]) > 0.001:
        print("in: " + str(temp[i]))
        print("out: " + str(temp2[i]))