#!/usr/bin/python3

percentages = [10]

import json
from datetime import datetime, timedelta
        
with open('./ids2.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    with open('./tweets_selected/features_step1/{}/{}target.json'.format(percentage, user_id), 'r') as file:
      targets = json.load(file)

    byday = {}
    for key in sorted(targets.keys()):
      if key not in byday:
        byday[key] = {
          '_target':[],
          'source_runkeeper_or_not':[],
          'runkeeper_distance':[],
          'runkeeper_activity':[],
        }
      byday[key]['_target'] = targets[key]

    with open('./tweets_selected/features_step2/{}/{}source_runkeeper_or_not.json'.format(percentage, user_id), 'r') as file:
      source_runkeeper_or_not = json.load(file)

    with open('./tweets_selected/features_step2/{}/{}runkeeper_distance.json'.format(percentage, user_id), 'r') as file:
      runkeeper_distance = json.load(file)

    with open('./tweets_selected/features_step2/{}/{}runkeeper_activity.json'.format(percentage, user_id), 'r') as file:
      runkeeper_activity = json.load(file)

    with open('./tweets_selected/{}/{}.json'.format(percentage, user_id), 'r') as file:
      tweets_hash = json.load(file)

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    i = -1
    for tweet in tweets:
      i += 1
      #Mon Sep 26 22:47:22 +0000 2016
      current_day = tweet['created_at']
      current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
      next_day_object = current_day_object + timedelta(days=1)
      key = '{0:%Y-%m-%d}'.format(next_day_object)

      if key not in byday:
        continue
      if source_runkeeper_or_not[i] == 0:
        continue
      byday[key]['source_runkeeper_or_not'].append(source_runkeeper_or_not[i])
      if runkeeper_distance[i] != -1.0:
        byday[key]['runkeeper_distance'].append(runkeeper_distance[i])
      if runkeeper_activity != 'NO':
        byday[key]['runkeeper_activity'].append(runkeeper_activity[i])

    keys_to_del = []
    for key in byday.keys():
      # if sum(byday[key]['source_runkeeper_or_not']) == 0:
      if len(byday[key]['runkeeper_distance']) == 0:
      # if len(byday[key]['runkeeper_activity']) == 0:
        keys_to_del.append(key)
    for key_to_del in keys_to_del:
      del byday[key_to_del]

    with open('./tweets_selected/features_step3/{}/{}.json'.format(percentage, user_id), 'w') as file:
      json.dump(byday, file, sort_keys=True)
