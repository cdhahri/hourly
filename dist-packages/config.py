import json, sys

def load_token(path):
  try:
    with open(path) as file:
      token = json.load(file)
    return token['token']
  except Exception as e:
    print('[ERR] config.load_token: {0}'.format(e))
    sys.exit(1)
