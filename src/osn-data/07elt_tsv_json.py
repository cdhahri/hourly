#!/usr/bin/python3

import json
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

def process(r, w):
  with open(r, newline='', encoding='latin-1') as file:
    import csv
    ok = True
    try:
      csv_reader = csv.reader(file, delimiter='\t')
    except Exception as e:
      ok = False
    if ok:
      out = {}
      first_line = True
      for row in csv_reader:
        if first_line:
          first_line = False
          continue
        out[row[2]] = [row[0], row[1]]

  import json
  with open(w, 'w') as file:
    json.dump(out, file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/words/{}0_out.txt'.format(user_id)
  w = '/vagrant/data/osn-data/tweets/words/json/{}.json'.format(user_id)
  try:
    process(r, w)
  except Exception as e:
    print('{} {}'.format(user_id, e))

#path = '/vagrant/data/osn-data/tweets/mentions/past_tweets/words'
#from os import listdir
#from os.path import isfile, join
#files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('0_out.txt')]

#for f in files:
#  import re
#  user_id = re.search('^(.*)0_out\.txt$', f).group(1)
#  r = '/vagrant/data/osn-data/tweets/mentions/past_tweets/words/{}0_out.txt'.format(user_id)
#  w = '/vagrant/data/osn-data/tweets/mentions/past_tweets/words/json/{}.json'.format(user_id)
#  process(r, w)
