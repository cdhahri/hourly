def tip_ids(tips):
  ids = []
  if tips is not None:
    for tip in tips:
      ids.append(tip['id'])
  ids.sort()
  return ids
