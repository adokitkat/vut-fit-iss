import numpy as np
from scipy.signal import spectrogram


def spctgrm(samples, frequency):

  samples = samples - np.mean(samples)
  wlen = 25e-3 * frequency
  wshift =  10e-3 * frequency
  woverlap = wlen - wshift
  win = np.hamming(wlen)
  f, t, sgr = spectrogram(samples, fs=frequency, window=win, noverlap=woverlap, nfft=512-1)  
  sgr_log = 10 * np.log10(sgr+1e-20)

  return f,t,sgr_log
