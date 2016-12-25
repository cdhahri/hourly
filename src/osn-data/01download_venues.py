#!/usr/bin/python3

import json
      
import config
token = config.load_token('/vagrant/config/foursquare.json')

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [106104712, 109223169, 11437162, 117093537, 11922222, 119436439, 13385712, 14098915, 14216821, 14229632, 14262523, 14701396, 14900774, 14901281, 15370082, 15412985, 15413409, 15479048, 15482020, 15507115, 15526160, 15844952]
  
for user_id in ids:
  user_id = str(user_id)

  print('user {}'.format(user_id))

  import os.path
  if os.path.exists('/vagrant/data/osn-data/venues/{}.json'.format(user_id)):
    continue

  print('user {} already processed'.format(user_id))

  venue_categories = {}

  with open('/vagrant/data/osn-data/user_4sqcheckins.csv', newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
      if row[0] != user_id:
        continue
      venue_id = row[2]
      if venue_id in venue_categories:
        continue
      print(venue_id)
      import api_foursquare
      remote_venue_category = api_foursquare.venue_category(token, venue_id)
      if remote_venue_category is not None:
        venue_categories[venue_id] = remote_venue_category

  with open('/vagrant/data/osn-data/venues/{}.json'.format(user_id), 'w') as file:
    json.dump(venue_categories, file, sort_keys = True)
