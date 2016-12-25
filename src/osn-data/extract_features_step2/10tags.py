#!/usr/bin/python3

import json

month = {
 'Jan': '01',
 'Feb': '02',
 'Mar': '03',
 'Apr': '04',
 'May': '05',
 'Jun': '06',
 'Jul': '07',
 'Aug': '08',
 'Sep': '09',
 'Oct': '10',
 'Nov': '11',
 'Dec': '12',
}

with open('/vagrant/data/osn-data/user_4sqcheckins.csv', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  byday = {}
  for row in csv_reader:
    user_id = row[0]
    import os.path
    if not os.path.exists('/vagrant/data/osn-data/venues/{}.json'.format(user_id)):
      continue
    byday = {}
    if os.path.exists('/vagrant/data/osn-data/features_step2/{}tags.json'.format(user_id)):
      with open('/vagrant/data/osn-data/features_step2/{}tags.json'.format(user_id), 'r') as file:
        byday = json.load(file)
    with open('/vagrant/data/osn-data/venues/{}.json'.format(user_id), 'r') as file:
      venue_categories = json.load(file)
    venue_id = row[2]
    if venue_id not in venue_categories:
      continue
    category = venue_categories[venue_id]
    with open('/vagrant/data/osn-data/tweets/{}.json'.format(user_id), 'r') as file:
      tweets = json.load(file)
    tweet_id = row[1]
    tweet = tweets[tweet_id]
    if tweet is None or 'created_at' not in tweet:
      continue
    created_at = tweet['created_at']
    import re
    #Mon Sep 26 22:47:22 +0000 2016
    m = re.search('^.{3} (.{3}) (.{2}) .{8} \+.{4} (.{4})$', created_at)
    key = '{}-{}-{}'.format(m.group(3), month[m.group(1)], m.group(2))
    if key not in byday:
      byday[key] = []
    byday[key].append(category)
    with open('/vagrant/data/osn-data/features_step2/{}tags.json'.format(user_id), 'w') as file:
      json.dump(byday, file)
