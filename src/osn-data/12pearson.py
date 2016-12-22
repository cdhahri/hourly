#!/usr/bin/python

import json
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 1007531, 101496212, 1021239846, 102464379, 103114245, 103695733, 10449052, 104852013, 10521002, 106104712, 108944858, 109223169, 10929372, 109485267, 110808568, 111178547, 11126582, 111454868, 112490071, 112858627, 11312992, 113441429, 11346942, 11437162, 115073079, 115138473, 115171979, 11661442, 117093537, 117562901, 117567036, 1177083624, 11778632, 117870724, 117987103, 118459389, 118474054, 11922222, 119436439, 119773854, 11987272, 119979433, 120268489, 12091872, 121768977, 122737979, 123059038, 1231465759, 1236198937, 123745496]  

for user_id in ids:
  r = '/vagrant/data/osn-data/features_step3/aggregated/{}.json'.format(user_id)

  with open(r, 'r') as file:
    byday_aggregated = json.load(file)

  target = []
  hashtags_count = []      
  mentions_count = []
  favourites_count = []
  media_count = []
  source = []
  week = []
  active_passive = []
  for key in sorted(byday_aggregated.keys()):
    target.append(byday_aggregated[key]['_target'])
    hashtags_count.append(byday_aggregated[key]['hashtags_count'])
    mentions_count.append(byday_aggregated[key]['mentions_count'])
    favourites_count.append(byday_aggregated[key]['favourites_count'])
    media_count.append(byday_aggregated[key]['media_count'])
    source.append(byday_aggregated[key]['source'])
    week.append(byday_aggregated[key]['week'])
    active_passive.append(byday_aggregated[key]['active_passive'])

  if user_id == 1231465759:
    print(active_passive)
  from scipy.stats import pearsonr
#  print('{}: Hashtags count: {}'.format(user_id, str(pearsonr(target, hashtags_count))))
#  print('{}: Mentions count: {}'.format(user_id, str(pearsonr(target, mentions_count))))
#  print('{}: Favourites count: {}'.format(user_id, str(pearsonr(target, favourites_count))))
#  print('{}: Media count: {}'.format(user_id, str(pearsonr(target, media_count))))
#  print('{}: Source: {}'.format(user_id, str(pearsonr(target, source))))
#  print('{}: Week: {}'.format(user_id, str(pearsonr(target, week))))
  print('{}: Active/Passive: {}'.format(user_id, str(pearsonr(target, active_passive))))
