#!/usr/bin/python

import json

import db

tweets = db.tweet__read_all()

with open('./7.json', 'w') as file:
    json.dump(tweets, file, sort_keys=True)
