import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from scipy.io import wavfile
from sys import argv
from pathlib import Path

path = Path(argv[1])
freq, samples = wavfile.read(path)
# normalizacia
samples = samples / 2**15

def spctgrm(samples, frequency):

  samples = samples - np.mean(samples)
  wlen = 25e-3 * frequency
  wshift =  10e-3 * frequency
  woverlap = wlen - wshift
  win = np.hamming(wlen)
  f, t, sgr = spectrogram(samples, fs=frequency, window=win, noverlap=woverlap, nfft=512-1)  
  sgr_log = 10 * np.log10(sgr+1e-20)

  return f,t,sgr_log

def drawSpectogram(samples, frequency):

  f, t, sgr_log = spctgrm(samples, frequency) 

  plt.figure(figsize=(8,3))
  plt.pcolormesh(t,f,sgr_log)
  plt.gca().set_title(path.name)
  plt.gca().set_xlabel('Čas [s]')
  plt.gca().set_ylabel('Frekvencia [Hz]')
  #cbar = plt.colorbar()
  #cbar.set_label('Spektralna hustota výkonu [dB]', rotation=270, labelpad=15)
  plt.tight_layout()
  plt.plot()
  plt.savefig(path.stem + '_spectogram.pdf')

if __name__ == '__main__':
  drawSpectogram(samples, freq)