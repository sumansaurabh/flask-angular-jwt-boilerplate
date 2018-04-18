# -*- coding: utf-8 -*-
"""
routes.home.py
~~~~~~

:copyright: (c) 2014
"""
from flask import (Blueprint, current_app, render_template,
				   request, send_from_directory, jsonify)
import flask

from Models.User import User
import config
from Base_controller import login_required


home = Blueprint('home', __name__)


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