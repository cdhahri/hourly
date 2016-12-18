#!/usr/bin/python3

r = ['../data_tmp/train.csv','../data_tmp/test.csv']
w = ['../data_tmp/train/count_all_capital.json','../data_tmp/test/count_all_capital.json']

for i in range(2):
  with open(r[i], newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      words = row[5].split()
      all_capital = 0
      for word in words:
        if len(word) > 3 and word.isupper():
          all_capital += 1
      out.append(all_capital)

  import json
  with open(w[i], 'w') as file:
    json.dump(out, file)
