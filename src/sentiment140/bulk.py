#!/usr/bin/python

import json, requests

# with open('/vagrant/src/new/osn-data/ids.json', 'r') as file:
with open('/vagrant/src/track/data/ids.json', 'r') as file:
	ids = json.load(file)

url = 'http://www.sentiment140.com/api/bulkClassifyJson'
params = {'appid':'marouen.jilani@gmail.com'}

for user_id in ids:
	print(user_id)

	# with open('/vagrant/src/new/osn-data/tweets_raw/{}.json'.format(user_id), 'r') as file:
	with open('/vagrant/src/track/data/tweets/{}.json'.format(user_id), 'r') as file:
		tweets_hash = json.load(file)

	data = []
	for key in sorted(tweets_hash.keys()):
		text = tweets_hash[key]['text']
		data.append({'text':text})

	body = {'data':data}

	try:
		r = requests.post(url, params=params, json=body)
		tweets = json.loads(r.text)['data']
		targets = []
		for tweet in tweets:
			targets.append(tweet['polarity'])
		# with open('./targets/{}.json'.format(user_id), 'w') as file:
		with open('/vagrant/src/track/data/tweets/targets/{}.json'.format(user_id), 'w') as file:
			json.dump(targets, file)
	except Exception as e:
		print('[ERR] {0}'.format(e))
