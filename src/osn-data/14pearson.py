#!/usr/bin/python

import json
from scipy.stats import pearsonr
from scipy import stats

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

#ids = [10521002, 106104712, 109485267, 111178547, 113441429, 115138473, 11661442, 117567036, 11922222, 127828353, 1315286089, 133794989, 13385712, 142406505, 142802575, 14852278, 14900774, 15507115, 16090559, 16133557, 164266156, 16427456, 16830304, 16983823, 17289508, 17395031, 17997140, 18100365, 18107739, 18142778, 18853460, 19257498, 19388800, 199082056, 20022522, 20405425, 2084821, 212732867, 212991627, 21449222]

for user_id in ids:
  r = '/vagrant/data/osn-data/features_step3/aggregated/{}.json'.format(user_id)

  try:
    with open(r, 'r') as file:
      byday_aggregated = json.load(file)
  except FileNotFoundError:
    continue

  target = []
  hashtags_count = []      
  mentions_count = []
  favourites_count = []
  media_count = []
  source = []
  week = []
  active_passive = []
  mentions = []
#  tags = []
  coordinates = []
  top_mentions = []
  for key in sorted(byday_aggregated.keys()):
    target.append(byday_aggregated[key]['_target'])
    hashtags_count.append(byday_aggregated[key]['hashtags_count'])
    mentions_count.append(byday_aggregated[key]['mentions_count'])
    favourites_count.append(byday_aggregated[key]['favourites_count'])
    media_count.append(byday_aggregated[key]['media_count'])
    source.append(byday_aggregated[key]['source'])
    week.append(byday_aggregated[key]['week'])
    active_passive.append(byday_aggregated[key]['active_passive'])
    mentions.append(byday_aggregated[key]['mentions'])
#    tags.append(byday_aggregated[key]['tags'])
    coordinates.append(byday_aggregated[key]['coordinates'])
    top_mentions.append(byday_aggregated[key]['top_mentions'])

  if len(set(target)) < 2:
    continue

  '''
  hashtags_count = stats.zscore(hashtags_count).tolist()
  hashtags_count_pearson = pearsonr(target, hashtags_count)
  if abs(hashtags_count_pearson[0]) > 0.3:
    print(user_id)
    print('@{}'.format(hashtags_count_pearson[0]))
    print('@{}'.format(hashtags_count_pearson[1]))
  '''

  '''
  mentions_count = stats.zscore(mentions_count).tolist()
  mentions_count_pearson = pearsonr(target, mentions_count)
  if abs(mentions_count_pearson[0]) > 0.3:
    print(user_id)
    print('@{}'.format(mentions_count_pearson[0]))
    print('@{}'.format(mentions_count_pearson[1]))
  '''

  '''
  favourites_count = stats.zscore(favourites_count).tolist()
  favourites_count_pearson = pearsonr(target, favourites_count)
  if abs(favourites_count_pearson[0]) > 0.3:
    print(user_id)
    print('@{}'.format(favourites_count_pearson[0]))
    print('@{}'.format(favourites_count_pearson[1]))
  '''

  '''
  media_count = stats.zscore(media_count).tolist()
  media_count_pearson = pearsonr(target, media_count)
  if abs(media_count_pearson[0]) > 0.3:
    print(user_id)
    print('@{}'.format(media_count_pearson[0]))
    print('@{}'.format(media_count_pearson[1]))
  '''

  '''
  if len(set(source)) < 2:
    continue
  source = stats.zscore(source).tolist()
  source_pearson = pearsonr(target, source)
  if abs(source_pearson[0]) > 0.3:
    print(user_id)
    print('@{}'.format(source_pearson[0]))
    print('@{}'.format(source_pearson[1]))
  '''

  '''
  week = stats.zscore(week).tolist()
  week_pearson = pearsonr(target, week)
  if abs(week_pearson[0]) > 0.3:
    print(user_id)
    print('@{}'.format(week_pearson[0]))
    print('@{}'.format(week_pearson[1]))
  '''

  '''
  if len(set(active_passive)) < 2:
    continue
  active_passive = stats.zscore(active_passive).tolist()
  active_passive_pearson = pearsonr(target, active_passive)
  if abs(active_passive_pearson[0]) > 0.3 and abs(active_passive_pearson[1]) < 0.01:
    print(user_id)
    print('@{}'.format(active_passive_pearson[0]))
    print('@{}'.format(active_passive_pearson[1]))
  '''

  '''
  target_mentions = []
  mentions_mentions = []
  for i in range(len(target)):
    for j in range(len(mentions[i])):
      #?
      #if mentions[i][j] == -100:
      #  continue
      target_mentions.append(target[i])
      mentions_mentions.append(mentions[i][j])
  if len(set(mentions_mentions)) < 2:
    continue
  mentions_mentions = stats.zscore(mentions_mentions).tolist()
  mentions_pearson = pearsonr(target_mentions, mentions_mentions)
  if abs(mentions_pearson[0]) > 0.2 and abs(mentions_pearson[1]) < 0.01:
    print(user_id)
    print('@{}'.format(mentions_pearson[0]))
    print('@{}'.format(mentions_pearson[1]))
  '''

  '''
  target_coordinates = []
  coordinates_coordinates = []
  for i in range(len(target)):
    for j in range(len(coordinates[i])):
      if coordinates[i][j] == -100:
        continue
      target_coordinates.append(target[i])
      coordinates_coordinates.append(coordinates[i][j])
  if len(set(coordinates_coordinates)) < 2:
    continue
  coordinates_coordinates = stats.zscore(coordinates_coordinates).tolist()
  coordinates_pearson = pearsonr(target_coordinates, coordinates_coordinates)
  if abs(coordinates_pearson[0]) > 0.1 and abs(coordinates_pearson[1]) < 0.01:
    print(user_id)
    print('@{}'.format(coordinates_pearson[0]))
    print('@{}'.format(coordinates_pearson[1]))
  '''

  #'''
  target_top_mentions = []
  top_mentions_mentions = []
  for i in range(len(target)):
    for j in range(len(top_mentions[i])):
      #?
      #if top_mentions[i][j] == -100:
      #  continue
      target_top_mentions.append(target[i])
      top_mentions_mentions.append(top_mentions[i][j])
  if len(set(top_mentions_mentions)) < 2:
    continue
  top_mentions_mentions = stats.zscore(top_mentions_mentions).tolist()
  top_mentions_pearson = pearsonr(target_top_mentions, top_mentions_mentions)
  if abs(top_mentions_pearson[0]) > 0.2 and abs(top_mentions_pearson[1]) < 0.01:
    print(user_id)
    print('@{}'.format(top_mentions_pearson[0]))
    print('@{}'.format(top_mentions_pearson[1]))
  #'''
