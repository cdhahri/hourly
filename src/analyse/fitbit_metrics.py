#!/usr/bin/python

import json

import db

time_id_from = '2016-01-01-00'
time_id_to = '2016-12-31-23'

stat = {}
stat['distance'] = {
  "00":0.0,
  "01":0.0,
  "02":0.0,
  "03":0.0,
  "04":0.0,
  "05":0.0,
  "06":0.0,
  "07":0.0,
  "08":0.0,
  "09":0.0,
  "10":0.0,
  "11":0.0,
  "12":0.0,
  "13":0.0,
  "14":0.0,
  "15":0.0,
  "16":0.0,
  "17":0.0,
  "18":0.0,
  "19":0.0,
  "20":0.0,
  "21":0.0,
  "22":0.0,
  "23":0.0
}
stat['steps'] = {
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
stat['floors'] = {
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

activity = db.history_fitbit__read('10449052', time_id_from, time_id_to)

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
    prev_profile = json.loads(prev['data'])
    curr_profile = json.loads(curr['data'])

    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    
    prev_distance = locale.atof(prev_profile['lifetime_distance'])
    curr_distance = locale.atof(curr_profile['lifetime_distance'])
    prev_steps = locale.atoi(prev_profile['lifetime_steps'])
    curr_steps = locale.atoi(curr_profile['lifetime_steps'])
    prev_floors = locale.atoi(prev_profile['lifetime_floors'])
    curr_floors = locale.atoi(curr_profile['lifetime_floors'])

    stat['distance'][prev_hour] = stat['distance'][prev_hour] + (curr_distance-prev_distance)
    stat['steps'][prev_hour] = stat['steps'][prev_hour] + (curr_steps-prev_steps)
    stat['floors'][prev_hour] = stat['floors'][prev_hour] + (curr_floors-prev_floors)

    if curr_distance-prev_distance != 0.0:
      stat['_'][prev_hour] = stat['_'][prev_hour] + 1
    if curr_steps-prev_steps != 0:
      stat['_'][prev_hour] = stat['_'][prev_hour] + 1
    if curr_floors-prev_floors != 0:
      stat['_'][prev_hour] = stat['_'][prev_hour] + 1

with open('/tmp/fitbit_metrics.json', 'w') as file:
  json.dump(stat, file, sort_keys=True)
