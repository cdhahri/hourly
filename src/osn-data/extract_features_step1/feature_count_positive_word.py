#!/usr/bin/python3

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 1007531, 101496212, 1021239846, 102464379, 103114245, 103695733, 10449052, 104852013, 10521002, 106104712, 108944858, 109223169, 10929372, 109485267, 110808568, 111178547, 11126582, 111454868, 112490071, 112858627, 11312992, 113441429, 11346942, 11437162, 114978482, 115073079, 115138473, 115171979, 11661442, 117093537, 117562901, 117567036, 1177083624, 11778632, 117870724, 117987103, 118459389, 118474054, 11922222, 119436439, 119773854, 11987272, 119979433, 120268489, 12091872, 121768977, 122737979, 123059038, 1231465759, 1236198937, 123745496]

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/csv/{}.csv'.format(user_id)
  w = '/vagrant/data/osn-data/features_step1/{}count_positive_word.json'.format(user_id)

  words_path = '/vagrant/data/osn-data/tweets/words/json/{}.json'.format(user_id)

  with open(words_path, 'r') as file:
    all_words = json.load(file)
  
  with open(r, newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      words = row[5].split()
      positive = 0
      for word in words:
        if word in all_words:
          score = int(all_words[word][0]) - abs(int(all_words[word][1]))
          if score > 0:
            positive += 1
      out.append(positive)

  with open(w, 'w') as file:
    json.dump(out, file)
