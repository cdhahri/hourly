#!/usr/bin/python3

import json
from datetime import datetime, timedelta
        
def process(r, target_path, w):
  with open(r, 'r') as file:
    tweets = json.load(file)

  with open(target_path, 'r') as file:
    targets = json.load(file)

  out = {}
  i = -1
  for key in sorted(tweets.keys()):
    i += 1
    if targets[i] == '0':
      # Tue Sep 27 01:58:41 +0000 2016
      current_day = tweets[key]['created_at']
      current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
      out['{0:%Y-%b-%d}'.format(current_day_object)] = None

  with open(w, 'w') as file:
    json.dump(out, file, sort_keys=True)
  
with open('./ids.json', 'r') as file:
  ids = json.load(file)
  
for user_id in ids:
  r = './tweets_raw/{}.json'.format(user_id)
  target_path = './tweets_raw/features_step1/{}target.json'.format(user_id)
  w = './tweets_selected/days/{}.json'.format(user_id)
  process(r, target_path, w)
