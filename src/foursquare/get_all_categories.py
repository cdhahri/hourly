#!/usr/bin/python

import config
token = config.load_token('/vagrant/config/foursquare.json')

from api_foursquare import category_hierarchy
categories = category_hierarchy(token)

import json
with open('/vagrant/data/osn-data/category_hierarchy.json', 'w') as file:
  json.dump(categories, file, sort_keys=True)
