#!/usr/bin/python

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import csv
import json
import itertools
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = './tweets_selected/features_step3/aggregated/{}/{}.json'.format(percentage, user_id)
    w = './tweets_selected/features_step3/aggregated/weka/{}/{}.csv'.format(percentage, user_id)

    with open(r, 'r') as file:
      byday_aggregated = json.load(file)

    with open(w, 'w', newline='', encoding='utf-8') as file:
      csv_writer = csv.writer(file, delimiter=',')
      # csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','top_mentions','coordinates','target'])
      csv_writer.writerow(['count_all_capital','count_exclamation_mark','count_question_mark','count_negative_word','count_positive_word','exist_more_than_three_dots','exist_more_than_three_vowels','target'])
      for key in sorted(byday_aggregated.keys()):
        mentions = byday_aggregated[key]['mentions']
        if len(mentions) == 0:
          mentions = [-1]
        top_mentions = byday_aggregated[key]['top_mentions']
        if len(top_mentions) == 0:
          top_mentions = [-1]
        coordinates = byday_aggregated[key]['coordinates']
        if len(coordinates) == 0:
          coordinates = [-1]
  #      a = [mentions, top_mentions, coordinates]
  #      products = list(itertools.product(*a))
  #      for prod in products:
        csv_writer.writerow([

          #byday_aggregated[key]['hashtags_count'],
          #byday_aggregated[key]['mentions_count'],
          #byday_aggregated[key]['favourites_count'],
          #byday_aggregated[key]['media_count'],
          #byday_aggregated[key]['source'],
          #byday_aggregated[key]['week'],
          #byday_aggregated[key]['day_night'],
          #byday_aggregated[key]['active_passive'],
          #mentions[0],
          #top_mentions[0],
          #coordinates[0],

          byday_aggregated[key]['count_all_capital'],
          byday_aggregated[key]['count_exclamation_mark'],
          byday_aggregated[key]['count_question_mark'],
          byday_aggregated[key]['count_negative_word'],
          byday_aggregated[key]['count_positive_word'],
          byday_aggregated[key]['exist_more_than_three_dots'],
          byday_aggregated[key]['exist_more_than_three_vowels'],

  #        prod[0], NO
  #        prod[1], NO
  #        prod[2], NO
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
