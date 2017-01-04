#!/usr/bin/python3

# ids
import json
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

#ids = [10521002, 106104712, 109485267, 111178547, 113441429, 115138473, 11661442, 117567036, 11922222, 127828353, 1315286089, 133794989, 13385712, 142406505, 142802575, 14852278, 14900774, 15507115, 16090559, 16133557, 164266156, 16427456, 16830304, 16983823, 17289508, 17395031, 17997140, 18100365, 18107739, 18142778, 18853460, 19257498, 19388800, 199082056, 20022522, 20405425, 2084821, 212732867, 212991627, 21449222]

# categories
#with open('/vagrant/data/osn-data/category_coordinates_grouped.json', 'r') as file:
#  category_coordinates = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step2/{}coordinates.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    if tweet is None or 'coordinates' not in tweet or tweet['coordinates'] is None:
      feature.append(None)
      continue
    ll = tweet['coordinates']['coordinates']
    ll_string = json.dumps(ll, sort_keys=True)
    '''
    #print('{}: processing...'.format(ll_string))
    category = None
    if ll_string in category_coordinates:
      category = category_coordinates[ll_string]
    feature.append(category)
    '''
    feature.append(ll_string)

  with open(w, 'w') as file:
    json.dump(feature, file)
