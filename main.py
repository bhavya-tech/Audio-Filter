import numpy as np
from numpy import fft
from matplotlib import pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from scipy.io.wavfile import read
import sounddevice as sd
import soundfile as sf
    

#rate, audio = wavfile.read('sine.wav')

#audio = np.mean(audio, axis=1)

#N = audio.shape[0]
#L = N / rate

#print(f'Audio length: {L:.2f} seconds') #total time of the audio in seconds

#plt won't work in console, so need to be checked using GUI
#f, ax = plt.subplots() 
#ax.plot(np.arange(N) / rate, audio)
#ax.set_xlabel('Time [s]')
#ax.set_ylabel('Amplitude [unknown]');


'''
def polarToRectangular(radii, angles):
    return radii * np.exp(1j * angles)

def sortZip(x, y):
    order = np.argsort(x)
    xs = np.array(x)[order]
    ys = np.array(y)[order]
    return xs, ys

def frequencyGenerator(time, steps=None):
    𝛿 = time.max() - time.min()
    if steps is None:
        steps = np.diff(time).min()
    M = np.arange(1, steps + 1)
    return M / 𝛿, steps

def easyFourierTransform(time, signal, frequency=None, steps=None, sorted=False, uniform=False):
    if sorted:
        ts = time
        Xs = signal
    else:
        ts, Xs = sortZip(time, signal)
    
    if frequency is None:
        frequency, steps = frequencyGenerator(ts, steps)
    else:
        steps = frequency.shape[0]
    
    if uniform:
        N = signal.shape[0]
        amplitude = np.abs(scipy.fftpack.fft(signal)[:steps]) * 2.0 / N
    else:
        ft = frequency[:, np.newaxis]
        𝜃 = (ts - ts.min()) * 2 * np.pi * ft
        Y = polarToRectangular(Xs, 𝜃)[:, 1:] * np.diff(ts)
        amplitude = np.abs(Y.sum(axis=1))
    return frequency, amplitude

def easyFourierTransformThreshold(time, signal, frequency=None, steps=None, sorted=False, uniform=False):  
    threshold = 0.5
    if sorted:
        ts = time
        Xs = signal
    else:
        ts, Xs = sortZip(time, signal)
    
    if frequency is None:
        frequency, steps = frequencyGenerator(ts, steps)
    else:
        steps = frequency.shape[0]
    
    if uniform:
        N = signal.shape[0]
        amplitude = np.abs(scipy.fftpack.fft(signal)[:steps]) * 2.0 / N
    else:
        ft = frequency[:, np.newaxis]
        𝜃 = (ts - ts.min()) * 2 * np.pi * ft
        Y = polarToRectangular(Xs, 𝜃)[:, 1:] * np.diff(ts)
        amplitude = np.abs(Y.sum(axis=1))
        threshold = amplitude[np.argsort(amplitude)[-5:]].mean()
        for i in range(len(amplitude)):
            if amplitude[i] < threshold:
                amplitude[i] = 0
    return frequency, amplitude
'''

#a = read("sine.wav")
#np.array(a[1],dtype=float)
#print(a)
#rate, data = wavfile.read('sine.wav')
#print("HEy")
#fft_out = fft(data)
#print("helllllo")
#plt.plot(data, np.abs(fft_out))
#plt.show()
#print(data)
#print(np.abs(fft_out))
#def fft(data):
#fft_out = (np.fft.fftshift(data))
#fftout = np.fft.fft(data)
#    return fft_out
#print(fft_out)
#print(len(fft_out))
#print(fftout)
#print(len(fftout))
#plt.plot(data, np.abs(fft_out))
#plt.show()
#plt.plot(data, np.abs(fftout))
#plt.show()
# Load the data and calculate the time of each sample

samplerate, data = wavfile.read('eagle.wav')
times = np.arange(0,len(data)/samplerate,1/samplerate) # kav ek sec


# Make the plot
# You can tweak the figsize (width, height) in inches
plt.figure(figsize=(30, 4))
#plt.plot(times, data)
plt.plot(times, data)
plt.xlim(times[0], times[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
# You can set the format by changing the extension
# like .pdf, .svg, .eps
#plt.savefig('plot.png', dpi=100)
plt.show()
'''
code to plot filtered and unfiltered fft signals..thought this could be helpful ;)
subplot(2,1,1)
Y=fft(ch1,NFFT)/L;
plot(f,log10(abs(Y(1:NFFT/2+1))))
title('unfiltered')

subplot(2,1,2)
Y1=fft(y1,NFFT)/L;
plot(f,log10(abs(Y1(1:NFFT/2+1))))
title('filtered')
'''