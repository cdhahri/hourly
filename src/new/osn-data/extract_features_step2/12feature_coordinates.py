#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ids
import json
with open('../ids.json', 'r') as file:
  ids = json.load(file)

# categories
#with open('/vagrant/data/osn-data/category_coordinates_grouped.json', 'r') as file:
#  category_coordinates = json.load(file)

for user_id in ids:
  print(user_id)
  for percentage in percentages:
    print(percentage / 10)

    r = '../tweets_selected/{}/{}.json'.format(percentage, user_id)
    w = '../tweets_selected/features_step2/{}/{}coordinates.json'.format(percentage, user_id)

    with open(r, 'r') as file:
      tweets_hash = json.load(file)

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    feature = []
    for tweet in tweets:
      if tweet['coordinates'] is None:
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
