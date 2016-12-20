#!/usr/bin/python

import json

with open('/vagrant/src/rf/data_tmp/pearson/hashtags_exist.json', 'r') as file:
  f1 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/mentions_exist.json', 'r') as file:
  f2 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/media_exist.json', 'r') as file:
  f3 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/day.json', 'r') as file:
  f4 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/week.json', 'r') as file:
  f5 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/favorite_count.json', 'r') as file:
  f6 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/retweet_count.json', 'r') as file:
  f7 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/source.json', 'r') as file:
  f8 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/top_mentions.json', 'r') as file:
  f9 = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/target.json', 'r') as file:
  ft = json.load(file)


import csv
w = '/vagrant/src/rf/data_tmp/weka_in.csv'
with open(w, 'w', newline='', encoding='utf-8') as file:
  csv_writer = csv.writer(file, delimiter=',')
  csv_writer.writerow(['hashtags_exist','mentions_exist','media_exist','day','week','favorite_count','retweet_count','source','target'])
  for i in range(len(ft)):
    csv_writer.writerow([f1[i],f2[i],f3[i],f4[i],f5[i],f6[i],f7[i],f8[i],ft[i]])
