#!/usr/bin/python3

import json
import os.path

'''        
# mentioned users
path = '/vagrant/data/osn-data/tweets/mentions/past_tweets/csv'
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv')]

for f in files:
  import re
  user_id = re.search('^(.*)\.csv$', f).group(1)

  r = '/vagrant/data/osn-data/features_step3/mentions/past_tweets/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step3/mentions/past_tweets/aggregated/{}.json'.format(user_id)

  with open(r, 'r') as file:
    byday = json.load(file)

  byday_aggregated = {}
  for key, day in byday.items():
    target = day['_target']
    pos = target.count('4')
    neg = target.count('0')
    target = pos / (pos + neg)

    byday_aggregated[key] = {
      '_target':target,
    }

  with open(w, 'w') as file:
    json.dump(byday_aggregated, file, sort_keys=True)
'''

# users
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

#ids = [10521002, 106104712, 109485267, 111178547, 113441429, 115138473, 11661442, 117567036, 11922222, 127828353, 1315286089, 133794989, 13385712, 142406505, 142802575, 14852278, 14900774, 15507115, 16090559, 16133557, 164266156, 16427456, 16830304, 16983823, 17289508, 17395031, 17997140, 18100365, 18107739, 18142778, 18853460, 19257498, 19388800, 199082056, 20022522, 20405425, 2084821, 212732867, 212991627, 21449222]

for user_id in ids:
  r = '/vagrant/data/osn-data/features_step3/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step3/aggregated/{}.json'.format(user_id)

  try:
    with open(r, 'r') as file:
      byday = json.load(file)
  except FileNotFoundError:
    continue

  i = 0
  auto_inc = {}
  j = 0
  auto_inc2 = {}
  k = 0
  auto_inc_mentions = {}
  l = 0
  auto_inc_top_mentions = {}
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

    # media type

    # source type

    week = day['week'][0]

    day_night = day['day_night']
    d = 0
    n = 0
    for dn in day_night:
      if int(dn) > 20 or int(dn) < 6:
        n += 1
      else:
        d += 1
    day_night = d / (d + n)

    active_passive = day['active_passive']
    pos = active_passive.count(1)
    neg = active_passive.count(-1)
    active_passive = pos / (pos + neg)

    mentions = day['mentions']
    mentions_values = []
    for mention in mentions:
      if mention not in auto_inc_mentions:
        k += 1
        auto_inc_mentions[mention] = k
      mentions_values.append(auto_inc_mentions[mention])

    top_mentions = day['top_mentions']
    top_mentions_values = []
    for mention in top_mentions:
      if mention not in auto_inc_top_mentions:
        l += 1
        auto_inc_top_mentions[mention] = l
      top_mentions_values.append(auto_inc_top_mentions[mention])

    '''
    mentions = day['mentions']
    moods = []
    for mention in mentions:
      if not os.path.exists('/vagrant/data/osn-data/features_step3/mentions/past_tweets/aggregated/{}.json'.format(mention)):
        continue
      with open('/vagrant/data/osn-data/features_step3/mentions/past_tweets/aggregated/{}.json'.format(mention), 'r') as file:
        mention_history = json.load(file)
      if key in mention_history:
        moods.append(mention_history[key]['_target'])
    #
    if len(moods) == 0:
      moods = [0]
    import numpy
    moods = numpy.mean(moods)
    '''

    '''
    tags = day['tags']
    tags_values = []
    for tag in tags:
      if tag not in auto_inc:
        i += 1
        auto_inc[tag] = i
      tags_values.append(auto_inc[tag])
    '''

    coordinates = day['coordinates']
    coordinates_values = []
    for coordinate in coordinates:
      if coordinate is None:
        coordinates_values.append(-100)
        continue
      if coordinate not in auto_inc2:
        j += 1
        auto_inc2[coordinate] = j
      coordinates_values.append(auto_inc2[coordinate])

    byday_aggregated[key] = {
      '_target':target,
      'hashtags_count':hashtags_count,
      'mentions_count':mentions_count,
      'favourites_count':favourites_count,
      'media_count':media_count,
      'source':source,
      'week':week,
      'day_night':day_night,
      'active_passive':active_passive,
      'mentions':mentions_values,
#      'tags':tags_values,
      'coordinates':coordinates_values,
      'top_mentions':top_mentions_values,
    }

  with open(w, 'w') as file:
    json.dump(byday_aggregated, file, sort_keys=True)

