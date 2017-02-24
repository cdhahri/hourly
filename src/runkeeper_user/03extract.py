#!/usr/bin/python3

import json

#with open('./data/runkeeper.json.2', 'r') as file:
with open('./data/runkeeper.json', 'r') as file:
  data = json.load(file)

runkeepers = data['tweets']

#print('INSERT INTO `user` (twitter_id, runkeeper_url) VALUES ')

for runkeeper in runkeepers:
#  if 'url_expanded' in runkeeper:
#    print('(\'{}\', \'https://runkeeper.com/user/{}/profile\'),'.format(runkeeper['user_name'], runkeeper['url_expanded']))
  print(runkeeper['id'])

#print(';')
