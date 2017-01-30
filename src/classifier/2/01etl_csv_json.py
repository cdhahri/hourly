#!/usr/bin/python

sentiment_hash = {
    "0" :"-1",
    "4" : "1",
}

import csv, json, random

out = []

with open('./data/01raw.csv', newline='', encoding='latin1') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        if random.random() > 0.97:
            print('1')
            out.append({"mood":sentiment_hash[row[0]],"text":row[1]})

with open('./data/02.json', 'w') as file:
    json.dump(out, file, sort_keys=True)
