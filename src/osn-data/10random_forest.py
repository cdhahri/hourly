#!/usr/bin/python3

import json
with open('/vagrant/src/rf/data_tmp/train/features.json', 'r') as file:
  features = json.load(file)

with open('/vagrant/src/rf/data_tmp/train/target.json', 'r') as file:
  target = json.load(file)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(features, target)

def process(r, w):
  with open(r, 'r') as file:
    test = json.load(file)

  if len(test) == 0:
    print('skipping {}'.format(r))
    return

  target_predicted = rfc.predict(test)

  target_predicted_json = []
  for e in target_predicted:
    target_predicted_json.append(e)

  with open(w, 'w') as file:
    json.dump(target_predicted_json, file)

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/features_step1/{}features.json'.format(user_id)
  #w = '/vagrant/data/osn-data/features_step1/{}target_tweets.json'.format(user_id)
  #w = '/vagrant/data/osn-data/features_step1/{}target_tweets_selected.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step1/{}target_tweets_next.json'.format(user_id)
  process(r, w)
