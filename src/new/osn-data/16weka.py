#!/usr/bin/python

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import csv
import json
import itertools
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

ids = [1021239846,10521002,10929372,115138473,11661442,117093537,117567036,11922222,12091872,132191278,137123695,140289159,14683259,15030109,15153365,151846979,15232993,15413409,15473636,15676300,15852942,16090559,16218208,163554714,16568592,16754274,16830304,17006237,17611773,17679900,178290294,18100365,18107739,18671170,19007528,19243536,19257498,19429282,19640038,1972501,212732867,21305689,213170736,21449222,215464034,215538575,21841580,22097148,2235343141,22723261,22800249,22804043,22817477,23446307,24390992,2445862754,248969328,255570795,26059680,26111925,261283186,26299238,272932351,27328412,27817688,281800166,28258368,28388270,285877073,289677739,29207028,294149843,2971829547,30133362,3025016884,31512916,3270360024,33552718,35135168,36053100,37433679,40869137,43772221,43787354,46535963,466446470,471669821,47473194,474874843,481990966,531084450,541899796,543479819,54463831,553749027,566866170,5723252,59809965,61178222,612889857,6246252,625299965,62947925,64035286,68306612,73000498,791125,867192025,86924274,8776002,87967892,902226338,96147007,96886316]

for user_id in ids:
  for percentage in percentages:
    r = './tweets_selected/features_step3/aggregated/{}/{}.json'.format(percentage, user_id)
    w = './tweets_selected/features_step3/aggregated/weka/{}/{}.csv'.format(percentage, user_id)

    with open(r, 'r') as file:
      byday_aggregated = json.load(file)

    with open(w, 'w', newline='', encoding='utf-8') as file:
      csv_writer = csv.writer(file, delimiter=',')
      csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','top_mentions','coordinates','target'])
      #csv_writer.writerow(['count_all_capital','count_exclamation_mark','count_question_mark','count_negative_word','count_positive_word','exist_more_than_three_dots','exist_more_than_three_vowels','target'])
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

          #byday_aggregated[key]['count_all_capital'],
          #byday_aggregated[key]['count_exclamation_mark'],
          #byday_aggregated[key]['count_question_mark'],
          #byday_aggregated[key]['count_negative_word'],
          #byday_aggregated[key]['count_positive_word'],
          #byday_aggregated[key]['exist_more_than_three_dots'],
          #byday_aggregated[key]['exist_more_than_three_vowels'],

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
