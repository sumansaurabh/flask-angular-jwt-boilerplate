# -*- coding: utf-8 -*-
"""
routes.home.py
~~~~~~

:copyright: (c) 2014
"""
from flask import (Blueprint, current_app, render_template,
				   request, send_from_directory, jsonify)
import flask
import requests

from Models.User import User
import config
from Base_controller import login_required, jsonify_resp

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from oauth2client.client import OAuth2WebServerFlow
import logging																																										
import sys

logging.StreamHandler(sys.stdout)
logging.basicConfig(level=logging.DEBUG)

import json

home = Blueprint('home', __name__)

client_secret_google = json.loads(
	open('./config/client_secret_google.json', 'r').read())


@home.route('/')
def index():
	"""Redirect to the AngularJS entry."""
	print("sdkjjdjksgdsgnd ---------- ")
	# print(current_app.db)
	# users = config.db.session.query(User).all()
	# for user in users:
	# 	print(user)
	# return u"<br>".join([u"{0}: {1}".format(user.email) for user in users])
	return render_template('index.html')


@home.route('/auth/signup', methods=['POST'])
def signup():
	data = request.json

	email = data["email"]
	password = data["password"]

	user = User(email=email, password=password)

	print(user)
	config.db.session.add(user)
	config.db.session.commit()

	return jsonify(token=user.token())

@home.route('/auth/google', methods=['POST'])
@jsonify_resp
def signup_google():
	data = request.json
	from pprint import pprint
	pprint(data)
	code = request.data
	oauth_flow = flow_from_clientsecrets('./config/client_secret_google.json', scope='')
	pprint(oauth_flow)
	oauth_flow.redirect_uri = 'http://localhost:5000'
	credentials = oauth_flow.step2_exchange(data)
	access_token = credentials.access_token
	url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'% access_token)

	print("access_token ->",access_token)
	print("url ->",url)
	result = json.loads(requests.get(url).text)

	pprint(result)

	email = result['email']
	password = result['user_id']

	user = User(email=email, password=password)

	print(user)
	config.db.session.add(user)
	config.db.session.commit()

	return {"token":user.token()}, 200


	# flow = OAuth2WebServerFlow(client_id=client_secret_google['web']['client_id'],
 #                           client_secret=client_secret_google['web']['client_secret'],
 #                           scope='',
 #                           redirect_uri='http://localhost:5000')
	# credentials = flow.step2_exchange(code)


	# try:
	# 	# Upgrade the authorization code into a credentials object
	# 	oauth_flow = flow_from_clientsecrets('./config/client_secret_google.json', scope='')
	# 	pprint(oauth_flow)
	# 	oauth_flow.redirect_uri = 'postmessage'
	# 	credentials = oauth_flow.step2_exchange(code)
	# except FlowExchangeError:
	# 	return {"eoro":"er"}, 400




	return {}, 200


@home.route('/auth/login', methods=['POST'])
def login():
	data = request.json

	email = data.get("email")
	password = data.get("password")

	user = config.db.session.query(User).filter_by(email=email).first()
	print(user)
	if not user:
		return jsonify(error="No such user"), 404

	if user.password == password:
		return jsonify(token=user.token()), 200
	else:
		return jsonify(error="Wrong email or password"), 400


@home.route('/robots.txt/')
@home.route('/sitemap.xml/')
@home.route('/favicon.ico/')
def static_from_root():
	"""Serves static resources."""
	return send_from_directory(current_app.static_folder, request.path[1:])


@home.route('/<path:path>')
def send_fonts(path):
	x = current_app.static_folder +'/dist/'
	return send_from_directory(x, path)