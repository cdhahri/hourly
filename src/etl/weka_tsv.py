#!/usr/bin/python

import json

r1 = '/vagrant/src/rf/data_tmp/test/features.json'
with open(r1, 'r') as file:
  features = json.load(file)

r2 = '/vagrant/src/rf/data_tmp/pearson/target.json'
with open(r2, 'r') as file:
  target = json.load(file)

import csv
w = '/vagrant/src/rf/data_tmp/weka_in.csv'
with open(w, 'w', newline='', encoding='utf-8') as file:
  csv_writer = csv.writer(file, delimiter=',')
  for i in range(len(features)):
    csv_writer.writerow([features[i][0],features[i][1],features[i][2],features[i][3],features[i][4],features[i][5],features[i][6],target[i]])
