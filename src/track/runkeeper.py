#!/usr/bin/python

import datetime, json, schedule, time

import db
import scrap_runkeeper

def job():
  now = datetime.datetime.now() + datetime.timedelta(0, 60)
  time_id = '{:%Y-%m-%d-%H}'.format(now)
  print(time_id)
  users = db.user__read__all()
  for twitter_id, meta in users.items():
    if meta['runkeeper_url'] is None:
      continue
    html = scrap_runkeeper.home_page(meta['runkeeper_url'])
    if html is None:
      continue
    data = {
      'activities': scrap_runkeeper.activities(html),
      'miles': scrap_runkeeper.miles(html),
      'calories': scrap_runkeeper.calories(html)
    }
    db.history_runkeeper__create(twitter_id, time_id, json.dumps(data, sort_keys=True))

now = datetime.datetime.now()
next_hour = datetime.datetime(now.year, now.month, now.day, now.hour+1, 0)
delta = next_hour - now
time.sleep(delta.seconds)
schedule.every().hour.do(job)
job()
while True:
  schedule.run_pending()
  time.sleep(1)
