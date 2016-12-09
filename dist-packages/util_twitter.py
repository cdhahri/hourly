def tweet_ids(tweets):
  ids = []
  if tweets is not None:
    for tweet in tweets:
      ids.append(tweet['id_str'])
  ids.sort()
  return ids
