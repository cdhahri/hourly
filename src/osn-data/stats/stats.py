#!/usr/bin/python

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  with open('/vagrant/data/osn-data/features_step1/{}target.json'.format(user_id), 'r') as file:
    targets = json.load(file)
  negative = 0
  total = 0
  for target in targets:
    if target == '0':
      negative += 1
    total += 1
  ratio = negative/total 
  print(ratio)
