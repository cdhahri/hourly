#!/usr/bin/python

import json

def negative_count():
  targets_hash = {'0':0,'4':0}

  for target in targets:
    targets_hash[target] += 1

  print(targets_hash['0']/(targets_hash['0']+targets_hash['4']))

  return targets_hash['0']

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  #with open('/vagrant/data/osn-data/tweets/{}.json'.format(user_id), 'r') as file:
  with open('/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id), 'r') as file:
    all_ = json.load(file)

  #with open('/vagrant/data/osn-data/features_step1/{}target_tweets.json'.format(user_id), 'r') as  file:
  try:
    with open('/vagrant/data/osn-data/features_step1/{}target_tweets_selected.json'.format(user_id), 'r') as  file:
      targets = json.load(file)
  except Exception:
    continue

  negative_count()

  '''
  keys = sorted(all_.keys())
  selected_ = {}
  i = -1
  for target in targets:
    i += 1
    if target == '0':
      selected_[keys[i]] = all_[keys[i]]
      if len(keys) > i+1:
        selected_[keys[i+1]] = all_[keys[i+1]]
      if i > 0:
        selected_[keys[i-1]] = all_[keys[i-1]]
#      if len(keys) > i+2:
#        selected_[keys[i+2]] = all_[keys[i+2]]
#      if i > 1:
#        selected_[keys[i-2]] = all_[keys[i-2]]
      
  with open('/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id), 'w') as file:
    json.dump(selected_, file, sort_keys=True)
  '''
