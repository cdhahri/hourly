#!/usr/bin/python3

r = ['../data_tmp/train.csv','../data_tmp/test.csv']
w = ['../data_tmp/train/exist_more_than_three_vowels.json','../data_tmp/test/exist_more_than_three_vowels.json']

for i in range(2):
  with open(r[i], newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      import re
      m = re.search('^.*(a{3,}|i{3,}|u{3,}|e{3,}|o{3,}).*$', row[5])
      out.append(bool(m))

  import json
  with open(w[i], 'w') as file:
    json.dump(out, file)
