#!/usr/bin/python3

sources = {
  '<a href="http://foursquare.com" rel="nofollow">Foursquare</a>':None,
  '<a href="http://instagram.com" rel="nofollow">Instagram</a>':None
}

import json
from datetime import datetime, timedelta
        
def process(tweets, selected_days, targets, w):
  out = {}
  i = -1
  for key in sorted(tweets.keys()):
    i += 1
    # Tue Sep 27 01:58:41 +0000 2016
    # if targets[i] == '0':
    # if tweets[key]['source'] not in sources or targets[i] != '0':
      # continue
    current_day = tweets[key]['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    next_day_object = current_day_object + timedelta(days=1)
    if '{0:%Y-%m-%d}'.format(next_day_object) in selected_days:# and tweets[key]['source'] in sources:
      out[key] = tweets[key]

  with open(w, 'w') as file:
    json.dump(out, file, sort_keys=True)
  
with open('./ids.json', 'r') as file:
  ids = json.load(file)
  
percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]
for user_id in ids:
  r = './tweets_raw/{}.json'.format(user_id)
  target_path = './tweets_raw/features_step1/{}target.json'.format(user_id)
  selected_days_path = './tweets_selected/days/{}.json'.format(user_id)

  with open(r, 'r') as file:
    tweets = json.load(file)
  with open(selected_days_path, 'r') as file:
    selected_days = json.load(file)
  with open(target_path, 'r') as file:
    targets = json.load(file)

  for percentage in percentages:
    length = int((percentage/10)*(len(selected_days.keys())))
    selected_days_subset = {}
    i = -1
    for key in sorted(selected_days.keys()):
      i += 1
      if i == length:
        break
      selected_days_subset[key] = selected_days[key]

    w = './tweets_selected/{}/{}.json'.format(percentage, user_id)
    process(tweets, selected_days_subset, targets, w)
