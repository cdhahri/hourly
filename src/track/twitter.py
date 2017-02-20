#!/usr/bin/python

import datetime, json, schedule, time

import db
import api_twitter

import config
token = config.load_token('/vagrant/config/twitter.json')

def job():
  now = datetime.datetime.now() + datetime.timedelta(0, 60)
  time_id = '{:%Y-%m-%d-%H}'.format(now)
  print(time_id)
  users = db.user__read__all()
  for twitter_id, meta in users.items():
    user = None
#    user = api_twitter.user(token, twitter_id) # get user profile
#    if user is None:
#      continue
    tweets = api_twitter.user_tweets(token, twitter_id, meta['since_id']) # get user tweets
    import util_twitter
    tweet_ids = util_twitter.tweet_ids(tweets)
    db.history_twitter__create(twitter_id, time_id, json.dumps({'profile':user,'tweets':tweet_ids}, sort_keys=True))
    db.tweet__create__batch(tweets)
    if len(tweet_ids) > 0:
      since_id = tweet_ids[-1]
      db.user__update__since_id(twitter_id, since_id)

now = datetime.datetime.now()
next_hour = datetime.datetime(now.year, now.month, now.day, now.hour+1, 0)
delta = next_hour - now
time.sleep(delta.seconds)
schedule.every().hour.do(job)
job()
while True:
  schedule.run_pending()
  time.sleep(1)
