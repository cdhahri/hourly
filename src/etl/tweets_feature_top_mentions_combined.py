#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/top_mentions_combined.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

user_mentions_occurences = {}
for tweet in tweets:
#  if 'retweeted_status' in tweet:
#    continue
  entities = tweet['entities']
  if 'user_mentions' not in entities:
    continue
  user_mentions = entities['user_mentions']
  for user_mention in user_mentions:
    screen_name = user_mention['screen_name']
    n = 1
    if screen_name in user_mentions_occurences:
      n += user_mentions_occurences[screen_name]
    user_mentions_occurences[screen_name] = n

hi = min(5, len(user_mentions_occurences))

top_user_mentions = sorted(user_mentions_occurences.items(), key=lambda x: x[1], reverse=True)[:hi]

all = []
for tweet in tweets:
  entities = tweet['entities']
  user_mentions = entities['user_mentions']
  exist = False
  for user_mention in user_mentions:
    if user_mention['screen_name'] in top_user_mentions[0]:
      exist = True
      break
  all.append(exist)

with open(w, 'w') as file:
  json.dump(all, file)
