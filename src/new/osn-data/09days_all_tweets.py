#!/usr/bin/python3

import json
from datetime import datetime, timedelta
        
def process(r, w):
  with open(r, 'r') as file:
    tweets = json.load(file)

#  sources = {
#    '<a href="http://foursquare.com" rel="nofollow">Foursquare</a>':None,
#    '<a href="http://instagram.com" rel="nofollow">Instagram</a>':None
#  }

  out = {}
  for key in sorted(tweets.keys()):
    # Tue Sep 27 01:58:41 +0000 2016
    current_day = tweets[key]['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    out['{0:%Y-%m-%d}'.format(current_day_object)] = None

  with open(w, 'w') as file:
    json.dump(out, file, sort_keys=True)
  
with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = './tweets_raw/{}.json'.format(user_id)
  w = './tweets_selected/days/{}.json'.format(user_id)
  process(r, w)
