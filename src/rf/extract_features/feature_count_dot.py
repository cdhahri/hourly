#!/usr/bin/python3

r = ['../data_tmp/train.csv','../data_tmp/test.csv']
w = ['../data_tmp/train/count_dot.json','../data_tmp/test/count_dot.json']

for i in range(2):
  with open(r[i], newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      out.append(row[5].count('.'))

  import json
  with open(w[i], 'w') as file:
    json.dump(out, file)
