#!/usr/bin/python

import json
with open('./data_tmp/pearson/target.json', 'r') as file:
  target = json.load(file)

with open('./data_tmp/pearson/hashtags_exist.json', 'r') as file:
  hashtags = json.load(file)

with open('./data_tmp/pearson/mentions_exist.json', 'r') as file:
  mentions = json.load(file)

with open('./data_tmp/pearson/hashtags_or_mentions_exist.json', 'r') as file:
  hashtions = json.load(file)

with open('./data_tmp/pearson/media_exist.json', 'r') as file:
  media = json.load(file)

with open('./data_tmp/pearson/retweet_count.json', 'r') as file:
  retweet = json.load(file)

with open('./data_tmp/pearson/favorite_count.json', 'r') as file:
  favorite = json.load(file)

with open('./data_tmp/pearson/source.json', 'r') as file:
  source = json.load(file)

with open('./data_tmp/pearson/day.json', 'r') as file:
  day = json.load(file)

with open('./data_tmp/pearson/week.json', 'r') as file:
  week = json.load(file)

with open('./data_tmp/pearson/top_mentions.json', 'r') as file:
  top_mentions = json.load(file)

#with open('./data_tmp/pearson/place.json', 'r') as file:
#  place = json.load(file)

for i in range(len(target)):
  if target[i] == '0':
    target[i] = 0
  elif target[i] == '4':
    target[i] = 4

from scipy.stats import pearsonr

print('Hashtag (y/n)    : ' + str(pearsonr(target, hashtags)))
print('Mentions (y/n)   : ' + str(pearsonr(target, mentions)))
print('Hashtions (y/n)  : ' + str(pearsonr(target, hashtions)))
print('Media (y/n)      : ' + str(pearsonr(target, media)))
print('Retweet (count)  : ' + str(pearsonr(target, retweet)))
print('Favorites (count): ' + str(pearsonr(target, favorite)))
print('Source           : ' + str(pearsonr(target, source)))
print('Day              : ' + str(pearsonr(target, day)))
print('Week             : ' + str(pearsonr(target, week)))
for top_mention in top_mentions:
  print('Top mention      : ' + str(pearsonr(target, top_mention)))
#print('Place            : ' + str(pearsonr(target, place)))
