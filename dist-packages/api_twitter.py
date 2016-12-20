import json, requests

def user(token, user_id):
  url = 'https://api.twitter.com/1.1/users/show.json'
  params = {'user_id': user_id, 'include_entities': 'true'}
  headers= {'Authorization': 'Bearer ' + token}
  try:
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)
  except Exception as e:
    print('[ERR] api_twitter.user: {0}'.format(e))
    return None

def user_tweets(token, user_id, since_id):
  url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
  params = {'user_id':user_id,'trim_user':'true','exclude_replies':'true'}
  # 'include_rts':'true' check the user who tweeted this
  if since_id != -1:
    params['since_id'] = since_id
  headers= {'Authorization': 'Bearer ' + token}
  try:
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)
  except Exception as e:
    print('[ERR] api_twitter.user_tweets: {0}'.format(e))
    return []

def user_tweets_before(token, user_id, tweet_id, count):
  url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
  params = {'user_id':user_id,'count':count,'max_id':tweet_id,'trim_user':'true','exclude_replies':'true','include_rts':'false'}
  headers= {'Authorization': 'Bearer ' + token}
  try:
    while True:
      r = requests.get(url, params=params, headers=headers)
      if r.status_code == 429:
        import time
        time.sleep(120)
      else:
        break
    return json.loads(r.text)
  except Exception as e:
    print('[ERR] api_twitter.user_tweets_before: {0}'.format(e))
    return []

def user_tweets_max_id(token, screen_name, count, max_id):
  url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
  params = {'screen_name':screen_name,'count':count,'trim_user':'true','exclude_replies':'true','include_rts':'false'}
  if max_id is not None:
    params['max_id'] = max_id
  headers= {'Authorization': 'Bearer ' + token}
  try:
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)
  except Exception as e:
    print('[ERR] api_twitter.user_tweets_max_id: {0}'.format(e))
    return []

def tweet(token, tweet_id):
  url = 'https://api.twitter.com/1.1/statuses/show.json'
  params = {'id': tweet_id, 'trim_user': 'false', 'include_my_retweet': 'false', 'include_entities': 'true'}
  headers= {'Authorization': 'Bearer ' + token}
  try:
    while True:
      r = requests.get(url, params=params, headers=headers)
      if r.status_code == 429:
        import time
        time.sleep(120)
      else:
        break
    return json.loads(r.text)
  except Exception as e:
    print('[ERR] api_twitter.tweet: {0}'.format(e))
    return None
