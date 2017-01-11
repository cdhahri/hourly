#!/usr/bin/python3

month = {
 'Jan': '01',
 'Feb': '02',
 'Mar': '03',
 'Apr': '04',
 'May': '05',
 'Jun': '06',
 'Jul': '07',
 'Aug': '08',
 'Sep': '09',
 'Oct': '10',
 'Nov': '11',
 'Dec': '12',
}

import json
from datetime import datetime, timedelta
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  with open('./tweets_selected/features_step1/{}target.json'.format(user_id), 'r') as file:
    targets = json.load(file)

#  with open('./tweets_selected/features_step1/{}target_current.json'.format(user_id), 'r') as file:
#    targets_current = json.load(file)

  byday = {}
  i = -1
  for key in sorted(targets.keys()):
    i += 1
#    if key not in targets_current:
#      continue
    if key not in byday:
      byday[key] = {
        '_target':targets[key],
#        '_target_current':targets_current[key],
        'hashtags_count':[],
        'mentions_count':[],
        'favourites_count':[],
        'media_count':[],
        'source':[],
        'week':[],
        'day_night':[],
        'active_passive':[],
        'mentions':[],
        'coordinates':[],
        'top_mentions_day':[],
      }
    byday[key]['_target'] = targets[key]
#    byday[key]['_target_current'] = targets_current[key]

  #
  #
  #

  with open('./tweets_selected/{}.json'.format(user_id), 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  with open('./tweets_selected/features_step2/{}hashtags_count.json'.format(user_id), 'r') as file:
    hashtags_count = json.load(file)
      
  with open('./tweets_selected/features_step2/{}mentions_count.json'.format(user_id), 'r') as file:
    mentions_count = json.load(file)
      
  with open('./tweets_selected/features_step2/{}favourites_count.json'.format(user_id), 'r') as file:
    favourites_count = json.load(file)
      
  with open('./tweets_selected/features_step2/{}media_count.json'.format(user_id), 'r') as file:
    media_count = json.load(file)
      
  with open('./tweets_selected/features_step2/{}source.json'.format(user_id), 'r') as file:
    source = json.load(file)
      
  with open('./tweets_selected/features_step2/{}week.json'.format(user_id), 'r') as file:
    week = json.load(file)
      
  with open('./tweets_selected/features_step2/{}day_night.json'.format(user_id), 'r') as file:
    day_night = json.load(file)
      
  with open('./tweets_selected/features_step2/{}active_passive.json'.format(user_id), 'r') as file:
    active_passive = json.load(file)
      
  with open('./tweets_selected/features_step2/{}mentions.json'.format(user_id), 'r') as file:
    mentions = json.load(file)

  with open('./tweets_selected/features_step2/{}top_mentions.json'.format(user_id), 'r') as file:
    top_mentions = json.load(file)

  with open('./tweets_selected/features_step2/{}coordinates.json'.format(user_id), 'r') as file:
    coordinates = json.load(file)

  i = -1
  for tweet in tweets:
    i += 1
    #Mon Sep 26 22:47:22 +0000 2016
    current_day = tweet['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    next_day_object = current_day_object + timedelta(days=1)
    key = '{0:%Y-%m-%d}'.format(next_day_object)

    if key not in byday:
      continue
    top_mentions_day = []
    for top_mention in top_mentions:
      if top_mention in mentions[i]:
        top_mentions_day.append(top_mention)
    byday[key]['hashtags_count'].append(hashtags_count[i])
    byday[key]['mentions_count'].append(mentions_count[i])
    byday[key]['favourites_count'].append(favourites_count[i])
    byday[key]['media_count'].append(media_count[i])
    byday[key]['source'].append(source[i])
    byday[key]['week'].append(week[i])
    byday[key]['day_night'].append(day_night[i])
    byday[key]['active_passive'].append(active_passive[i])
    byday[key]['mentions'].extend(mentions[i])
    byday[key]['coordinates'].append(coordinates[i])
    byday[key]['top_mentions'] = top_mentions_day

  with open('./tweets_selected/features_step3/{}.json'.format(user_id), 'w') as file:
    json.dump(byday, file, sort_keys=True)
