#!/usr/bin/python3

import json
with open('/vagrant/tmp/osn-data/all.json', 'r') as file:
  all = json.load(file)

i = 0
auto_inc = {}

categories = []
targets = []
for _, val in all.items():
  if val['category'] not in auto_inc:
    i += 1
    auto_inc[val['category']] = i
  categories.append(auto_inc[val['category']])
  targets.append(val['target'])

from scipy.stats import pearsonr
print(pearsonr(targets, categories))
