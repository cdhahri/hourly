#!/usr/bin/python

user_id = '10045092'

import json
with open('/vagrant/src/rf/data_tmp/pearson/day.json', 'r') as file:
  day = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/week.json', 'r') as file:
  week = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/hashtags_exist.json', 'r') as file:
  hashtag = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/mentions_exist.json', 'r') as file:
  mentions = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/media_exist.json', 'r') as file:
  media = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/favorite_count.json', 'r') as file:
  favorite = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/source.json', 'r') as file:
  source = json.load(file)

#with open('/vagrant/src/rf/data_tmp_pearson/place.json', 'r') as file:
#  place = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/target.json', 'r') as file:
  target = json.load(file)

#mean w variance w momentum w entropy

mat = []
for i in range(len(target)):
  row = [day[i], week[i], hashtag[i], mentions[i], media[i], favorite[i], source[i], target[i]]
  mat.append(row)

with open('/vagrant/data/osn-data/matrices/{}.json'.format(user_id), 'w') as file:
  json.dump(mat, file)
