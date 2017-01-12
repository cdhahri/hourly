#!/usr/bin/python

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import csv
import json
import itertools
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  print(user_id)
  for percentage in percentages:
    print(percentage / 10)
    r = './tweets_selected/features_step3/aggregated/{}/{}.json'.format(percentage, user_id)
    w = './tweets_selected/features_step3/aggregated/weka/{}/{}.csv'.format(percentage, user_id)

    with open(r, 'r') as file:
      byday_aggregated = json.load(file)

    with open(w, 'w', newline='', encoding='utf-8') as file:
      csv_writer = csv.writer(file, delimiter=',')
      csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','top_mentions','coordinates','target'])
      #csv_writer.writerow(['mentions','top_mentions','coordinates','target'])
      for key in sorted(byday_aggregated.keys()):
        mentions = byday_aggregated[key]['mentions']
        if len(mentions) == 0:
          mentions = [-1]
  #        continue
        top_mentions = byday_aggregated[key]['top_mentions']
        if len(top_mentions) == 0:
          top_mentions = [-1]
  #        continue
        coordinates = byday_aggregated[key]['coordinates']
        if len(coordinates) == 0:
          coordinates = [-1]
  #        continue
  #      a = [mentions, top_mentions, coordinates]
  #      products = list(itertools.product(*a))
  #      for prod in products:
        csv_writer.writerow([
          byday_aggregated[key]['hashtags_count'],
          byday_aggregated[key]['mentions_count'],
          byday_aggregated[key]['favourites_count'],
          byday_aggregated[key]['media_count'],
          byday_aggregated[key]['source'],
          byday_aggregated[key]['week'],
          byday_aggregated[key]['day_night'],
          byday_aggregated[key]['active_passive'],
          mentions[0],
          top_mentions[0],
          coordinates[0],
  #        prod[0],
  #        prod[1],
  #        prod[2],
          byday_aggregated[key]['_target']
         ])

  '''
  w = '/vagrant/data/osn-data/features_step3/aggregated/weka/all.csv'.format(user_id)
  with open(w, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','coordinates','top_mentions','target'])
    for user_id in ids:
      r = '/vagrant/data/osn-data/features_step3/aggregated/{}.json'.format(user_id)
      with open(r, 'r') as file:
        byday_aggregated = json.load(file)

      for key in sorted(byday_aggregated.keys()):
        csv_writer.writerow([
          byday_aggregated[key]['hashtags_count'],
          byday_aggregated[key]['mentions_count'],
          byday_aggregated[key]['favourites_count'],
          byday_aggregated[key]['media_count'],
          byday_aggregated[key]['source'],
          byday_aggregated[key]['week'],
          byday_aggregated[key]['day_night'],
          byday_aggregated[key]['active_passive'],
          byday_aggregated[key]['mentions'],
          byday_aggregated[key]['coordinates'],
          byday_aggregated[key]['top_mentions'],
          byday_aggregated[key]['_target']
        ])
  '''
