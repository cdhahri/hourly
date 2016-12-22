#!/usr/bin/python

import api_twitter
import json

import config
token = config.load_token('/vagrant/config/twitter.json')

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  user_id = str(user_id)

  import os.path
  if os.path.exists('/vagrant/data/osn-data/tweets/{}.json'.format(user_id)):
    continue

  tweets_hash = {}

  # checkin tweets
  with open('/vagrant/data/osn-data/user_4sqcheckins.csv', newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
      if row[0] != user_id:
        continue
      tweet_id = row[1]
      print(tweet_id)
      remote_tweet = api_twitter.tweet(token, tweet_id) 
      tweets_hash[tweet_id] = remote_tweet

  with open('/vagrant/data/osn-data/tweets/{}.json'.format(user_id), 'w') as file:
    json.dump(tweets_hash, file, sort_keys=True)

  # download past tweet
  remote_tweet = api_twitter.user_tweets_max_id_by_user_id(token, user_id, '1', None)
  if len(remote_tweet) != 1:
    print('{} failed'.format(user_id))
    continue

  remote_tweet = remote_tweet[0]
  max_id = remote_tweet['id_str']
  tweets_hash[remote_tweet['id_str']] = remote_tweet

  i = 0
  while True:
    i += 1
    if i > 100:
      break
    print(i)
    remote_tweets = api_twitter.user_tweets_max_id_by_user_id(token, user_id, '200', max_id)
    print(len(remote_tweets))
    for remote_tweet in remote_tweets:
      if remote_tweet['id_str'] < max_id:
        max_id = remote_tweet['id_str']
      tweets_hash[remote_tweet['id_str']] = remote_tweet

  with open('/vagrant/data/osn-data/tweets/{}.json'.format(user_id), 'w') as file:
    json.dump(tweets_hash, file, sort_keys=True)
