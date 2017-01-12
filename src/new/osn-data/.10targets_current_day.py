#!/usr/bin/python3

import json
from datetime import datetime, timedelta
        
def process(r, targets_path, selected_days_path, w):
  with open(r, 'r') as file:
    tweets = json.load(file)

  with open(targets_path, 'r') as file:
    targets = json.load(file)

  with open(selected_days_path, 'r') as file:
    selected_days = json.load(file)

  sources = {
    '<a href="http://foursquare.com" rel="nofollow">Foursquare</a>':None,
    '<a href="http://instagram.com" rel="nofollow">Instagram</a>':None
  }

  out = {}
  i = -1
  for key in sorted(tweets.keys()):
    i += 1
    if tweets[key]['source'] in sources:
      continue
    # Tue Sep 27 01:58:41 +0000 2016
    current_day = tweets[key]['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    next_day_object = current_day_object + timedelta(days=1)
    next_day = '{0:%Y-%m-%d}'.format(next_day_object)
    if next_day in selected_days:
      if next_day not in out:
        out[next_day] = []
      out[next_day].append(targets[i])

  with open(w, 'w') as file:
    json.dump(out, file, sort_keys=True)
  
with open('./ids.json', 'r') as file:
  ids = json.load(file)
  
for user_id in ids:
  r = './tweets_raw/{}.json'.format(user_id)
  targets_path = './tweets_raw/features_step1/{}target.json'.format(user_id)
  selected_days_path = './tweets_selected/days/{}.json'.format(user_id)
  w = './tweets_selected/features_step1/{}target_current.json'.format(user_id)
  process(r, targets_path, selected_days_path, w)
