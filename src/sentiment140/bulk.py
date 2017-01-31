#!/usr/bin/python

import json, requests

url = 'http://www.sentiment140.com/api/bulkClassifyJson'
params = {'appid':'marouen.jilani@gmail.com'}
body = {'data':[{'text':'I love Titanic.'}]}
try:
  r = requests.post(url, params=params, json=body)
  print(r.text)
#  print(json.loads(r.text))
except Exception as e:
  print('[ERR] {0}'.format(e))
