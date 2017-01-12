#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import json
with open('./ids.json', 'r') as file:
  ids = json.load(file)

users = {}
for user_id in ids:
  print(user_id)
  user_id = str(user_id)
  if user_id not in users:
    users[user_id] = {'count':[],'rmse':[]}
  for i in ['1','2','3','4','5','6','7','8','9','10']:
    with open('../../weka/data/{}.grep'.format(i), 'r') as file:
      rmse = json.load(file)
    if user_id in rmse:
      users[user_id]['count'].append(i)
      users[user_id]['rmse'].append(rmse[user_id])

print('plot')
#'''
for key, val in users.items():
  print(key)
  if len(val['count']) == 0:
    continue
  plt.plot(val['count'], val['rmse'], 'b--')
  plt.xlabel('tweet count')
  plt.ylabel('rmse')
  plt.savefig('../../weka/data/plots/{}.png'.format(key))
  plt.clf()
#'''
