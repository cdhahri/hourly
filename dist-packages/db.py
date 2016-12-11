import MySQLdb

# naming pattern: <table name>__<crud operation>__<no restriction>

#
# user
#
def user__read__all():
  try:
    db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='hourly')
    cursor = db.cursor()
    cursor.execute('SELECT twitter_id, since_id, fitbit_url FROM user;')
    results = cursor.fetchall()
    users = {}
    for result in results:
      twitter_id = result[0]
      since_id = result[1]
      fitbit_url = result[2]
      if since_id is None:
        since_id = -1
      users[twitter_id] = {'since_id':since_id,'fitbit_url':fitbit_url}
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
