#!/usr/bin/python

import json
from scipy.stats import pearsonr
from scipy import stats

with open('/vagrant/src/track/data/ids.json', 'r') as file:
  ids = json.load(file)

# steps_mean = []
# distance_mean = []
# targets_mean = []

for user_id in ids:
  r = './tweets_selected/features_step2/10/{}fitbit_steps.json'.format(user_id)
  with open(r, 'r') as file:
    steps = json.load(file)

  r = './tweets_selected/features_step2/10/{}fitbit_floors.json'.format(user_id)
  with open(r, 'r') as file:
    floors = json.load(file)

  r = './tweets_selected/features_step2/10/{}fitbit_distance.json'.format(user_id)
  with open(r, 'r') as file:
    distance = json.load(file)

  r = './tweets_selected/features_step1/10/{}target.json'.format(user_id)
  with open(r, 'r') as file:
    targets = json.load(file)

  steps_mean = []
  distance_mean = []
  targets_mean = []

  for day in steps.keys():
    if day not in targets:
      continue

    # steps
    steps_min = steps[day][0]
    steps_max = steps[day][-1]
    for char in ',.':
      steps_min = steps_min.replace(char, '')
      steps_max = steps_max.replace(char, '')
    try:
      steps_min = int(steps_min)
      steps_max = int(steps_max)
    except ValueError:
      continue

    # distance
    distance_min = distance[day][0]
    distance_max = distance[day][-1]
    for char in ',.':
      distance_min = distance_min.replace(char, '')
      distance_max = distance_max.replace(char, '')
    try:
      distance_min = int(distance_min)
      distance_max = int(distance_max)
    except ValueError:
      continue

    # targets
    steps_mean.append(steps_max - steps_min)
    distance_mean.append(distance_max - distance_min)
    pos = targets[day].count('1')
    neg = targets[day].count('-1')
    target_mean = (pos) / (pos + neg)
    targets_mean.append(target_mean)

  if len(targets_mean) == 0:
    continue

  steps_mean = stats.zscore(steps_mean).tolist()
  distance_mean = stats.zscore(distance_mean).tolist()
  targets_mean = stats.zscore(targets_mean).tolist()
  # print(pearsonr(targets_mean, steps_mean))
  print(pearsonr(targets_mean, distance_mean))
  # print(pearsonr(steps_mean, distance_mean))
