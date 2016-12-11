#!/usr/bin/python

import datetime, json, schedule, time

import db
import api_foursquare

import config
token = config.load_token('/vagrant/config/foursquare.json')

def job():
  now = datetime.datetime.now() + datetime.timedelta(0, 60)
  time_id = '{:%Y-%m-%d-%H}'.format(now)
  print(time_id)
  users = db.user__read__all()
  for twitter_id, meta in users.items():
    user = api_foursquare.user(token, meta['foursquare_id']) # get user profile
    if user is None:
      continue
    tips = []
    if meta['foursquare_last'] is not None:
      this_count = user['tips']['count']
      last_count = db.history_foursquare__read__tip_count(twitter_id, meta['foursquare_last'])
      count = this_count - last_count
      if count > 0:
        tips = api_foursquare.user_tips(token, meta['foursquare_id'], count) # get user tips
    import util_foursquare
    tip_ids = util_foursquare.tip_ids(tips)
    db.history_foursquare__create(twitter_id, time_id, json.dumps({'profile':user,'tweets':tip_ids}, sort_keys=True))
    db.tip__create__batch(tips)
    db.user__update__foursquare_last(twitter_id, time_id)

now = datetime.datetime.now()
next_hour = datetime.datetime(now.year, now.month, now.day, now.hour+1, 0)
delta = next_hour - now
time.sleep(delta.seconds)
schedule.every().hour.do(job)
job()
while True:
  schedule.run_pending()
  time.sleep(1)
