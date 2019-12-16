import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from sys import argv
from pathlib import Path

path = Path(argv[1])

freq, samples = wavfile.read(path)
# normalizacia
samples = samples / 2**15

def signal(samples, frequency, q1=None, q2=None):
  
  t = np.arange(samples.size) / frequency
  fig = plt.figure(figsize=(8,2))
  plt.plot(t, samples)
  plt.gca().set_xlabel('t')
  plt.gca().set_ylabel('signal')
  plt.gca().set_xlim(left=0)
  if __name__ != '__main__':
    if q1 != None and q2 != None:
      plt.gca().set_title('"' + q1 + '" and "' + q2 + '" vs. ' + path.name)
    else:
      plt.gca().set_title('query1 and query2 vs. ' + path.name)
  plt.tight_layout()
  if __name__ == '__main__':
    plt.savefig(path.stem + '_signal.pdf')
  else:
    return fig

signal(samples, freq)