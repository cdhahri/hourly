#!/usr/bin/python3

# token
import config
token = config.load_token('/vagrant/config/foursquare.json')

# ids
import json
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [10521002, 106104712, 109485267, 111178547, 113441429, 115138473, 11661442, 117567036, 11922222, 127828353, 1315286089, 133794989, 13385712, 142406505, 142802575, 14852278, 14900774, 15507115, 16090559, 16133557, 164266156, 16427456, 16830304, 16983823, 17289508, 17395031, 17997140, 18100365, 18107739, 18142778, 18853460, 19257498, 19388800, 199082056, 20022522, 20405425, 2084821, 212732867, 212991627, 21449222]

# categories
with open('/vagrant/data/osn-data/category_coordinates.json', 'r') as file:
  category_coordinates = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    if tweet is None or 'coordinates' not in tweet or tweet['coordinates'] is None:
      continue
    ll = tweet['coordinates']['coordinates']
    ll_string = json.dumps(ll, sort_keys=True)
    if ll_string not in category_coordinates:
      print('{}: fetching from 4sq'.format(ll_string))
      import api_foursquare
      venue = api_foursquare.venue(token, ll[1], ll[0])
      if venue is None:
        print('{}: either api error or no match on 4sq'.format(ll_string))
      else:
        if len(venue['categories']) == 0:
          print('{}: no category on 4sq'.format(ll_string))
        primary = None
        for category in venue['categories']:
          if 'primary' in category and category['primary'] == True:
            primary = category['name']
            break
        if primary is not None:
          category_coordinates[ll_string] = primary
          with open('/vagrant/data/osn-data/category_coordinates.json', 'w') as file:
            json.dump(category_coordinates, file, sort_keys=True)
