#!/usr/bin/python

import json

def negative_count():
  targets_hash = {'0':0,'4':0}

  for target in targets:
    targets_hash[target] += 1

  print(targets_hash)

  return targets_hash['0']

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  with open('/vagrant/data/osn-data/features_step1/{}target.json'.format(user_id), 'r') as  file:
    targets = json.load(file)

  nc = negative_count()

  '''
  with open('/vagrant/data/osn-data/tweets/{}.json'.format(user_id), 'r') as file:
    all_ = json.load(file)

  selected_ = {}
  curr = -1
  so_far = 0
  for key in sorted(all_.keys()):
    curr += 1
    if targets[curr] == '0':
      selected_[key] = all_[key]
    if so_far == nc:
      continue
    if targets[curr] == '4':
      selected_[key] = all_[key]
      so_far += 1

  with open('/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id), 'w') as file:
    json.dump(selected_, file, sort_keys=True)
  '''
