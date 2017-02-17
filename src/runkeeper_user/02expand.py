#!/usr/bin/python3

import json, re, requests

def expand(url):
  r = requests.head(url)
  if 'location' in r.headers:
    return r.headers['location']
  return url

with open('./data/runkeeper.json', 'r') as file:
  data = json.load(file)

runkeepers = data['tweets']
print(len(runkeepers))

i = 0
for runkeeper in runkeepers:
  i += 1
  print(i)
  url = runkeeper['url']
  url_expanded = expand('http://{}'.format(url))
  url_expanded = expand(url_expanded)
  url_expanded = expand(url_expanded)
  match = re.match('^/user/(.*)/activity/.*$', url_expanded)
  if match is None:
    print(url_expanded)
    continue
  url_expanded = match.group(1)
  runkeeper['url_expanded'] = url_expanded

with open('./data/runkeeper.json.2', 'w') as file:
  json.dump(data, file, sort_keys=True)
