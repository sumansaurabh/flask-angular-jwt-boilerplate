# -*- coding: utf-8 -*-
"""
routes.api.py
~~~~~~

:copyright: (c) 2014
"""
from flask import Blueprint, jsonify
from Base_controller import login_required


api = Blueprint('api', __name__)

@api.route('/api/get_cofee', methods=['GET'])
@login_required
def coffee_shop_list():
	"""Checkk authentication flow"""
	return jsonify({'hello': "I am your coffee"})

