
db = None
TOKEN_SECRET = 'IQLECT_SECRET_KEY'

class Default(object):
  DEBUG = True

class Staging(Default):
  pass

class Production(Default):
  pass
