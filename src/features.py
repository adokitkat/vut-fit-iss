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

"""
b = [0.01, 0.01, 0.01, 0.01, 0.01]
a = [1, 0, 0, 0, 0]
# impulsni odezva
N_imp = 16
imp = [1, *np.zeros(N_imp-1)] # jednotkovy impuls
h = lfilter(b, a, imp)

# frekvencni charakteristika
w, H = freqz(b, a)

# nuly, poly
z, p, k = tf2zpk(b, a)

# stabilita
is_stable = (p.size == 0) or np.all(np.abs(p) < 1) 

# filtrace
sf = lfilter(b, a, samples)
f, t, sfgr = spectrogram(sf, freq)
sfgr_log = 10 * np.log10(sfgr+1e-20)
"""
def features(samples, frequency, pdf=False, figuresize=(8,2)):

  _, t, sgr_log = spctgrm(samples, frequency)

  sgr_filtered = np.add.reduceat(sgr_log, np.arange(0, len(sgr_log), 16), axis=0)

  fig = plt.figure(figsize=figuresize)
  plt.pcolormesh(t, np.arange(16), sgr_filtered)
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

features(samples, freq)