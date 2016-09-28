#!/bin/python2.7
# coding=utf-8

import mysql.connector as mariadb
from config import Config


class Database():
	"""
	This is the constructor for the Gateway object.
	It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
	:return: the gateway object itself
	"""
	def __init__(self, database):
		cnf = Config()
		self.user = cnf.get_mysql_credentials()['username']
		self.password = cnf.get_mysql_credentials()['password']
		self.database = database

		self.mariadb_connection = mariadb.connect(user=self.user, password=self.password, database=self.database)
		self.cursor = self.mariadb_connection.cursor()


	def query(self, sql_stmt):
		try:
			self.cursor.execute(sql_stmt)
		except mariadb.Error as error:
			print("Error: {}".format(error))
		if self.cursor.with_rows:
			rows = self.cursor.fetchall()
			if self.cursor.rowcount >= 1:
				return rows


	def close(self):
		self.mariadb_connection.commit()
		self.cursor.close()
		self.mariadb_connection.close()
		
