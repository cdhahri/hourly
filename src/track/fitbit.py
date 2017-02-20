#!/usr/bin/python

import datetime, json, schedule, time

import db
import scrap_fitbit

def job():
  now = datetime.datetime.now() + datetime.timedelta(0, 60)
  time_id = '{:%Y-%m-%d-%H}'.format(now)
  print(time_id)
  users = db.user__read__all()
  for twitter_id, meta in users.items():
    if meta['fitbit_url'] is None:
      continue
    html = scrap_fitbit.home_page(meta['fitbit_url'])
    if html is None:
      continue
    data = {
      'profile_description': scrap_fitbit.profile_desc(html),
      'profile_image': scrap_fitbit.profile_image(html),
      'location': scrap_fitbit.location(html),
      'height': scrap_fitbit.height(html),
      'lifetime_steps': scrap_fitbit.lifetime_steps(html),
      'lifetime_floors': scrap_fitbit.lifetime_floors(html),
      'lifetime_distance': scrap_fitbit.lifetime_distance(html)
    }
    db.history_fitbit__create(twitter_id, time_id, json.dumps(data, sort_keys=True))

now = datetime.datetime.now()
next_hour = datetime.datetime(now.year, now.month, now.day, now.hour+1, 0)
delta = next_hour - now
time.sleep(delta.seconds)
schedule.every().hour.do(job)
job()
while True:
  schedule.run_pending()
  time.sleep(1)
