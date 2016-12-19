#!/usr/bin/python3

import json

data = ['./data_tmp/train.csv','./data_tmp/test.csv']

first_path = ['./data_tmp/train/count_all_capital.json','./data_tmp/test/count_all_capital.json']
rest_of_paths = [
 ['./data_tmp/train/count_dot.json','./data_tmp/test/count_dot.json'],
 ['./data_tmp/train/count_exclamation_mark.json','./data_tmp/test/count_exclamation_mark.json'],
 ['./data_tmp/train/count_negative_word.json','./data_tmp/test/count_negative_word.json'],
 ['./data_tmp/train/count_positive_word.json','./data_tmp/test/count_positive_word.json'],
 ['./data_tmp/train/count_question_mark.json','./data_tmp/test/count_question_mark.json'],
 ['./data_tmp/train/exist_more_than_three_dots.json','./data_tmp/test/exist_more_than_three_dots.json'],
 ['./data_tmp/train/exist_more_than_three_vowels.json','./data_tmp/test/exist_more_than_three_vowels.json']
]

feature_path = ['./data_tmp/train/features.json','./data_tmp/test/features.json']
target_path = ['./data_tmp/train/target.json','./data_tmp/test/target.json']

for i in range(2):
  # features
  features = []

  with open(first_path[i], 'r') as file:
    feature = json.load(file)
  for f in feature:
    features.append([f])

  for path in rest_of_paths:
    with open(path[i], 'r') as file:
      feature = json.load(file)
    j = -1
    for f in feature:
      j += 1
      features[j].append(f)

  with open(feature_path[i], 'w') as file:
    json.dump(features, file)

  # target
  target = []

  with open(data[i], newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
      target.append(row[0])
 
  with open(target_path[i], 'w') as file:
    json.dump(target, file)
