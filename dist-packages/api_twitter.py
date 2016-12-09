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
  if since_id != -1:
    params['since_id'] = since_id
  headers= {'Authorization': 'Bearer ' + token}
  try:
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)
  except Exception as e:
    print('[ERR] api_twitter.user_tweets: {0}'.format(e))
    return []
