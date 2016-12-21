#!/usr/bin/python3

user_id = '10045092'

import json
with open('/vagrant/tmp/osn-data/venue_categories2.json', 'r') as file:
  venue_categories = json.load(file)

with open('/vagrant/tmp/osn-data/checkin_tweet_target.json', 'r') as file:
  targets = json.load(file)

categories_count = {}
for venue_id, categories in venue_categories.items():
  for category in categories:
    count = 1
    if category in categories_count:
      count += categories_count[category]
    categories_count[category] = count

mapping = {}
with open('/vagrant/tmp/osn-data/user_4sqcheckins.csv', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  for row in csv_reader:
    if row[0] != user_id:
      continue
    venue_id = row[2]
    categories = venue_categories[venue_id]
    max_category = categories[0]
    max_count = categories_count[categories[0]]
    for category in categories:
      if categories_count[category] > max_count:
        max_count = categories_count[category]
        max_category = category
    mapping[row[1]] = {'category':max_category,'target':targets[row[1]]}

with open('/vagrant/tmp/osn-data/all.json', 'w') as file:
  json.dump(mapping, file, sort_keys = True)
