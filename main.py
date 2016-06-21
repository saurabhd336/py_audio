import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import pylab
from scipy.io import wavfile

N = 1000
sampfreq, snd = wavfile.read('sample3.wav')

yf = scipy.fft(snd[0:1000000])

yf[0:5000] = 0;

new_sound = scipy.ifft(yf)

new_sound = new_sound.astype('int16')

wavfile.write('new_sound.wav', 44100, new_sound)

