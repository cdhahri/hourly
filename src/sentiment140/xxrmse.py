#!/usr/bin/python3

hashm = {
  "1": 1,
  "-1": -1,
}

import json
import numpy
from sklearn.metrics import mean_squared_error

with open('/vagrant/src/new/osn-data/ids.json', 'r') as file:
  ids = json.load(file)
  
rmse = []

for user_id in ids:
  y_true = []
  y_pred = []

  with open('/vagrant/src/new/osn-data/tweets_selected/features_step1/10/{}target.json'.format(user_id), 'r') as file:
    ground_truth = json.load(file)
  with open('/vagrant/src/new/osn-data/tweets_selected/features_step1/10/{}target_current.json'.format(user_id), 'r') as file:
    predicted = json.load(file)

  for key in ground_truth.keys():
    if key not in predicted:
      continue
    ground_truth_day = []
    for val in ground_truth[key]:
      ground_truth_day.append(hashm[val])
    predicted_day = []
    for val in predicted[key]:
      predicted_day.append(hashm[val])
    y_true.append(numpy.mean(ground_truth_day))
    y_pred.append(numpy.mean(predicted_day))

  if len(y_true) == 0:
    continue
  rmse.append(numpy.sqrt(mean_squared_error(y_true, y_pred)))

print(rmse)
print(numpy.mean(rmse))