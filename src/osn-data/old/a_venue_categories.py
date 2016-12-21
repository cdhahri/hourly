#!/usr/bin/python3

user_id = '10045092'

import config
token = config.load_token('/vagrant/config/foursquare.json')

venue_categories = {}

with open('/vagrant/tmp/osn-data/user_4sqcheckins.csv', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  for row in csv_reader:
    if row[0] != user_id:
      continue
    venue_id = row[2]
    if venue_id in venue_categories:
      continue
    print(venue_id)
    while True:
      import api_foursquare
      remote_venue_category = api_foursquare.venue_category(token, venue_id)
      if remote_venue_category is not None:
        venue_categories[venue_id] = [remote_venue_category]
        break
    import json
    with open('/vagrant/tmp/osn-data/venue_categories.json', 'w') as file:
      json.dump(venue_categories, file, sort_keys = True)
