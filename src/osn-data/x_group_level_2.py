#!/usr/bin/python

import json
with open('/vagrant/data/osn-data/category_hierarchy.json', 'r') as file:
  hierarchy = json.load(file)
with open('/vagrant/data/osn-data/category_coordinates.json', 'r') as file:
  coordinates = json.load(file)

category_hash = {}
for category in coordinates.values():
  category_hash[category] = None

def loop_category(category, level):
  if level == 1:
    if category['name'] == 'Food':
      level = 'Food'
    else:
      level += 1
  else:
    if level == 2:
      level = category['name']
    if category['name'] in category_hash:
      category_hash[category['name']] = level

  for sub_category in category['categories']:
    loop_category(sub_category, level)

for category in hierarchy:
  loop_category(category, 1)

for ll, category in coordinates.items():
  if category_hash[category] == None:
    print(None)
  else:
    print(category_hash[category].encode('utf-8'))
  coordinates[ll] = category_hash[category]

with open('/vagrant/data/osn-data/category_coordinates_grouped.json', 'w') as file:
  json.dump(coordinates, file, sort_keys=True)
