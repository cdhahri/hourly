import json, requests

def user(token, user_id):
  url = 'https://api.foursquare.com/v2/users/' + user_id
  params = {'oauth_token': token, 'v':'20161116'}
  try:
    r = requests.get(url, params=params)
    return json.loads(r.text)['response']['user']
  except Exception as e:
    print('[ERR] api_foursquare.user: {0}'.format(e))
    return None

def user_tips(token, user_id, count):
  url = 'https://api.foursquare.com/v2/lists/' + user_id + '/tips'
  params = {'oauth_token': token, 'limit':count, 'sort':'recent', 'v':'20161116'}
  try:
    r = requests.get(url, params=params)
    return json.loads(r.text)['response']['list']['listItems']['items']
  except Exception as e:
    print('[ERR] api_foursquare.user_tips: {0}'.format(e))
    return []