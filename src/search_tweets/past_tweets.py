#!/usr/bin/python

import db
import json
import requests
import time

import api_twitter

import config
token = config.load_token('/vagrant/config/twitter.json')

screen_name = 'larryconlin'

#remote_tweet = api_twitter.user_tweets_max_id(token, screen_name, '1', None)
#if len(remote_tweet) == 0:
#  import sys
#  print('Exiting...')
#  sys.exit(1)

#max_id = remote_tweet[0]['id_str']
#tweets = {}
#tweets[remote_tweet[0]['id_str']] = remote_tweet[0]

#while True:
#  remote_tweets = api_twitter.user_tweets_max_id(token, screen_name, '200', max_id)
#  if len(remote_tweets) == 0:
#    break
#  for remote_tweet in remote_tweets:
#    if remote_tweet['id_str'] < max_id:
#      max_id = remote_tweet['id_str']
#    tweets[remote_tweet['id_str']] = remote_tweet

with open('/vagrant/tmp/tweets_{}.json'.format(screen_name), 'r') as file:
  hashed_tweets = json.load(file)

tweets = []
for key in sorted(hashed_tweets.keys()):
  tweets.append(hashed_tweets[key])

with open('/vagrant/tmp/tweets_{}2.json'.format(screen_name), 'w') as file:
  json.dump(tweets, file, sort_keys=True)
