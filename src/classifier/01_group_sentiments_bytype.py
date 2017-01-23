#!/usr/bin/python

sentiment_hash = {
  "anger":-1,
  "boredom":-1,
  "empty":-1,
  "enthusiasm":1,
  "fun":1,
  "happiness":1,
  "hate":-1,
  "love":1,
  "neutral":0,
  "relief":1,
  "sadness":-1,
  "worry":-1,
}

import csv, json

out = []

with open('./data/01raw.csv', newline='', encoding='latin1') as file:
  csv_reader = csv.reader(file, delimiter=',')
  for row in csv_reader:
    if row[1] not in sentiment_hash:
      continue
    out.append({"mood":sentiment_hash[row[1]],"text":row[3]})

with open('./data/02.json', 'w') as file:
  json.dump(out, file, sort_keys=True)
