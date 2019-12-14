from scipy.io import wavfile
from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
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
Nc = 16
B = 256/Nc
samp = np.add.reduceat(samples, np.arange(0, len(samples), 16))

f, t, sfgr = spectrogram(samp, freq)
sfgr_log = 10 * np.log10(sfgr+1e-20)
plt.figure(figsize=(9,3))
plt.pcolormesh(t*16,f,sfgr_log)
plt.gca().set_title('Spektrogram vyfiltrovaného signálu')
plt.gca().set_xlabel('Čas [s]')
plt.gca().set_ylabel('Frekvence [Hz]')
cbar = plt.colorbar()
cbar.set_label('Spektralní hustota výkonu [dB]', rotation=270, labelpad=15)

plt.tight_layout()

plt.plot()
plt.savefig(path.stem + '_filtred.pdf')