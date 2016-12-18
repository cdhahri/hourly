#!/usr/bin/python3

r = ['./data_tmp/train/all_words0_out.txt','./data_tmp/test/all_words0_out.txt']
w = ['./data_tmp/train/all_words.json','./data_tmp/test/all_words.json']

for i in range(2):
  with open(r[i], newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter='\t')
    out = {}
    for row in csv_reader:
      out[row[2]] = [row[0], row[1]]

  import json
  with open(w[i], 'w') as file:
    json.dump(out, file)
