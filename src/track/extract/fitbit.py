#!/usr/bin/python

import json

import db

twitter_ids = db.user__read__all_fitbit()
with open('../data/ids.json', 'w') as file:
  json.dump(twitter_ids, file, sort_keys=True)

for twitter_id in twitter_ids:
  '''
  # tweets
  tweet_ids = db.history_twitter__read__all_tweet_ids(twitter_id)
  print(tweet_ids)
  tweets = {}
  for tweet_id in tweet_ids:
    tweet = db.tweet__read(tweet_id)
    tweets[tweet['id_str']] = tweet
    with open('../data/tweets/{}.json'.format(twitter_id), 'w') as file:
      json.dump(tweets, file, sort_keys=True)
  '''
  # fitbit
  fitbit_activities = db.history_fitbit__read__all(twitter_id)
  with open('../data/fitbit/{}.json'.format(twitter_id), 'w') as file:
    json.dump(fitbit_activities, file, sort_keys=True)
