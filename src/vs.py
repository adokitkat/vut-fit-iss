from scipy.io import wavfile
from signals import signal
from features import features
from scores import scores
import matplotlib.pyplot as plt
from sys import argv
from pathlib import Path
from matplotlib.backends.backend_pdf import PdfPages

path1 = Path(argv[1])

freq1, samples1 = wavfile.read(path1)

try:
  path2 = Path(argv[2])
  path3 = Path(argv[3])

except:
  path2 = Path('queries/q1.wav')
  path3 = Path('queries/q2.wav')

freq2, samples2 = wavfile.read(path2)
freq3, samples3 = wavfile.read(path3)
# normalizacia
samples1 = samples1 / 2**15
samples2 = samples2 / 2**15
samples3 = samples3 / 2**15

pdf = PdfPages(path1.stem + '_nas.pdf')

fig = signal(samples1, freq1, 'gigantic', 'parking')
pdf.savefig(fig)
fig.clf()

fig = features(samples1, freq1, pdf=True)
pdf.savefig(fig)
fig.clf()

fig = scores(samples1, freq1, samples2, freq2, samples3, freq3, 'gigantic', 'parking')
pdf.savefig(fig)
fig.clf()

pdf.close()