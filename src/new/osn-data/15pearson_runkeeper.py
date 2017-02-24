#!/usr/bin/python

import json
from scipy.stats import pearsonr
from scipy import stats

with open('./ids2.json', 'r') as file:
  ids = json.load(file)

source_pearsons = []

print(len(ids))
for user_id in ids:
  r = './tweets_selected/features_step3/aggregated/10/{}.json'.format(user_id)

  with open(r, 'r') as file:
    byday_aggregated = json.load(file)

  target = []
  source_count = []
  runkeeper_distance_count = []

  for key in sorted(byday_aggregated.keys()):
    target.append(byday_aggregated[key]['_target'])
    source_count.append(byday_aggregated[key]['source_runkeeper_or_not'])
    runkeeper_distance_count.append(byday_aggregated[key]['runkeeper_distance'])

  if len(target) < 2:
    # print(len(target))
    continue

  target = stats.zscore(target).tolist()

  # source_count = stats.zscore(source_count).tolist()
  # source_count_pearson = pearsonr(target, source_count)
  # for percentage in [0.3]:
  #   if abs(source_count_pearson[0]) > percentage and abs(source_count_pearson[1]) < 0.05:
  #     # print(len(target))
  #     print(user_id)
  #   else:
  #     a = 1
  #     # print(len(target))

  runkeeper_distance_count = stats.zscore(runkeeper_distance_count).tolist()
  runkeeper_distance_count_pearson = pearsonr(target, runkeeper_distance_count)
  for percentage in [0.2]:
    if abs(runkeeper_distance_count_pearson[0]) > percentage and abs(runkeeper_distance_count_pearson[1]) < 0.05:
      # print(len(target))
      print(user_id)
    else:
      a = 1
      # print(len(target))
