#!/usr/bin/python

targets_hash = {
  0: '-1',
  2: '0',
  4: '1',
}

import json, requests

with open('/vagrant/src/new/osn-data/ids2.json', 'r') as file:
# with open('/vagrant/src/track/data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  with open('./targets/{}.json'.format(user_id), 'r') as file:
  # with open('/vagrant/src/track/data/tweets/targets/{}.json'.format(user_id), 'r') as file:
    targets = json.load(file)

  targets2 = []
  for target in targets:
    targets2.append(targets_hash[target])

  with open('/vagrant/src/new/osn-data/tweets_raw/features_step1/{}target.json'.format(user_id), 'w') as file:
  # with open('/vagrant/src/track/data/tweets/targets/{}target.json'.format(user_id), 'w') as file:
    json.dump(targets2, file)
