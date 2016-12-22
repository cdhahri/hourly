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

ids = [10045092, 1007531, 101496212, 1021239846, 102464379, 103114245, 103695733, 10449052, 104852013, 10521002, 106104712, 108944858, 109223169, 10929372, 109485267, 110808568, 111178547, 11126582, 111454868, 112490071, 112858627, 11312992, 113441429, 11346942, 11437162, 115073079, 115138473, 115171979, 11661442, 117093537, 117562901, 117567036, 1177083624, 11778632, 117870724, 117987103, 118459389, 118474054, 11922222, 119436439, 119773854, 11987272, 119979433, 120268489, 12091872, 121768977, 122737979, 123059038, 1231465759, 1236198937, 123745496]  

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step3/{}.json'.format(user_id)

  with open('/vagrant/data/osn-data/features_step1/{}target.json'.format(user_id), 'r') as file:
    targets = json.load(file)

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
      
  with open('/vagrant/data/osn-data/features_step2/{}active_passive.json'.format(user_id), 'r') as file:
    active_passive = json.load(file)
      
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
        'active_passive':[],
      }
    byday[key]['_target'].append(targets[i])
    byday[key]['hashtags_count'].append(hashtags_count[i])
    byday[key]['mentions_count'].append(mentions_count[i])
    byday[key]['favourites_count'].append(favourites_count[i])
    byday[key]['media_count'].append(media_count[i])
    byday[key]['source'].append(source[i])
    byday[key]['week'].append(week[i])
    byday[key]['active_passive'].append(active_passive[i])

  with open(w, 'w') as file:
    json.dump(byday, file, sort_keys=True)
