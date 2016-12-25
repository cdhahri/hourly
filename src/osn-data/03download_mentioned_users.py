#!/usr/bin/python

import api_twitter
import json

import config
token = config.load_token('/vagrant/config/twitter.json')

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [106104712, 109223169, 11437162, 117093537, 11922222, 119436439, 13385712, 14098915, 14216821, 14229632, 14262523, 14701396, 14900774, 14901281, 15370082, 15412985, 15413409, 15479048, 15482020, 15507115, 15526160, 15844952]

for user_id in ids:
  with open('/vagrant/data/osn-data/tweets/mentions/{}.json'.format(user_id), 'r') as file:
    mentions = json.load(file)

  for mention in mentions:
    import os.path
    if os.path.exists('/vagrant/data/osn-data/tweets/mentions/past_tweets/{}.json'.format(mention)):
      continue

    tweets_hash = {}

    remote_tweet = api_twitter.user_tweets_max_id_by_user_id(token, mention, '1', None)
    if len(remote_tweet) != 1:
      print('{} failed'.format(mention))
      continue

    remote_tweet = remote_tweet[0]
    max_id = remote_tweet['id_str']
    tweets_hash[remote_tweet['id_str']] = remote_tweet

    i = 0
    while True:
      i += 1
      if i > 10:
        break
      print(i)
      remote_tweets = api_twitter.user_tweets_max_id_by_user_id(token, mention, '200', max_id)
      print(len(remote_tweets))
      for remote_tweet in remote_tweets:
        if remote_tweet['id_str'] < max_id:
          max_id = remote_tweet['id_str']
        tweets_hash[remote_tweet['id_str']] = remote_tweet

    with open('/vagrant/data/osn-data/tweets/mentions/past_tweets/{}.json'.format(mention), 'w') as file:
      json.dump(tweets_hash, file, sort_keys=True)
