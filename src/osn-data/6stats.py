#!/usr/bin/python

user_id = '10045092'

import json
with open('/vagrant/data/osn-data/matrices/{}.json'.format(user_id), 'r') as file:
  matrix = json.load(file)

# mean w variance w momentum w entropy

import numpy
import scipy.stats

mean = numpy.mean(matrix, axis=0)
variance = numpy.var(matrix, axis=0)

np_matrix = numpy.array(matrix)
entropy = []
for i in range(len(matrix[0])):
  occu = {}
  for e in np_matrix[:,i]:
    if str(e) in occu:
      occu[str(e)] = occu[str(e)] + 1
    else:
      occu[str(e)] = 1
  count = occu.values()
  prob = []
  for c in count:
    prob.append(c/sum(count))
  entropy.append(scipy.stats.entropy(prob))

#import numpy.ndarray

with open('/vagrant/data/osn-data/matrices/mean_{}.json'.format(user_id), 'w') as file:
  json.dump(mean.tolist(), file)

with open('/vagrant/data/osn-data/matrices/variance_{}.json'.format(user_id), 'w') as file:
  json.dump(variance.tolist(), file)

with open('/vagrant/data/osn-data/matrices/entropy_{}.json'.format(user_id), 'w') as file:
  json.dump(entropy, file)

print(mean)
print(variance)
print(entropy)

#np_mean = numpy.array(mean)
#for i in range(len(mean)-1):
#  print(np_mean[:,i])
#  print(np_mean[:,(len(mean)-1)])
#  print(scipy.stats.ttest_ind(np_mean[:,i],np_mean[:,(len(mean)-1)]))
  #print(scipy.stats.ttest_ind([1,2],[3,4]))
