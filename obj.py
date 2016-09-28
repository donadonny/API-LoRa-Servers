#!/bin/python2.7
# coding=utf-8

import sys
from database import Database


class Gateway():
	"""
	This is the constructor for the Gateway object.
	It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
	:return: the gateway object itself
	"""
	def __init__(self, eui):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.eui = eui
		self.exist = False
		self.region = None
		self.maxTxPower_dBm = None
		self.allowGpsToSetPosition = None
		self.time = None
		self.latitude = None
		self.longitude = None
		self.altitude = None
		self.ntwkMaxDelayUp_ms = None
		self.ntwkMaxDelayDn_ms = None
		self.uppacketsreceived = None
		self.gooduppacketsreceived = None
		self.uppacketsforwarded = None
		self.uppacketsacknowedgedratio = None
		self.downpacketsreceived = None
		self.packetstransmitted = None
		self.lastuppacketid = None
		self.dspVersion = None
		self.fpgaVersion = None
		self.halVersion = None

		db = Database("lora_network")
		if db is not None:
			result = db.query("SELECT * FROM gateways WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
				self.exist = True
				self.region = result[0][1]
				self.maxTxPower_dBm = result[0][2]
				self.allowGpsToSetPosition = result[0][3]
				self.time = result[0][4]
				self.latitude = result[0][5]
				self.longitude = result[0][6]
				self.altitude = result[0][7]
				self.ntwkMaxDelayUp_ms = result[0][8]
				self.ntwkMaxDelayDn_ms = result[0][9]
				self.uppacketsreceived = result[0][10]
				self.gooduppacketsreceived = result[0][11]
				self.uppacketsforwarded = result[0][12]
				self.uppacketsacknowedgedratio = result[0][13]
				self.downpacketsreceived = result[0][14]
				self.packetstransmitted = result[0][15]
				self.lastuppacketid = result[0][16]
				self.dspVersion = result[0][17]
				self.fpgaVersion = result[0][18]
				self.halVersion = result[0][19]


	def add_cmd(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		command = "ns\n"
		if not self.exist:
			command = command+"gateway add "+str(self.eui)
		else:
			command = command+"gateway set "+str(self.eui)
		if self.region is not None:
			if self.region == 0:
				command = command+" region americas902"
			elif self.region == 1:
				command = command+" region china779"
			elif self.region == 2:
				command = command+" region europe433"
			elif self.region == 4:
				command = command+" region europe863"
		if self.latitude is not None:
			command = command+" lat "+str(self.latitude)
		if self.longitude is not None:
			command = command+" long "+str(self.longitude)
		if self.altitude is not None:
			command = command+" alt "+str(self.altitude)
		if self.allowGpsToSetPosition is not None:
			if self.allowGpsToSetPosition == True:
				command = command+" allowgps true"
			else:
				command = command+" allowgps false"
		if self.maxTxPower_dBm is not None:
			command = command+" pwr "+str(self.maxTxPower_dBm)
		if self.ntwkMaxDelayUp_ms is not None:
			command = command+" updelay_ms "+str(self.ntwkMaxDelayUp_ms)
		if self.ntwkMaxDelayDn_ms is not None:
			command = command+" downdelay_ms "+str(self.ntwkMaxDelayDn_ms)
		return command+"\n"


	def del_cmd(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		if not self.exist:
			pass
		else:
			command = "ns\ngateway delete "+str(self.eui)+"\n"
			return command


	def geteui(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.eui
	def getregion(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.region
	def getmaxTxPower_dBm(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.maxTxPower_dBm
	def getallowGpsToSetPosition(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.allowGpsToSetPosition
	def gettime(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.time
	def getlatitude(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.latitude
	def getlongitude(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.longitude
	def getaltitude(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.altitude
	def getntwkMaxDelayUp_ms(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.ntwkMaxDelayUp_ms
	def getntwkMaxDelayDn_ms(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.ntwkMaxDelayDn_ms
	def getuppacketsreceived(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.uppacketsreceived
	def getgooduppacketsreceived(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.gooduppacketsreceived
	def getuppacketsforwarded(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.uppacketsforwarded
	def getuppacketsacknowedgedratio(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.uppacketsacknowedgedratio
	def getdownpacketsreceived(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.downpacketsreceived
	def getpacketstransmitted(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.packetstransmitted
	def getlastuppacketid(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.lastuppacketid
	def getdspVersion(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.dspVersion
	def getfpgaVersion(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.fpgaVersion
	def gethalVersion(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.halVersion

	def setregion(self, region):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.region = region
	def setmaxTxPower_dBm(self, maxTxPower_dBm):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.maxTxPower_dBm = maxTxPower_dBm
	def setallowGpsToSetPosition(self, allowGpsToSetPosition):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.allowGpsToSetPosition = allowGpsToSetPosition
	def setlatitude(self, latitude):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.latitude = latitude
	def setlongitude(self, longitude):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.longitude = longitude
	def setaltitude(self, altitude):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.altitude = altitude
	def setntwkMaxDelayUp_ms(self, ntwkMaxDelayUp_ms):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.ntwkMaxDelayUp_ms = ntwkMaxDelayUp_ms
	def setntwkMaxDelayDn_ms(self, ntwkMaxDelayDn_ms):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.ntwkMaxDelayDn_ms = ntwkMaxDelayDn_ms



class Mote():
	"""
	This is the constructor for the Mote object.
	It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
	:return: the mote object itself
	"""
	def __init__(self, eui):
		self.eui = eui
		self.exist = False
		self.appeui = None
		self.classC = None
		self.networkAddress = None
		self.networkSessionKey = None
		self.downMsgSeqNo = None
		self.upMsgSeqNo = None
		self.applicationSessionKey = None

		db = Database("lora_network")
		if db is not None:
			result = db.query("SELECT * FROM motes WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
				self.exist = True
				self.appeui = str("{0:x}".format(result[0][1]))
				self.classC = result[0][2]
				self.networkAddress = str("{0:x}".format(result[0][3]))
				self.networkSessionKey = result[0][4]
				self.downMsgSeqNo = result[0][5]
				self.upMsgSeqNo = result[0][6]

		db = Database("lora_application")
		if db is not None:
			result = db.query("SELECT * FROM activemotes WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
				self.applicationSessionKey = result[0][3]


	def add_cmd(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		command = "as\n"
		#if not self.exist:
		command = command+"mote add "+str(self.eui)
		#else:
			#command = command+"mote set "+str(self.eui)
		command = command+" p app "+str(self.appeui)
		if self.networkAddress is not None:
			command = command+" netaddr "+str(self.networkAddress)
		if self.applicationSessionKey is not None:
			command = command+" key "+str(self.applicationSessionKey)
		if not self.exist:
			command = command+"\nnc\nmote add "+str(self.eui)+" app "+str(self.appeui)+"\n"
			command = command+"cs\nmote add "+str(self.eui)+" app "+str(self.appeui)+"\n"
		else:
			command = command+"\nnc\nmote set "+str(self.eui)+" app "+str(self.appeui)+"\n"
			command = command+"cs\nmote set "+str(self.eui)+" app "+str(self.appeui)+"\n"
		if not self.exist:
			command = command+"ns\nmote add "+str(self.eui)+" app "+str(self.appeui)
		else:
			command = command+"ns\nmote set "+str(self.eui)+" app "+str(self.appeui)
		if self.networkSessionKey is not None:
			command = command+" key "+str(self.networkSessionKey)
		if self.networkAddress is not None:
			command = command+" netaddr "+str(self.networkAddress)
		if self.classC is not None:
			if self.classC != 0:
				command = command+" class c"
		return command+"\n"


	def del_cmd(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		if not self.exist:
			pass
		else:
			command = "as\nmote delete "+str(self.eui)+"\nnc\nmote delete "+str(self.eui)+"\nns\nmote delete "+str(self.eui)+"\ncs\nmote delete "+str(self.eui)+"\n"
			return command


	def send_cmd(self, port, payload):
		if not self.exist:
			pass
		else:
			command = "cs\nmote send "+str(self.eui)+" port "+str(port)+" data "+str(payload)+"\n"
			return command


	def geteui(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.eui
	def getappeui(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.appeui
	def getexist(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.exist
	def getclassC(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.classC
	def getnetworkAddress(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.networkAddress
	def getnetworkSessionKey(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.networkSessionKey
	def getdownMsgSeqNo(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.downMsgSeqNo
	def getupMsgSeqNo(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.upMsgSeqNo
	def getapplicationSessionKey(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.applicationSessionKey

	def setappeui(self, appeui):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.appeui = appeui
	def setclassC(self, classC):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.classC = classC
	def setnetworkAddress(self, networkAddress):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.networkAddress = networkAddress
	def setnetworkSessionKey(self, networkSessionKey):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.networkSessionKey = networkSessionKey
	def setapplicationSessionKey(self, applicationSessionKey):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.applicationSessionKey = applicationSessionKey



class App():
	"""
	This is the constructor for the Gateway object.
	It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
	:return: the gateway object itself
	"""
	def __init__(self, eui):
		self.eui = eui
		self.exist = False
		self.name = None
		self.owner = None
		self.ipns = "127.0.0.1:1701"
		self.ipas = "127.0.0.1:4000"
		self.ipcs = "127.0.0.1:5000"
		self.ipnc = "127.0.0.1:6000"

		db = Database("lora_network")
		if db is not None:
			result = db.query("SELECT * FROM applications WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
				self.exist = True
				self.name = result[0][1]
				self.owner = result[0][2]


	def add_cmd(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		if not self.exist:
			command = "ns\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipas)+" active user motetx gwrx joinserver maccmd\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipnc)+" active motetx gwrx maccmd\n"
			command = command+"as\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipcs)+" active user motetx gwrx joinmonitor maccmd\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipns)+" passive downstream\n"
			command = command+"cs\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipas)+" passive downstream\n"
			command = command+"nc\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipcs)+" active user\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipns)+" passive downstream\n"
			return command


	def del_cmd(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		if not self.exist:
			pass
		else:
			command = "ns\napp server delete "+str(self.eui)+" "+str(self.ipas)+"\n"
			command = command+"app server delete "+str(self.eui)+" "+str(self.ipnc)+"\n"
			command = command+"app delete "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"as\napp server delete "+str(self.eui)+" "+str(self.ipcs)+"\n"
			command = command+"app server delete "+str(self.eui)+" "+str(self.ipns)+"\n"
			command = command+"app delete "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"cs\napp server delete "+str(self.eui)+" "+str(self.ipas)+"\n"
			command = command+"app delete "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"nc\napp server delete "+str(self.eui)+" "+str(self.ipcs)+"\n"
			command = command+"app server delete "+str(self.eui)+" "+str(self.ipns)+"\n"			
			command = command+"app delete "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			return command


	def geteui(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.eui
	def getexist(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.exist
	def getname(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.name
	def getowner(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		return self.owner

	def setname(self, name):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.name = name
	def setowner(self, owner):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:param state: Current state to be in.
		:type state: bool.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError

		"""
		self.owner = owner



		
