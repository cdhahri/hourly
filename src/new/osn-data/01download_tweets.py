#!/usr/bin/python

import requests, time
def tweets(token, user_id, count, max_id):
  url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
  params = {'user_id':user_id,'count':count,'trim_user':'true','exclude_replies':'false','include_rts':'true'}
  if max_id is not None:
    params['max_id'] = max_id
  headers = {'Authorization': 'Bearer ' + token}
  try:
    while True:
      r = requests.get(url, params=params, headers=headers)
      if r.status_code == 429:
        time.sleep(120)
        continue
      if r.status_code != 200:
        return None
      return json.loads(r.text)
  except Exception as e:
    print('[ERR] {0}'.format(e))
    return None

import config
token = config.load_token('/vagrant/config/twitter.json')

import json
with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  print('BEGIN {}'.format(user_id))

  import os.path
  if os.path.exists('./tweets_raw/{}.json'.format(user_id)):
    continue

  tweets_hash = {}

  remote_tweet = tweets(token, user_id, '1', None)
  if remote_tweet is None or len(remote_tweet) == 0:
    print('FAIL {} unable to get first tweet'.format(user_id))
    continue

  remote_tweet = remote_tweet[0]
  if 'id_str' not in remote_tweet:
    print('FAIL {} id_str not in first tweet'.format(user_id))
    continue

  max_id = remote_tweet['id_str']
  tweets_hash[remote_tweet['id_str']] = remote_tweet

  i = 0
  while True:
    i += 1
    if i > 10:
      break
    remote_tweets = tweets(token, user_id, '200', max_id)
    if remote_tweets is None:
      print('FAIL {}'.format(user_id))
      continue
    print(len(remote_tweets))
    for remote_tweet in remote_tweets:
      if 'id_str' not in remote_tweet:
        print('WARN {} id_str not in tweet'.format(user_id))
        continue
      if remote_tweet['id_str'] < max_id:
        max_id = remote_tweet['id_str']
      tweets_hash[remote_tweet['id_str']] = remote_tweet

  with open('./tweets_raw/{}.json'.format(user_id), 'w') as file:
    json.dump(tweets_hash, file, sort_keys=True)

  print('END {}'.format(user_id))
