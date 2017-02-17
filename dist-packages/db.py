import MySQLdb

# naming pattern: <table name>__<crud operation>__<no restriction>

#
# user
#
def user__read__all():
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('SELECT twitter_id, since_id, fitbit_url, foursquare_id, foursquare_last FROM user;')
    results = cursor.fetchall()
    users = {}
    for result in results:
      twitter_id = result[0]
      since_id = result[1]
      fitbit_url = result[2]
      foursquare_id = result[3]
      foursquare_last = result[4]
      if since_id is None:
        since_id = -1
      users[twitter_id] = {'since_id':since_id,'fitbit_url':fitbit_url,'foursquare_id':foursquare_id,'foursquare_last':foursquare_last}
    return users
  except Exception as e:
    print('[ERR] db.user__read__all: {0}'.format(e))
    return {}
  finally:
    db.close()

def user__update__since_id(twitter_id, since_id):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('UPDATE user SET since_id=%s WHERE twitter_id=%s;', (since_id, twitter_id))
    db.commit()
  except Exception as e:
    print('[ERR] db.user__update__since_id: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

def user__update__foursquare_last(twitter_id, foursquare_last):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('UPDATE user SET foursquare_last=%s WHERE twitter_id=%s;', (foursquare_last, twitter_id))
    db.commit()
  except Exception as e:
    print('[ERR] db.user__update__foursquare_last: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

#
# history_twitter
#
def history_twitter__create(twitter_id, time_id, data):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('INSERT INTO history_twitter (twitter_id,time_id,data) VALUES (%s,%s,%s)', (twitter_id, time_id, data))
    db.commit()
  except Exception as e:
    print('[ERR] db.history_twitter__create: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

def history_twitter__read(twitter_id, from_time_id, to_time_id):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('SELECT time_id, data FROM history_twitter WHERE twitter_id = %s AND time_id >= %s AND time_id <= %s ORDER BY time_id;', (twitter_id, from_time_id, to_time_id))
    results = cursor.fetchall()
    activity = []
    for result in results:
      activity.append({'time_id':result[0], 'data':result[1]})
    return activity
  except Exception as e:
    print('[ERR] db.history_twitter__read: {0}'.format(e))
    return []
  finally:
    db.close()

#
# tweet
#
def tweet__create(tweet):
  tweet_id = tweet['id_str']
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    import json
    cursor.execute('INSERT INTO tweet (tweet_id,tweet) VALUES (%s,%s)', (tweet_id, json.dumps(tweet, sort_keys=True)))
    db.commit()
  except Exception as e:
    print('[ERR] db.tweet__create: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

def tweet__create__batch(tweets):
  if tweets is not None:
    for tweet in tweets:
      tweet__create(tweet)

def tweet__read(tweet_id):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('SELECT tweet FROM tweet WHERE tweet_id = {}'.format(tweet_id))
    row = cursor.fetchone()
    import json
    tweet = json.loads(row[0])
    return tweet
  except Exception as e:
    print('[ERR] db.tweet__read: {0}'.format(e))
    return None
  finally:
    db.close()

#
# history_runkeeper
#
def history_runkeeper__create(twitter_id, time_id, data):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('INSERT INTO history_runkeeper (twitter_id,time_id,data) VALUES (%s,%s,%s)', (twitter_id, time_id, data))
    db.commit()
  except Exception as e:
    print('[ERR] db.history_runkeeper__create: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

#
# history_fitbit
#
def history_fitbit__create(twitter_id, time_id, data):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('INSERT INTO history_fitbit (twitter_id,time_id,data) VALUES (%s,%s,%s)', (twitter_id, time_id, data))
    db.commit()
  except Exception as e:
    print('[ERR] db.history_fitbit__create: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

def history_fitbit__read(twitter_id, from_time_id, to_time_id):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('SELECT time_id, data FROM history_fitbit WHERE twitter_id = %s AND time_id >= %s AND time_id <= %s ORDER BY time_id;', (twitter_id, from_time_id, to_time_id))
    results = cursor.fetchall()
    activity = []
    for result in results:
      activity.append({'time_id':result[0], 'data':result[1]})
    return activity
  except Exception as e:
    print('[ERR] db.history_fitbit__read: {0}'.format(e))
    return []
  finally:
    db.close()

#
# history_foursquare
#
def history_foursquare__create(twitter_id, time_id, data):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('INSERT INTO history_foursquare (twitter_id,time_id,data) VALUES (%s,%s,%s)', (twitter_id, time_id, data))
    db.commit()
  except Exception as e:
    print('[ERR] db.history_foursquare__create: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

def history_foursquare__read__tip_count(twitter_id, time_id):
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('SELECT data FROM history_foursquare WHERE twitter_id = %s AND time_id = %s', (twitter_id, time_id))
    row = cursor.fetchone()
    import json
    data = json.loads(row[0])
    return data['profile']['tips']['count']
  except Exception as e:
    print('[ERR] db.history_foursquare__read__tip_count: {0}'.format(e))
    return None
  finally:
    db.close()

#
# tip
#
def tip__create(tip):
  tip_id = tip['id']
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    import json
    cursor.execute('INSERT INTO tip (tip_id,tip) VALUES (%s,%s)', (tip_id, json.dumps(tip, sort_keys=True)))
    db.commit()
  except Exception as e:
    print('[ERR] db.tip__create: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

def tip__create__batch(tips):
  if tips is not None:
    for tip in tips:
      tip__create(tip)

#
# tweet_sentiment
#
def tweet_sentiment__create(tweet):
  tweet_id = tweet['id_str']
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    import json
    cursor.execute('INSERT INTO tweet_sentiment (tweet_id,tweet) VALUES (%s,%s)', (tweet_id, json.dumps(tweet, sort_keys=True)))
    db.commit()
  except Exception as e:
    print('[ERR] db.tweet_sentiment__create: {0}'.format(e))
    db.rollback()
  finally:
    db.close()

def tweet_sentiment__create__batch(tweets):
  if tweets is not None:
    for tweet in tweets:
      tweet_sentiment__create(tweet)

def tweet_sentiment__read():
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('SELECT tweet FROM tweet_sentiment')
    results = cursor.fetchall()
    tweets = []
    for result in results:
      import json
      tweet = json.loads(result[0])
      tweets.append(tweet)
    return tweets
  except Exception as e:
    print('[ERR] db.tweet__read: {0}'.format(e))
    return None
  finally:
    db.close()
