#!/usr/bin/python3

import json
  
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

def process(r):
  try:
    with open(r, 'r') as file:
      targets = json.load(file)
  except FileNotFoundError as e:
    return

  neg = 0
  all = 0
  for target in targets:
    if target == '0':
      neg += 1
    all += 1
  ratio = neg / all
  if ratio > 0.1:
    print(neg/all)  

for user_id in ids:
  r = '/vagrant/data/osn-data/features_step1/{}target.json'.format(user_id)
  process(r)


#path = '/vagrant/data/osn-data/tweets/mentions/past_tweets'
#from os import listdir
#from os.path import isfile, join
#files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.json')]

#for f in files:
#  import re
#  user_id = re.search('^(.*)\.json$', f).group(1)
#  r = '/vagrant/data/osn-data/tweets/mentions/past_tweets/{}.json'.format(user_id)
#  w = '/vagrant/data/osn-data/tweets/mentions/past_tweets/csv/{}.csv'.format(user_id)
#  process(r, w)
