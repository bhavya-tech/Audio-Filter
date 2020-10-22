import numpy as np
from numpy import fft
from matplotlib import pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from scipy.io.wavfile import read
import sounddevice as sd
import soundfile as sf
import data

d = data.Data

d.loadSound("eagle.wav")

# Make the plot
# You can tweak the figsize (width, height) in inches
plt.figure(figsize=(30, 4))
#plt.plot(times, data)
plt.plot(d.time, d.input_sound)

plt.xlim(d.time[0], d.time[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
# You can set the format by changing the extension
# like .pdf, .svg, .eps
#plt.savefig('plot.png', dpi=100)
plt.show()
'''
fourierTransform = np.fft.fft(dat)/len(dat)           # Normalize amplitude

fourierTransform = fourierTransform[range(int(len(dat)/2))] # Exclude sampling frequency
tpCount     = len(dat)

values      = np.arange(int(tpCount/2))

timePeriod  = tpCount/samplerate

frequencies = values/timePeriod

axis[3].set_title('Fourier transform depicting the frequency components')

 

axis[3].plot(frequencies, abs(fourierTransform))

axis[3].set_xlabel('Frequency')

axis[3].set_ylabel('Amplitude')

 

plt.show()
'''