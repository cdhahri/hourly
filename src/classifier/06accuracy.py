#!/usr/bin/python3

import json
with open('./data/06features.json', 'r') as file:
  features = json.load(file)

with open('./data/07targets.json', 'r') as file:
  targets = json.load(file)

features_train = []
features_test = []
targets_train = []
targets_test = []

import random
for i in range(len(features)):
  if random.random() < 0.8:
    features_train.append(features[i])
    targets_train.append(targets[i])
  else:
    features_test.append(features[i])
    targets_test.append(targets[i])

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(features_train, targets_train)

targets_predicted = rfc.predict(features_test)

match = 0
for i in range(len(targets_test)):
  if targets_test[i] == targets_predicted[i]:
    match += 1

print(match / len(targets_test))
