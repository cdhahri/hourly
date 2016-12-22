#!/usr/bin/python3

import json
with open('/vagrant/src/rf/data_tmp/train/features.json', 'r') as file:
  features = json.load(file)

with open('/vagrant/src/rf/data_tmp/train/target.json', 'r') as file:
  target = json.load(file)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(features, target)

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 1007531, 101496212, 1021239846, 102464379, 103114245, 103695733, 10449052, 104852013, 10521002, 106104712, 108944858, 109223169, 10929372, 109485267, 110808568, 111178547, 11126582, 111454868, 112490071, 112858627, 11312992, 113441429, 11346942, 11437162, 114978482, 115073079, 115138473, 115171979, 11661442, 117093537, 117562901, 117567036, 1177083624, 11778632, 117870724, 117987103, 118459389, 118474054, 11922222, 119436439, 119773854, 11987272, 119979433, 120268489, 12091872, 121768977, 122737979, 123059038, 1231465759, 1236198937, 123745496]

for user_id in ids:
  with open('/vagrant/data/osn-data/features_step1/{}features.json'.format(user_id), 'r') as file:
    test = json.load(file)

  target_predicted = rfc.predict(test)

  target_predicted_json = []
  for e in target_predicted:
    target_predicted_json.append(e)

  with open('/vagrant/data/osn-data/features_step1/{}target.json'.format(user_id), 'w') as file:
    json.dump(target_predicted_json, file)
