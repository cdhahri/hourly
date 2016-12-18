#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/top_mentions.json'

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

hi = min(3, len(user_mentions_occurences))

all = []
for top_user_mention in sorted(user_mentions_occurences.items(), key=lambda x: x[1], reverse=True)[:hi]:
  one = []
  for tweet in tweets:
#    if 'retweeted_status' in tweet:
#      continue
    entities = tweet['entities']
#    if 'user_mentions' not in entities:
#      continue
    user_mentions = entities['user_mentions']
    exist = False
    for user_mention in user_mentions:
      if top_user_mention[0] == user_mention['screen_name']:
        exist = True
        break
    one.append(exist)
  all.append(one)

with open(w, 'w') as file:
  json.dump(all, file)
