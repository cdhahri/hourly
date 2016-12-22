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

def venue(token, latitude, longitude):
  url = 'https://api.foursquare.com/v2/venues/search'
  ll = '{},{}'.format(latitude, longitude)
  params = {'ll': ll, 'oauth_token': token, 'v':'20161116'}
  try:
    r = requests.get(url, params=params)
    venues =  json.loads(r.text)['response']['venues']
    if len(venues) == 0:
      return None
    return venues[0]
  except Exception as e:
    print('[ERR] api_foursquare.venue: {0}'.format(e))
    return None

def venue_category(token, venue_id):
  url = 'https://api.foursquare.com/v2/venues/' + venue_id
  params = {'oauth_token': token, 'v':'20161116'}
  try:
    while True:
      r = requests.get(url, params=params)
      if r.status_code == 403:
        import time 
        print('[ERR] api_foursquare.venue_category: {0}'.format(r.text))
        time.sleep(120)
        continue
      venue =  json.loads(r.text)['response']['venue']
      primary = None
      for category in venue['categories']:
        if 'primary' in category and category['primary'] == True:
          primary = category['name']
      return primary
  except Exception as e:
    print('[ERR] api_foursquare.venue_category: {0}'.format(e))
    return None
