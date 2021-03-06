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
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step3/{}.json'.format(user_id)

  try:
    with open('/vagrant/data/osn-data/features_step1/{}target_tweets_selected.json'.format(user_id), 'r') as file:
      targets = json.load(file)
  except FileNotFoundError as e:
    continue

  with open('/vagrant/data/osn-data/features_step2/{}hashtags_count.json'.format(user_id), 'r') as file:
    hashtags_count = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}mentions_count.json'.format(user_id), 'r') as file:
    mentions_count = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}favourites_count.json'.format(user_id), 'r') as file:
    favourites_count = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}media_count.json'.format(user_id), 'r') as file:
    media_count = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}source.json'.format(user_id), 'r') as file:
    source = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}week.json'.format(user_id), 'r') as file:
    week = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}day_night.json'.format(user_id), 'r') as file:
    day_night = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}active_passive.json'.format(user_id), 'r') as file:
    active_passive = json.load(file)
      
  with open('/vagrant/data/osn-data/features_step2/{}mentions.json'.format(user_id), 'r') as file:
    mentions = json.load(file)

  with open('/vagrant/data/osn-data/features_step2/{}top_mentions.json'.format(user_id), 'r') as file:
    top_mentions = json.load(file)

#  tags = {}
#  try:      
#    with open('/vagrant/data/osn-data/features_step2/{}tags.json'.format(user_id), 'r') as file:
#      tags = json.load(file)
#  except Exception as e:
#    tags = {}

  with open('/vagrant/data/osn-data/features_step2/{}coordinates.json'.format(user_id), 'r') as file:
    coordinates = json.load(file)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)
      
  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  byday = {}
  i = -1
  for tweet in tweets:
    i += 1
    if tweet is None or 'created_at' not in tweet:
      continue
    created_at = tweet['created_at']
    import re
    #Mon Sep 26 22:47:22 +0000 2016
    m = re.search('^.{3} (.{3}) (.{2}) .{8} \+.{4} (.{4})$', created_at)
    key = '{}-{}-{}'.format(m.group(3), month[m.group(1)], m.group(2))
    if key not in byday:
      byday[key] = {
        '_target':[],
        'hashtags_count':[],
        'mentions_count':[],
        'favourites_count':[],
        'media_count':[],
        'source':[],
        'week':[],
        'day_night':[],
        'active_passive':[],
        'mentions':[],
#        'tags':[],
        'coordinates':[],
        'top_mentions_day':[],
      }
    top_mentions_day = []
    for top_mention in top_mentions:
      if top_mention in mentions[i]:
        top_mentions_day.append(top_mention)
    byday[key]['_target'].append(targets[i])
    byday[key]['hashtags_count'].append(hashtags_count[i])
    byday[key]['mentions_count'].append(mentions_count[i])
    byday[key]['favourites_count'].append(favourites_count[i])
    byday[key]['media_count'].append(media_count[i])
    byday[key]['source'].append(source[i])
    byday[key]['week'].append(week[i])
    byday[key]['day_night'].append(day_night[i])
    byday[key]['active_passive'].append(active_passive[i])
    byday[key]['mentions'].extend(mentions[i])
#    if key in tags:
#      byday[key]['tags'].extend(tags[key])
    byday[key]['coordinates'].append(coordinates[i])
    byday[key]['top_mentions'] = top_mentions_day

  with open(w, 'w') as file:
    json.dump(byday, file, sort_keys=True)

# mentioned users
'''
path = '/vagrant/data/osn-data/tweets/mentions/past_tweets/csv'
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv')]

for f in files:
  import re
  user_id = re.search('^(.*)\.csv$', f).group(1)
  r = '/vagrant/data/osn-data/tweets/mentions/past_tweets/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step3/mentions/past_tweets/{}.json'.format(user_id)

  with open('/vagrant/data/osn-data/features_step1/mentions/past_tweets/{}target.json'.format(user_id), 'r') as file:
    targets = json.load(file)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  byday = {}
  i = -1
  for tweet in tweets:
    i += 1
    if tweet is None or 'created_at' not in tweet:
      continue
    created_at = tweet['created_at']
    import re
    #Mon Sep 26 22:47:22 +0000 2016
    m = re.search('^.{3} (.{3}) (.{2}) .{8} \+.{4} (.{4})$', created_at)
    key = '{}-{}-{}'.format(m.group(3), month[m.group(1)], m.group(2))
    if key not in byday:
      byday[key] = {
        '_target':[],
      }
    byday[key]['_target'].append(targets[i])

  with open(w, 'w') as file:
    json.dump(byday, file, sort_keys=True)
'''
