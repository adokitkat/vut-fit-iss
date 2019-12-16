import numpy as np
from scipy.io import wavfile
from scores import scores
from sys import argv
from pathlib import Path

q1path = Path('queries/q1.wav')
q2path = Path('queries/q2.wav')

q1freq, q1samples = wavfile.read(q1path)
q2freq, q2samples = wavfile.read(q2path)
# normalizacia
q1samples = q1samples / 2**15
q2samples = q2samples / 2**15

for i in range(1, len(argv)):
  path = Path(argv[i])
  freq, samples = wavfile.read(path)
  samples = samples / 2**15 

  s1, s2 = scores(samples, freq, q1samples, q1freq, q2samples, q2freq, 'gigantic', 'parking', return_score=True)

  s1data = []
  s2data = []

  wavfile.write('hits/gigantic_hit' + str(i) + '.wav', 16000, np.array(s1data))

  wavfile.write('hits/parking_hit' + str(i) + '.wav', 16000, np.array(s2data))

"""
  continuous1 = False
  con_n = 0
  s1data = []
  for n in s1:
    if n >= 0.5:
      con_n += 1
      s1data.append(n)
    if con_n >= 20:
      continuous1 = True
    else:
      if continuous1 == False:
        s1data = []
      con_n = 0

  continuous2 = False
  con_m = 0
  s2data = []
  for m in s2:
    if m >= 0.5:
      con_m += 1
      s2data.append(m)
    if con_m >= 20:
      continuous2 = True
    else:
      if continuous2 == False:
        s2data = []
      con_m = 0


  if continuous1 == True:
    wavfile.write('hits/gigantic_hit' + str(i) + '.wav', 16000, np.array(s1data))

  if continuous2 == True:
    wavfile.write('hits/parking_hit' + str(i) + '.wav', 16000, np.array(s2data))
"""