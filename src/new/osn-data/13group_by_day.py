#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

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
from datetime import datetime, timedelta
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    with open('./tweets_selected/features_step1/{}/{}target.json'.format(percentage, user_id), 'r') as file:
      targets = json.load(file)

#   with open('./tweets_selected/features_step1/{}target_current.json'.format(user_id), 'r') as file:
#     targets_current = json.load(file)

    byday = {}
    for key in sorted(targets.keys()):
#     if key not in targets_current:
#       continue
      if key not in byday:
        byday[key] = {
          '_target':targets[key],
#         '_target_current':targets_current[key],
          'hashtags_count':[],
          'mentions_count':[],
          'favourites_count':[],
          'media_count':[],
          'source':[],
          'source_twitter_or_not':[],
          'week':[],
          'day_night':[],
          'active_passive':[],
          'mentions':[],
          'coordinates':[],
          'top_mentions_day':[],

          # 'count_all_capital':[],
          # 'count_exclamation_mark':[],
          # 'count_question_mark':[],
          # 'count_negative_word':[],
          # 'count_positive_word':[],
          # 'exist_more_than_three_dots':[],
          # 'exist_more_than_three_vowels':[],
        }
      byday[key]['_target'] = targets[key]
#     byday[key]['_target_current'] = targets_current[key]

    #
    #
    #

    with open('./tweets_selected/{}/{}.json'.format(percentage, user_id), 'r') as file:
      tweets_hash = json.load(file)

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    with open('./tweets_selected/features_step2/{}/{}hashtags_count.json'.format(percentage, user_id), 'r') as file:
      hashtags_count = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}mentions_count.json'.format(percentage, user_id), 'r') as file:
      mentions_count = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}favourites_count.json'.format(percentage, user_id), 'r') as file:
      favourites_count = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}media_count.json'.format(percentage, user_id), 'r') as file:
      media_count = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}source.json'.format(percentage, user_id), 'r') as file:
      source = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}source_twitter_or_not.json'.format(percentage, user_id), 'r') as file:
      source_twitter_or_not = json.load(file)

    with open('./tweets_selected/features_step2/{}/{}week.json'.format(percentage, user_id), 'r') as file:
      week = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}day_night.json'.format(percentage, user_id), 'r') as file:
      day_night = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}active_passive.json'.format(percentage, user_id), 'r') as file:
      active_passive = json.load(file)
        
    with open('./tweets_selected/features_step2/{}/{}mentions.json'.format(percentage, user_id), 'r') as file:
      mentions = json.load(file)

    with open('./tweets_selected/features_step2/{}/{}top_mentions.json'.format(percentage, user_id), 'r') as file:
      top_mentions = json.load(file)

    with open('./tweets_selected/features_step2/{}/{}coordinates.json'.format(percentage, user_id), 'r') as file:
      coordinates = json.load(file)


    # with open('./tweets_selected/features_step2/10/{}count_all_capital.json'.format(user_id), 'r') as file:
    #   count_all_capital = json.load(file)

    # with open('./tweets_selected/features_step2/10/{}count_exclamation_mark.json'.format(user_id), 'r') as file:
    #   count_exclamation_mark = json.load(file)

    # with open('./tweets_selected/features_step2/10/{}count_question_mark.json'.format(user_id), 'r') as file:
    #   count_question_mark = json.load(file)

    # with open('./tweets_selected/features_step2/10/{}count_negative_word.json'.format(user_id), 'r') as file:
    #   count_negative_word = json.load(file)

    # with open('./tweets_selected/features_step2/10/{}count_positive_word.json'.format(user_id), 'r') as file:
    #   count_positive_word = json.load(file)

    # with open('./tweets_selected/features_step2/10/{}exist_more_than_three_dots.json'.format(user_id), 'r') as file:
    #   exist_more_than_three_dots = json.load(file)

    # with open('./tweets_selected/features_step2/10/{}exist_more_than_three_vowels.json'.format(user_id), 'r') as file:
    #   exist_more_than_three_vowels = json.load(file)

    i = -1
    for tweet in tweets:
      i += 1
      #Mon Sep 26 22:47:22 +0000 2016
      current_day = tweet['created_at']
      current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
      next_day_object = current_day_object + timedelta(days=1)
      key = '{0:%Y-%m-%d}'.format(next_day_object)

      if key not in byday:
        continue
      top_mentions_day = []
      for top_mention in top_mentions:
        if top_mention in mentions[i]:
          top_mentions_day.append(top_mention)
      byday[key]['hashtags_count'].append(hashtags_count[i])
      byday[key]['mentions_count'].append(mentions_count[i])
      byday[key]['favourites_count'].append(favourites_count[i])
      byday[key]['media_count'].append(media_count[i])
      byday[key]['source'].append(source[i])
      byday[key]['source_twitter_or_not'].append(source_twitter_or_not[i])
      byday[key]['week'].append(week[i])
      byday[key]['day_night'].append(day_night[i])
      byday[key]['active_passive'].append(active_passive[i])
      byday[key]['mentions'].extend(mentions[i])
      byday[key]['coordinates'].append(coordinates[i])
      byday[key]['top_mentions'] = top_mentions_day

      # byday[key]['count_all_capital'].append(count_all_capital[i])
      # byday[key]['count_exclamation_mark'].append(count_exclamation_mark[i])
      # byday[key]['count_question_mark'].append(count_question_mark[i])
      # byday[key]['count_negative_word'].append(count_negative_word[i])
      # byday[key]['count_positive_word'].append(count_positive_word[i])
      # byday[key]['exist_more_than_three_dots'].append(exist_more_than_three_dots[i])
      # byday[key]['exist_more_than_three_vowels'].append(exist_more_than_three_vowels[i])

    with open('./tweets_selected/features_step3/{}/{}.json'.format(percentage, user_id), 'w') as file:
      json.dump(byday, file, sort_keys=True)
