from scipy.io import wavfile
import matplotlib.pyplot as plt
from sys import argv
from pathlib import Path
from spectogram import spctgrm

path = Path(argv[1])

freq, samples = wavfile.read(path)
# normalizacia
samples = samples / 2**15

def drawSpectogram(samples, frequency):

  t,f,sgr_log = spctgrm(samples, frequency)
  
  plt.figure(figsize=(9,3))
  plt.pcolormesh(t,f,sgr_log)
  plt.gca().set_title(path.name)
  plt.gca().set_xlabel('Čas [s]')
  plt.gca().set_ylabel('Frekvencia [Hz]')
  cbar = plt.colorbar()
  cbar.set_label('Spektralna hustota výkonu [dB]', rotation=270, labelpad=15)
  plt.tight_layout()
  plt.plot()
  plt.savefig(path.stem + '.pdf')

drawSpectogram(samples, freq)

