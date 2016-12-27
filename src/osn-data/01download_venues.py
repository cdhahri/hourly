#!/usr/bin/python3

import json
      
import config
token = config.load_token('/vagrant/config/foursquare.json')

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [109485267, 133794989, 14052274, 14852278, 15030109, 16133557, 16427456, 1652943942, 16754274, 16885564, 16983823, 17375954, 178183112, 18701575, 18853460, 19243536, 212732867, 21305689, 21668323, 218915630, 229191240, 231435258, 231850668, 234838196, 24390992, 25533464, 25772199, 26110977, 30331250, 31159879]

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
