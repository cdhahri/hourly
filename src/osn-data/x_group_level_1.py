#!/usr/bin/python

import json
with open('/vagrant/data/osn-data/category_hierarchy.json', 'r') as file:
  hierarchy = json.load(file)
with open('/vagrant/data/osn-data/category_coordinates.json', 'r') as file:
  coordinates = json.load(file)

category_hash = {}
for category in coordinates.values():
  category_hash[category] = None

def loop_category(category, level_one):
  if category['name'] in category_hash:
    category_hash[category['name']] = level_one
  for sub_category in category['categories']:
    loop_category(sub_category, level_one)

for category in hierarchy:
  level_one = category['name']
  print(level_one)
  loop_category(category, level_one)

for ll, category in coordinates.items():
  coordinates[ll] = category_hash[category]

with open('/vagrant/data/osn-data/category_coordinates_grouped.json', 'w') as file:
  json.dump(coordinates, file, sort_keys=True)
