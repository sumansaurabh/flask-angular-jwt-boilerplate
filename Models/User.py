from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from jwt import DecodeError, ExpiredSignature
from datetime import datetime, timedelta
import jwt
from jwt import DecodeError, ExpiredSignature
import config

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	email = Column(String(100), nullable=False)
	password = Column(String(100))

	def token(self):
		payload = {
			'sub': self.email,
			'iat': datetime.utcnow(),
			'exp': datetime.utcnow() + timedelta(days=14)
		}
		token = jwt.encode(payload, config.TOKEN_SECRET)
		return token.decode('unicode_escape')
		
	def __repr__(self):
		return '<User %r>' % (self.email)


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     email = Column(String(120), unique=True)

#     def __init__(self, name=None, email=None):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % (self.name)