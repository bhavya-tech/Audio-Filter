# import sympy  
from sympy import ifft 
  
# sequence  
seq = [15, 21, 13, 44] #our audio signal
  
# fft 
transform = ifft(seq) 
print ("Inverse FFT : ", transform) 