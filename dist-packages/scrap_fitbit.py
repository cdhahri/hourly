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

def profile_desc(html):
 return html('div.content.firstContent').text()

def profile_image(html):
  return html('img.profileImage').attr['src']

def location(html):
  return html('li.user-stat.location').text()

def height(html):
  return html('li.user-stat.height').text()

def lifetime_achievements(html):
  return html('div#achievementsLifetime')

def lifetime_steps(html):
  lifetime = lifetime_achievements(html)
  steps = lifetime('div.tabsData.steps')
  return steps('span.value').text()

def lifetime_floors(html):
  lifetime = lifetime_achievements(html)
  floors = lifetime('div.tabsData.floor')
  return floors('span.value').text()

def lifetime_distance(html):
  lifetime = lifetime_achievements(html)
  distance = lifetime('div.tabsData.distance')
  return distance('span.value').text()
