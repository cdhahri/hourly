#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import json
import os.path

# users
with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = './tweets_selected/features_step3/{}/{}.json'.format(percentage, user_id)
    w = './tweets_selected/features_step3/aggregated/{}/{}.json'.format(percentage, user_id)

    with open(r, 'r') as file:
      byday = json.load(file)

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
      pos = target.count('1')
      neg = target.count('-1')
      #neu = target.count('0')
      target = (pos) / (pos + neg)

#     target_current = day['_target_current']
#     pos = target_current.count('4')
#     neg = target_current.count('0')
#     target_current = pos / (pos + neg)

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

      try:
        week = day['week'][0]
      except IndexError:
        continue

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

      count_all_capital = day['count_all_capital']
      count_all_capital = sum(count_all_capital)

      count_exclamation_mark = day['count_exclamation_mark']
      count_exclamation_mark = sum(count_exclamation_mark)

      count_question_mark = day['count_question_mark']
      count_question_mark = sum(count_question_mark)

      count_negative_word = day['count_negative_word']
      count_negative_word = sum(count_negative_word)

      count_positive_word = day['count_positive_word']
      count_positive_word = sum(count_positive_word)

      exist_more_than_three_dots = day['exist_more_than_three_dots']
      exist = False
      for item in exist_more_than_three_dots:
        if item is True:
          exist = True
          break
      exist_more_than_three_dots = exist

      exist_more_than_three_vowels = day['exist_more_than_three_vowels']
      exist = False
      for item in exist_more_than_three_vowels:
        if item is True:
          exist = True
          break
      exist_more_than_three_vowels = exist

      byday_aggregated[key] = {
        '_target':target,
  #      '_target_current':target_current,
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

        'count_all_capital':count_all_capital,
        'count_exclamation_mark':count_exclamation_mark,
        'count_question_mark':count_question_mark,
        'count_negative_word':count_negative_word,
        'count_positive_word':count_positive_word,
        'exist_more_than_three_dots':exist_more_than_three_dots,
        'exist_more_than_three_vowels':exist_more_than_three_vowels,
      }

    with open(w, 'w') as file:
      json.dump(byday_aggregated, file, sort_keys=True)
