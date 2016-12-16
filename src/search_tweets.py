#!/usr/bin/python

import time

import config
token = config.load_token('/vagrant/config/twitter.json')

import json
# tweets
with open('tweets.json') as file:
  tweets = json.load(file)
# queries
with open('queries.json') as file:
  queries = json.load(file)

import requests
while True:
  for query in queries:
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    headers= {'Authorization': 'Bearer ' + token}
    params = {'q': query['q'], 'lang': 'en', 'result_type': 'recent', 'count': 100, 'since_id': query['since_id']}
    try:
      r = requests.get(url, params=params, headers=headers)    
    except Exception as e:
      continue
    if r.status_code is 200:
      tweets_remote = json.loads(r.text)
      for status in tweets_remote['statuses']:
        status['X_tag'] = query['tag']
        status['X_user'] = status['user']['id_str']
        for key in ['contributors', 'favorited', 'geo', 'id', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_user_id', 'metadata', 'retweeted', 'user']:
          if key in status:
            del status[key]
      tweets.extend(tweets_remote['statuses'])
      query['since_id'] = tweets_remote['search_metadata']['max_id_str']
      with open('tweets.json', 'w') as file:
        json.dump(tweets, file, sort_keys=True)
      with open('queries.json', 'w') as file:
        json.dump(queries, file, sort_keys=True)
    elif r.status_code is 429:
      print('[CODE] ' + str(r.status_code) + ' [TEXT] ' + r.text)
      time.sleep(120)
    else:
      print('[CODE] ' + str(r.status_code) + ' [TEXT] ' + r.text)
    time.sleep(10)
