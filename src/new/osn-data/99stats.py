#!/usr/bin/python3

import json
from datetime import datetime, timedelta
import numpy as np

with open('./ids.json', 'r') as file:
  ids = json.load(file)

all_ = []
for user_id in ids:
  with open('./tweets_selected/{}.json'.format(user_id), 'r') as file:
    tweets = json.load(file)

  out = {}
  for key in sorted(tweets.keys()):
    # Tue Sep 27 01:58:41 +0000 2016
    current_day = tweets[key]['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    day = '{0:%Y-%b-%d}'.format(current_day_object)
    if day not in out:
      out[day] = 0
    out[day] = out[day] + 1

  a = np.array([list(out.values())])
  if len(list(out.values())) != 0:
    all_.append(np.mean(a))

a = np.array([all_])
print(np.mean(a))
