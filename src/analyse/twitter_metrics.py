#!/usr/bin/python

import json

import db

time_id_from = '2016-01-01-00'
time_id_to = '2016-12-31-23'

stat = {}
stat['_'] = {
  "00":0,
  "01":0,
  "02":0,
  "03":0,
  "04":0,
  "05":0,
  "06":0,
  "07":0,
  "08":0,
  "09":0,
  "10":0,
  "11":0,
  "12":0,
  "13":0,
  "14":0,
  "15":0,
  "16":0,
  "17":0,
  "18":0,
  "19":0,
  "20":0,
  "21":0,
  "22":0,
  "23":0
}
stat['statuses'] = {
  "00":0,
  "01":0,
  "02":0,
  "03":0,
  "04":0,
  "05":0,
  "06":0,
  "07":0,
  "08":0,
  "09":0,
  "10":0,
  "11":0,
  "12":0,
  "13":0,
  "14":0,
  "15":0,
  "16":0,
  "17":0,
  "18":0,
  "19":0,
  "20":0,
  "21":0,
  "22":0,
  "23":0
}
stat['favourites'] = {
  "00":0,
  "01":0,
  "02":0,
  "03":0,
  "04":0,
  "05":0,
  "06":0,
  "07":0,
  "08":0,
  "09":0,
  "10":0,
  "11":0,
  "12":0,
  "13":0,
  "14":0,
  "15":0,
  "16":0,
  "17":0,
  "18":0,
  "19":0,
  "20":0,
  "21":0,
  "22":0,
  "23":0
}
stat['friends'] = {
  "00":0,
  "01":0,
  "02":0,
  "03":0,
  "04":0,
  "05":0,
  "06":0,
  "07":0,
  "08":0,
  "09":0,
  "10":0,
  "11":0,
  "12":0,
  "13":0,
  "14":0,
  "15":0,
  "16":0,
  "17":0,
  "18":0,
  "19":0,
  "20":0,
  "21":0,
  "22":0,
  "23":0
}

activity = db.history_twitter__read('10449052', time_id_from, time_id_to)

i = 0
for _ in activity[1:]:
  prev = activity[i]
  i += 1
  curr = activity[i]

  import re
  m = re.search('^.{4}-.{2}-.{2}-(.{2})$', prev['time_id'])
  prev_hour = m.group(1)
  m = re.search('^.{4}-.{2}-.{2}-(.{2})$', curr['time_id'])
  curr_hour = int(m.group(1))
  if curr_hour == 0:
    curr_hour = 24

  if curr_hour-int(prev_hour) == 1:
    prev_profile = json.loads(prev['data'])['profile']
    curr_profile = json.loads(curr['data'])['profile']

    if curr_profile['statuses_count'] != prev_profile['statuses_count']:
      stat['_'][prev_hour] = stat['_'][prev_hour] + 1
      stat['statuses'][prev_hour] = stat['statuses'][prev_hour] + 1#(curr_profile['statuses_count'] - prev_profile['statuses_count'])

    if curr_profile['favourites_count'] != prev_profile['favourites_count']:
      stat['_'][prev_hour] = stat['_'][prev_hour] + 1
      stat['favourites'][prev_hour] = stat['favourites'][prev_hour] + 1#(curr_profile['favourites_count'] - prev_profile['favourites_count'])

    if curr_profile['friends_count'] != prev_profile['friends_count']:
      stat['_'][prev_hour] = stat['_'][prev_hour] + 1
      stat['friends'][prev_hour] = stat['friends'][prev_hour] + 1#(curr_profile['friends_count'] - prev_profile['friends_count'])

with open('/tmp/twitter_metrics.json', 'w') as file:
  json.dump(stat, file, sort_keys=True)
