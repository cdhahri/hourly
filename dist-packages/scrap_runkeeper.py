import requests
from pyquery import PyQuery

def home_page(url):
  try:
    r = requests.get(url)
    pq = PyQuery(r.text)
    return pq
  except Exception as e:
    print('[ERR] scrap_fitbit.home_page: {0}'.format(e))
    return None

def activities(html):
  return html('div#statsSection div').eq(0)('div.statValue').text()
  
def miles(html):
  return html('div#statsSection div').eq(2)('div.statValue').text()
  
def calories(html):
  return html('div#statsSection div').eq(4)('div.statValue').text()
