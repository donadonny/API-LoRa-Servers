#!/bin/python2.7
# coding=utf-8

import json


class Config():
	"""
	This is the constructor for the Gateway object.
	It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
	:return: the gateway object itself
	"""
	def __init__(self):
		f = open('config.json', 'r')
		try:
			self.config_data = json.load(f)
		except FileNotFoundError:
			print("File was not found")


	def get_post_url(self):
		return self.config_data['post_url']

	def get_get_url(self):
		return self.config_data['get_url']

	def get_aws_credentials(self):
		return self.config_data['awsCredentials']

	def get_mysql_credentials(self):
		return self.config_data['mysql_credentials']

	def get_ipns(self):
		return self.config_data['ipns']

	def get_ipas(self):
		return self.config_data['ipas']

	def get_ipcs(self):
		return self.config_data['ipcs']

	def get_ipnc(self):
		return self.config_data['ipnc']

