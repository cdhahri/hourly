#!/usr/bin/python3

import json
with open('./data_tmp/test/target.json', 'r') as file:
  target = json.load(file)

with open('./data_tmp/test.csv', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  hashset = {}
  i = -1
  for row in csv_reader:
    print(row[5].encode('utf-8'))
    i += 1
    print(target[i])
