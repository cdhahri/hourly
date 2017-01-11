#!/usr/bin/python

sources = {
  '<a href="http://foursquare.com" rel="nofollow">Foursquare</a>':None,
  '<a href="http://instagram.com" rel="nofollow">Instagram</a>':None
}

import json
with open('./ids.json', 'r') as file:
  ids = json.load(file)

length_be = 0
length_af = 0

total_count = 0
non_text_count = 0

for user_id in ids:
  with open('./tweets_selected/{}.json'.format(user_id), 'r') as file:
    tweets = json.load(file)

  for key, tweet in tweets.items():    
    total_count += 1
    text_be = tweet['text']
    text_af = tweet['text']

    entities = tweet['entities']

#    hashtags = entities['hashtags']
#    for hashtag in hashtags:
#      text_af = text_af.replace('#{}'.format(hashtag['text']), '')

    user_mentions = entities['user_mentions']
    for user_mention in user_mentions:
      text_af = text_af.replace('@{}'.format(user_mention['screen_name']), '')

    urls = entities['urls']
    for url in urls:
      text_af = text_af.replace(url['url'], '')

    if 'media' not in tweet['entities']:
      continue
    media = entities['media']
    for medium in media:
      text_af = text_af.replace(medium['url'], '')

    text_af = ' '.join(text_af.split())

    length_be += len(text_be)
    length_af += len(text_af)

    if len(text_af) == 0:
      non_text_count += 1

#    if tweet['source'] in sources:
#      non_text_count += 1
#      continue

print(total_count)
print(non_text_count)

print(length_af/length_be)
