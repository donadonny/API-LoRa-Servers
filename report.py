#!/bin/python2.7
# coding=utf-8

import time
import os
import json
from database import *
from cloud import *
from threading import Thread


def default(obj):
	import calendar, datetime

	if isinstance(obj, datetime.datetime):
		if obj.utcoffset() is not None:
			obj = obj - obj.utcoffset()
		millis = int(calendar.timegm(obj.timetuple()) * 1000 +obj.microsecond / 1000)
		return millis
	raise TypeError('Not sure how to serialize %s' % (obj,))


class Looper(Thread):
	"""
	This is the constructor for the Gateway object.
	It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
	:return: the gateway object itself
	"""
	def __init__(self, sql, iterations=1, period=1):
		self.me = Thread.__init__(self)
		self.iterations = iterations
		self.period = period
		self.sql = sql
		self.cloud = Cloud()


	def run(self):
		for i in range(self.iterations):
			time.sleep(self.period)
			results = Database("lora_customer").query(self.sql)
			if results is not None:
				print("\t["+str(i)+"] looper is sending: "+json.dumps(results, default=default))
				rt = self.cloud.post_data(json.dumps(results, default=default))
		print("\tquitting looper")
		sys.exit(0)


	def getPID(self):
		return os.getpid()





