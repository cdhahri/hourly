#!/usr/bin/python3

import json

# features
features = []

path = './data_tmp/count_all_capital.json'
with open(path, 'r') as file:
  feature = json.load(file)
for f in feature:
  features.append([f])

paths = [
 './data_tmp/count_dot.json',
 './data_tmp/count_exclamation_mark.json',
 './data_tmp/count_question_mark.json',
 './data_tmp/exist_more_than_three_dots.json',
 './data_tmp/exist_more_than_three_vowels.json',
 './data_tmp/exist_negative_word.json',
 './data_tmp/exist_positive_word.json'
]
for path in paths:
  with open(path, 'r') as file:
    feature = json.load(file)
  i = -1
  for f in feature:
    i += 1
    features[i].append(f)

with open('./data_tmp/features.json', 'w') as file:
  json.dump(features, file)

# class
path = './training.1600000.processed.noemoticon.csv'
with open(path, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  out = []
  for row in csv_reader:
    out.append(row[0])
 
with open('./data_tmp/class.json', 'w') as file:
  json.dump(out, file)

features_train = []
classes_train = []
for i in range(500000):
  features_train.append(features[i])
  classes_train.append(out[i])
for i in range(500000):
  features_train.append(features[800000+i])
  classes_train.append(out[800000+i])

features_test = []
classes_test = []
for i in range(300000):
  features_test.append(features[500000+i])
  classes_test.append(out[500000+i])
for i in range(300000):
  features_test.append(features[800000+500000+i])
  classes_test.append(out[800000+500000+i])


with open('./data_tmp/features_train.json', 'w') as file:
  json.dump(features_train, file)

with open('./data_tmp/classes_train.json', 'w') as file:
  json.dump(classes_train, file)

with open('./data_tmp/features_test.json', 'w') as file:
  json.dump(features_test, file)

with open('./data_tmp/classes_test.json', 'w') as file:
  json.dump(classes_test, file)
