#!/usr/bin/python3

import json
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 1007531, 101496212, 1021239846, 102464379, 103114245, 103695733, 10449052, 104852013, 10521002, 106104712, 108944858, 109223169, 10929372, 109485267, 110808568, 111178547, 11126582, 111454868, 112490071, 112858627, 11312992, 113441429, 11346942, 11437162, 115073079, 115138473, 115171979, 11661442, 117093537, 117562901, 117567036, 1177083624, 11778632, 117870724, 117987103, 118459389, 118474054, 11922222, 119436439, 119773854, 11987272, 119979433, 120268489, 12091872, 121768977, 122737979, 123059038, 1231465759, 1236198937, 123745496]  

for user_id in ids:
  r = '/vagrant/data/osn-data/features_step3/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step3/aggregated/{}.json'.format(user_id)

  with open(r, 'r') as file:
    byday = json.load(file)
      
  byday_aggregated = {}
  for key, day in byday.items():
    target = day['_target']
    pos = target.count('4')
    neg = target.count('0')
    target = pos / (pos + neg)

    hashtags_count = day['hashtags_count']
    hashtags_count = sum(hashtags_count)

    mentions_count = day['mentions_count']
    mentions_count = sum(mentions_count)

    favourites_count = day['favourites_count']
    favourites_count = sum(favourites_count)

    media_count = day['media_count']
    media_count = sum(media_count)

    source = day['source']
    source = len(set(source))

    week = day['week'][0]

    active_passive = day['active_passive']
    pos = active_passive.count(1)
    neg = active_passive.count(-1)
    active_passive = pos / (pos + neg)

    byday_aggregated[key] = {
      '_target':target,
      'hashtags_count':hashtags_count,
      'mentions_count':mentions_count,
      'favourites_count':favourites_count,
      'media_count':media_count,
      'source':source,
      'week':week,
      'active_passive':active_passive,
    }

  with open(w, 'w') as file:
    json.dump(byday_aggregated, file, sort_keys=True)
