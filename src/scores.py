from scipy.io import wavfile
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from pathlib import Path
from features import features

path1 = Path(argv[1])

try:
  path2 = Path(argv[2])
  path3 = Path(argv[3])

except:
  path2 = Path('queries/q1.wav')
  path3 = Path('queries/q2.wav')

freq1, samples1 = wavfile.read(path1)
freq2, samples2 = wavfile.read(path2)
freq3, samples3 = wavfile.read(path3)
# normalizacia
samples1 = samples1 / 2**15
samples2 = samples2 / 2**15
samples3 = samples3 / 2**15

def scores(samples1, freq1, samples2, freq2, samples3, freq3, q1=None, q2=None):

  sentence = features(samples1, freq1)
  sentence = sentence.transpose()

  query1 = features(samples2, freq2)
  query1 = query1.transpose()

  query2 = features(samples3, freq3)
  query2 = query2.transpose()

  score = 0
  score_list1 = []
  
  for pp in range(sentence.shape[0]-query1.shape[0]):
    for n in range(query1.shape[0]):
      score += pearsonr(query1[n], sentence[pp+n])[0]
    score_list1.append(score/query1.shape[0])
    score = 0
  
  score = 0
  score_list2 = []

  for pp in range(sentence.shape[0]-query2.shape[0]):
    for n in range(query2.shape[0]):
      score += pearsonr(query2[n], sentence[pp+n])[0]
    score_list2.append(score/query2.shape[0])
    score = 0

  t1 = np.arange(len(score_list1))/100
  t2 = np.arange(len(score_list2))/100
  
  fig = plt.figure(figsize=(8,2))
  plt.plot(t1, score_list1, t2, score_list2)
  if q1 != None and q2 != None:
    plt.legend([q1, q2])
  else:
    plt.legend(['query1', 'query2'])
  plt.gca().set_xlabel('t')
  plt.gca().set_ylabel('scores')
  plt.gca().set_xlim(left=0)
  plt.gca().set_ylim(bottom=0)
  plt.tight_layout()
  if __name__ == '__main__':
    plt.savefig(path1.stem + '_score.pdf')
  else:
    return fig

scores(samples1, freq1, samples2, freq2, samples3, freq3)
