#!/usr/bin/python3

percentages = [10]

import json
import os.path

with open('./ids2.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = './tweets_selected/features_step3/{}/{}.json'.format(percentage, user_id)
    w = './tweets_selected/features_step3/aggregated/{}/{}.json'.format(percentage, user_id)

    with open(r, 'r') as file:
      byday = json.load(file)

    byday_aggregated = {}
    for key, day in byday.items():
      target = day['_target']
      pos = target.count('1')
      neg = target.count('-1')
      target = (pos) / (pos + neg)

      source_runkeeper_or_not = day['source_runkeeper_or_not']
      source_runkeeper_or_not = sum(source_runkeeper_or_not)
      runkeeper_distance = day['runkeeper_distance']
      runkeeper_distance = sum(runkeeper_distance)

      byday_aggregated[key] = {
        '_target':target,
        'source_runkeeper_or_not':source_runkeeper_or_not,
        'runkeeper_distance':runkeeper_distance,
      }

    with open(w, 'w') as file:
      json.dump(byday_aggregated, file, sort_keys=True)
