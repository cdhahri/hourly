#!/usr/bin/python3

import json
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 1007531, 101496212, 1021239846, 102464379, 103114245, 103695733, 10449052, 104852013, 10521002, 106104712, 108944858, 109223169, 10929372, 109485267, 110808568, 111178547, 11126582, 111454868, 112490071, 112858627, 11312992, 113441429, 11346942, 11437162, 114978482, 115073079, 115138473, 115171979, 11661442, 117093537, 117562901, 117567036, 1177083624, 11778632, 117870724, 117987103, 118459389, 118474054, 11922222, 119436439, 119773854, 11987272, 119979433, 120268489, 12091872, 121768977, 122737979, 123059038, 1231465759, 1236198937, 123745496]  
    
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
