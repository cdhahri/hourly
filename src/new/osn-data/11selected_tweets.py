#!/usr/bin/python3

import json
from datetime import datetime, timedelta
        
def process(r, selected_days_path, w):
  with open(r, 'r') as file:
    tweets = json.load(file)

  with open(selected_days_path, 'r') as file:
    selected_days = json.load(file)

  out = {}
  i = -1
  for key in sorted(tweets.keys()):
    i += 1
    # Tue Sep 27 01:58:41 +0000 2016
    current_day = tweets[key]['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    next_day_object = current_day_object + timedelta(days=1)
    if '{0:%Y-%b-%d}'.format(next_day_object) in selected_days:
      out[key] = tweets[key]

  with open(w, 'w') as file:
    json.dump(out, file, sort_keys=True)
  
with open('./ids.json', 'r') as file:
  ids = json.load(file)
  
for user_id in ids:
  r = './tweets_raw/{}.json'.format(user_id)
  selected_days_path = './tweets_selected/days/{}.json'.format(user_id)
  w = './tweets_selected/{}.json'.format(user_id)
  process(r, selected_days_path, w)
