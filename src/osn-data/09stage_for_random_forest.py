#!/usr/bin/python3

import json
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

def process(data, first_path, rest_of_paths, feature_path):
  features = []

  with open(first_path, 'r') as file:
    feature = json.load(file)
  for f in feature:
    features.append([f])

  for path in rest_of_paths:
    with open(path, 'r') as file:
      feature = json.load(file)
    j = -1
    for f in feature:
      j += 1
      features[j].append(f)

  with open(feature_path, 'w') as file:
    json.dump(features, file)

for user_id in ids:
  data = '/vagrant/data/osn-data/tweets/csv/{}.csv'.format(user_id)

  first_path = '/vagrant/data/osn-data/features_step1/{}count_all_capital.json'.format(user_id)

  rest_of_paths = [
   '/vagrant/data/osn-data/features_step1/{}count_exclamation_mark.json'.format(user_id),
   '/vagrant/data/osn-data/features_step1/{}count_question_mark.json'.format(user_id),
   '/vagrant/data/osn-data/features_step1/{}count_negative_word.json'.format(user_id),
   '/vagrant/data/osn-data/features_step1/{}count_positive_word.json'.format(user_id),
   '/vagrant/data/osn-data/features_step1/{}exist_more_than_three_dots.json'.format(user_id),
   '/vagrant/data/osn-data/features_step1/{}exist_more_than_three_vowels.json'.format(user_id),
  ]

  feature_path = '/vagrant/data/osn-data/features_step1/{}features.json'.format(user_id)
  process(data, first_path, rest_of_paths, feature_path)
