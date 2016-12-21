#!/usr/bin/python

user_id = '10045092'

import config
token = config.load_token('/vagrant/config/twitter.json')

tweets_hash = {}

tweet_ids_before = {}
tweet_ids_before[user_id] = {}

with open('/vagrant/tmp/osn-data/user_4sqcheckins.csv', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  for row in csv_reader:
    if row[0] != user_id:
      continue
    tweet_id = row[1]
#    if tweet_id in tweets_hash:
#      continue
    print(tweet_id)
    import api_twitter
    remote_tweets = api_twitter.user_tweets_before(token, user_id, tweet_id, 10)
    ids = []
    for tweet in remote_tweets:
      if tweet['id_str'] == tweet_id:
        continue
      tweets_hash[tweet['id_str']] = tweet
      # <a href=\"http://foursquare.com\" rel=\"nofollow\">Foursquare</a>
      source = tweet['source']
      import re
      m = re.search('^.*>(.*)<.*$', source)
      if m.group(1) != 'Foursquare':
        ids.append(tweet['id_str'])
    tweet_ids_before[user_id][tweet_id] = ids

tweets_before = []
keys = sorted(tweets_hash.keys())
for key in keys:
  tweets_before.append(tweets_hash[key])

import json
with open('/vagrant/tmp/osn-data/tweets_before.json', 'w') as file:
  json.dump(tweets_before, file, sort_keys=True)

with open('/vagrant/tmp/osn-data/tweet_ids_before.json', 'w') as file:
  json.dump(tweet_ids_before, file, sort_keys=True)
