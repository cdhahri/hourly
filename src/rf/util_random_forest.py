#!/usr/bin/python3

import json

with open('./data_tmp/train/features.json', 'r') as file:
  features = json.load(file)

with open('./data_tmp/train/target.json', 'r') as file:
  target = json.load(file)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(features, target)

with open('./data_tmp/test/features.json', 'r') as file:
  test = json.load(file)

target_predicted = rfc.predict(test)

target_predicted_json = []
for e in target_predicted:
  target_predicted_json.append(e)

with open('./data_tmp/pearson/target.json', 'w') as file:
  json.dump(target_predicted_json, file)

#x = 0
#for i in range(len(classes_test)):
#  if classes_test[i] == classes_predicted[i]:
#    x += 1
#print(x/len(classes_test))
