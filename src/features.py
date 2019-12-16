from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from pathlib import Path
from spectogram import spctgrm

path = Path(argv[1])
freq, samples = wavfile.read(path)
# normalizacia
samples = samples / 2**15

def features(samples, frequency, filter_sum=16, log_spectrum=256, pdf=False, figuresize=(8,2)):

  _, t, sgr_log = spctgrm(samples, frequency)

  sgr_filtered = np.add.reduceat(sgr_log, np.arange(0, len(sgr_log), filter_sum), axis=0)

  fig = plt.figure(figsize=figuresize)
  plt.pcolormesh(t, np.arange(log_spectrum/filter_sum), sgr_filtered)
  plt.gca().invert_yaxis()
  plt.gca().set_xlabel('t')
  plt.gca().set_ylabel('features')
  plt.gca().set_xlim(left=0)
  plt.tight_layout()
  if __name__ == '__main__':
    plt.savefig(path.stem + '_spectogram_filtred.pdf')
  elif pdf == True:
    return fig
  else:
    return sgr_filtered

if __name__ == '__main__':
  features(samples, freq)