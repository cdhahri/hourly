#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import json
with open('./ids.json', 'r') as file:
  ids = json.load(file)

users = {}
for user_id in ids:
  user_id = str(user_id)
  if user_id not in users:
    users[user_id] = {'count':[],'rmse':[]}
  for i in ['1', '2', '3', '4']:
    with open('./plots/tweets_count_{}.json'.format(i), 'r') as file:
      count = json.load(file)
    with open('./plots/rmse_{}.json'.format(i), 'r') as file:
      rmse = json.load(file)
    if user_id in count and user_id in rmse:
      users[user_id]['count'].append(count[user_id])
      users[user_id]['rmse'].append(rmse[user_id])

#'''
for key, val in users.items():
  if len(val['count']) == 0:
    continue
  plt.plot(val['count'], val['rmse'], 'b--')
  plt.xlabel('tweet count')
  plt.ylabel('rmse')
  plt.savefig('./plots/1/{}.png'.format(key))
  plt.clf()
#'''
