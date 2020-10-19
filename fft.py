# import sympy  
from sympy import fft 
  
# sequence  
seq = [15, 21, 13, 44] 
  
# fft 
transform = fft(seq) 
print (transform)