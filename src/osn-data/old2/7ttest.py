#!/usr/bin/python

user_id = '10045092'

import json

import numpy
import scipy.stats

with open('/vagrant/data/osn-data/matrices/mean_{}.json'.format(user_id), 'r') as file:
  mean = json.load(file)

with open('/vagrant/data/osn-data/matrices/variance_{}.json'.format(user_id), 'r') as file:
  variance = json.load(file)

with open('/vagrant/data/osn-data/matrices/entropy_{}.json'.format(user_id), 'r') as file:
  entropy = json.load(file)

ttest_mean = []

mean = [mean, mean]
np_mean = numpy.array(mean)
for i in range(len(mean)-1):
  print(np_mean[i])
  print(scipy.stats.ttest_ind(np_mean[:,i],np_mean[:,(len(mean)-1)]))
  #print(scipy.stats.ttest_ind(np_mean[i],np_mean[(len(mean)-1)]))
