#!/usr/bin/python

import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#with open('./ids.json', 'r') as file:
#  ids = json.load(file)

with open('./tweets_selected/features_step3/aggregated/weka.json', 'r') as file:
  weka = json.load(file)

for id_user, rez in weka.items():
  with open('./tweets_selected/features_step3/aggregated/{}.json'.format(id_user), 'r') as file:
    targets= json.load(file)

  tomorrow = weka[id_user]['actual']
  predicted = weka[id_user]['predicted']

  line_tomorrow, = plt.plot(tomorrow, 'b-', label='Actual')
  line_predicted, = plt.plot(predicted, 'r-', label='Predicted')
  #line_predicted, = plt.plot(tomorrow, predicted, 'bs')
  #baseline, = plt.plot([0, 1], [0, 1], 'b--')
  
  plt.legend(handles=[line_tomorrow, line_predicted])
  plt.xlabel('actual')
  plt.ylabel('predicted')
  #plt.xlim([-0.1,1.1])
  plt.ylim([-0.1,1.1])
  plt.savefig('./plots/1/{}_1.png'.format(id_user))
  plt.clf()
