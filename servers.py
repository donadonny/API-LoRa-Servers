#!/bin/python2.7
# coding=utf-8

import sys
import time
import subprocess
import shlex
from config import *
from threading import Thread


class Timer(Thread):

	def __init__(self, process, timeout):
		Thread.__init__(self)
		self.timeout = timeout
		self.process = process


	def run(self):
		time.sleep(self.timeout)
		self.process.terminate()
		sys.exit(0)


class Connector():
	"""
	This is the constructor for the Gateway object.
	It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
	:return: the gateway object itself
	"""
	def __init__(self):
		self.config_data = Config()
		self.ipNS = self.config_data.get_ipns()
		self.ipAS = self.config_data.get_ipas()
		self.ipCS = self.config_data.get_ipcs()
		self.ipNC = self.config_data.get_ipnc()
	

	def append(self, command, timeout):
		command_line = "../loracmd -ns "+str(self.ipNS)+" -as "+str(self.ipAS)+" -cs "+str(self.ipCS)+" -nc "+str(self.ipNC)
		args = shlex.split(command_line)
		process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		thread = Timer(process, timeout)
		thread.start()
		return process.communicate(command)