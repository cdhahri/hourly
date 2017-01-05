#!/usr/bin/python

import config
token = config.load_token('/vagrant/config/twitter.json')

import json
with open('./ids.json', 'r') as file:
  ids = json.load(file)

import api_twitter
count = 200
i = 0
for user_id in ids:
  i += 1
  print(i)
  tweets_hash = {}
  tweets = api_twitter.favorites(token, user_id, count, None)
  if not isinstance(tweets, list):
    print('{} not a list'.format(user_id))
    continue
  if len(tweets) == 0:
    print('{} empty list'.format(user_id))
    continue
  for remote_tweet in tweets:
    tweet_id = remote_tweet['id_str']
    created_at = remote_tweet['created_at']
    text = remote_tweet['text']
    tweets_hash[tweet_id] = {'tweet_id':tweet_id,'created_at':created_at,'text':text}
  max_id = min(tweets_hash.keys())
  for _ in range(4):
    tweets = api_twitter.favorites(token, user_id, count, max_id)
    if not isinstance(tweets, list):
      continue
    for remote_tweet in tweets:
      tweet_id = remote_tweet['id_str']
      created_at = remote_tweet['created_at']
      text = remote_tweet['text']
      tweets_hash[tweet_id] = {'tweet_id':tweet_id,'created_at':created_at,'text':text}
    max_id = min(tweets_hash.keys())
  with open('./favorites/{}.json'.format(user_id), 'w') as file:
    json.dump(tweets_hash, file, sort_keys=True)
