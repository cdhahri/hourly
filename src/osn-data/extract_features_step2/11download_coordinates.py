#!/usr/bin/python3

# token
import config
token = config.load_token('/vagrant/config/foursquare.json')

# ids
import json
with open('/vagrant/data/osn-data/.ids.json', 'r') as file:
  ids = json.load(file)

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
