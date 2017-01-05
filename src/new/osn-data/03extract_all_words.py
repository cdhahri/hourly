#!/usr/bin/python3

import json
        
def process(r, w):
  with open(r, newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    hashset = {}
    for row in csv_reader:
      words = row[5].split()
      for word in words:
        hashset[word] = None

  # clean
  import re
  keys_to_delete = []
  for key in sorted(hashset.keys()):
    # remove hashtag from words
    m = re.match('^#(.+)$', key)
    if m is not None:
      hashset[m.group(1)] = None
      keys_to_delete.append(key)

  for key in keys_to_delete:
    del hashset[key]

  out = '\n'.join(sorted(hashset.keys()))

  with open(w, 'w', encoding='latin-1') as file:
    file.write(out)
  
with open('./ids.json', 'r') as file:
  ids = json.load(file)
  
for user_id in ids:
  r = './tweets_raw/csv/{}.csv'.format(user_id)
  w = './tweets_raw/words/{}.txt'.format(user_id)
  process(r, w)
