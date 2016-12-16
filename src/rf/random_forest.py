#!/usr/bin/python3

import json

with open('./data_tmp/features_train.json', 'r') as file:
  features_train = json.load(file)

with open('./data_tmp/classes_train.json', 'r') as file:
  classes_train = json.load(file)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(features_train, classes_train)

with open('./data_tmp/features_test.json', 'r') as file:
  features_test = json.load(file)

with open('./data_tmp/classes_test.json', 'r') as file:
  classes_test = json.load(file)

classes_predicted = rfc.predict(features_test)

x = 0
for i in range(len(classes_test)):
  if classes_test[i] == classes_predicted[i]:
    x += 1

print(x/len(classes_test))
