#!/usr/bin/python

import json
with open('./ids.json', 'r') as file:
  ids = json.load(file)

days = []
for user_id in ids:
  with open('./tweets_selected/features_step3/aggregated/10/{}.json'.format(user_id), 'r') as file:
    aggregated = json.load(file)
  days.append(len(aggregated.keys()))

print(sorted(days))
import numpy as np
a = np.array([days])
print(np.mean(a))
print(min(days))
print(max(days))

