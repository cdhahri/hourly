#!/usr/bin/python

import json
with open('/vagrant/src/rf/data_tmp/pearson/target.json', 'r') as file:
  target = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/day.json', 'r') as file:
  day = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/week.json', 'r') as file:
  week = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/mentions_exist.json', 'r') as file:
  mentions = json.load(file)

with open('/vagrant/tmp/tweets.json', 'r') as file:
  tweets = json.load(file)

with open('/vagrant/tmp/osn-data/venue_categories2.json.pretty', 'r') as file:
  venues = json.load(file)

target_hash = {
  '4': '+',
  '0': '-'
}

day_hash = {
  '1': '1Mon',
  '2': '2Tue',
  '3': '3Wed',
  '4': '4Thu',
  '5': '5Fri',
  '6': '6Sat',
  '7': '7Sun'
}

week_hash = {
  '1': '1Weekday',
  '2': '2Weekend'
}

tags_hash = {
  'Airport': None,
  'Art': None,
  'Bar': None,
  'Beauty': None,
  'Cemetery': None,
  'Church': None,
  'Food': None,
  'Office': None,
  'Shopping': None,
  'Transportation': None,
}

day_stats = {
 '+/1Mon': 0,
 '+/2Tue': 0,
 '+/3Wed': 0,
 '+/4Thu': 0,
 '+/5Fri': 0,
 '+/6Sat': 0,
 '+/7Sun': 0,
 '-/1Mon': 0,
 '-/2Tue': 0,
 '-/3Wed': 0,
 '-/4Thu': 0,
 '-/5Fri': 0,
 '-/6Sat': 0,
 '-/7Sun': 0
}

week_stats = {
 '+/1Weekday': 0,
 '+/2Weekend': 0,
 '-/1Weekday': 0,
 '-/2Weekend': 0
}

mentions_stats = {
 '+/With Mention': 0,
 '+/Without Mention': 0,
 '-/With Mention': 0,
 '-/Without Mention': 0
}

tag_stats = {
  '+/Airport': 0,
  '-/Airport': 0,
  '+/Art': 0,
  '-/Art': 0,
  '+/Bar': 0,
  '-/Bar': 0,
  '+/Beauty': 0,
  '-/Beauty': 0,
  '+/Cemetery': 0,
  '-/Cemetery': 0,
  '+/Church': 0,
  '-/Church': 0,
  '+/Food': 0,
  '-/Food': 0,
  '+/Office': 0,
  '-/Office': 0,
  '+/Shopping': 0,
  '-/Shopping': 0,
  '+/Transportation': 0,
  '-/Transportation': 0,
}

for i in range(len(target)):
  key = target_hash[target[i]] + '/' + day_hash[str(day[i])]
  day_stats[key] = day_stats[key] + 1
  key = target_hash[target[i]] + '/' + week_hash[str(week[i])]
  week_stats[key] = week_stats[key] + 1
  key = target_hash[target[i]] + '/' + 'With Mention'
  if not mentions[i]:
    key = target_hash[target[i]] + '/' + 'Without Mention'
  mentions_stats[key] = mentions_stats[key] + 1

#print(json.dumps(day_stats, sort_keys=True))
#print(json.dumps(week_stats, sort_keys=True))
print(json.dumps(mentions_stats, sort_keys=True))

i = -1
for tweet in tweets:
  i += 1
  tweet_id = tweet['id_str']
  #
  user_id = '10045092'
  with open('/vagrant/tmp/osn-data/user_4sqcheckins.csv', newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
      if row[0] != user_id:
        continue
      if row[1] == tweet_id:
        venue_id = row[2]
        break
  #
  venue = venues[venue_id]
  category = venue[0]
  if category in tags_hash:
    key = target_hash[target[i]] + '/' + category
    tag_stats[key] = tag_stats[key] + 1

#print(json.dumps(tag_stats, sort_keys=True))
