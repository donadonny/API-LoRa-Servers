#!/bin/python2.7
# coding=utf-8

from obj import *
from database import *
from config import *
from servers import *
from cloud import *
from report import *


if __name__ == '__main__':
	#construction d'objets utiles
	signal.signal(signal.SIGALRM, handler)
	cloud = Cloud()
	servers = Connector("127.0.0.1", "127.0.0.1:4000", "127.0.0.1:5000", "127.0.0.1:6000")
	timeout = 3
	reports_id = {}

	#boucle infinie
	while True:

		raw_input("Press Enter to continue...")

		#recuperation des commandes venant du server
		while True:
			requests = cloud.get_data()
			if requests.status_code == 200:
				print("Success!")
				break
			print("echec..")
		requests_dict = json.loads(requests.text)
		
		#creation de l'objet de reponse
		answers_dict = {'token': requests_dict['token'], 'gateways': {}, 'motes': {}, 'applications': {}, 'reports': {}, 'frames': {}, 'DEL': {'gateways': {}, 'motes': {}, 'applications': {}, 'reports': {}}}

		#boucle sur toutes les commands requests recues de type GW
		for key, value in requests_dict['gateways'].iteritems():

			#creation de l'objet gw
			gw = Gateway(key)
			if gw.exist:
				print("\na gateway will be updated..."+str(gw.eui))
			else:
				print("\na gateway will be created..."+str(gw.eui))

			#on remplit l'objet avec les parametres de la requete
			if gw is not None:
				if 'region' in value:
					print("setting region..")
					if value['region'] is not gw.getregion():
						gw.setregion(value['region'])
						print("region changed to "+str(gw.getregion()))
					else:
						print("nothing to do!")
				if 'maxTxPower_dBm' in value:
					print("setting maxTxPower_dBm..")
					if value['maxTxPower_dBm'] is not gw.getmaxTxPower_dBm():
						gw.setmaxTxPower_dBm(value['maxTxPower_dBm'])
						print("maxTxPower_dBm changed to "+str(gw.getmaxTxPower_dBm()))
					else:
						print("nothing to do!")
				if 'allowGpsToSetPosition' in value:
					print("setting allowGpsToSetPosition..")
					if value['allowGpsToSetPosition'] is not gw.getallowGpsToSetPosition():
						gw.setallowGpsToSetPosition(value['allowGpsToSetPosition'])
						print("allowGpsToSetPosition changed to "+str(gw.getallowGpsToSetPosition()))
					else:
						print("nothing to do!")
				if 'latitude' in value:
					print("setting latitude..")
					if value['latitude'] is not gw.getlatitude():
						gw.setlatitude(value['latitude'])
						print("latitude changed to "+str(gw.getlatitude()))
					else:
						print("nothing to do!")
				if 'longitude' in value:
					print("setting longitude..")
					if value['longitude'] is not gw.getlongitude():
						gw.setlongitude(value['longitude'])
						print("longitude changed to "+str(gw.getlongitude()))
					else:
						print("nothing to do!")
				if 'altitude' in value:
					print("setting altitude..")
					if value['altitude'] is not gw.getaltitude():
						gw.setaltitude(value['altitude'])
						print("altitude changed to "+str(gw.getaltitude()))
					else:
						print("nothing to do!")
				if 'ntwkMaxDelayUp_ms' in value:
					print("setting ntwkMaxDelayUp_ms..")
					if value['ntwkMaxDelayUp_ms'] is not gw.getntwkMaxDelayUp_ms():
						gw.setntwkMaxDelayUp_ms(value['ntwkMaxDelayUp_ms'])
						print("ntwkMaxDelayUp_ms changed to "+str(gw.getntwkMaxDelayUp_ms()))
					else:
						print("nothing to do!")
				if 'ntwkMaxDelayDn_ms' in value:
					print("setting ntwkMaxDelayDn_ms..")
					if value['ntwkMaxDelayDn_ms'] is not gw.getntwkMaxDelayDn_ms():
						gw.setntwkMaxDelayDn_ms(value['ntwkMaxDelayDn_ms'])
						print("ntwkMaxDelayDn_ms changed to "+str(gw.getntwkMaxDelayDn_ms()))
					else:
						print("nothing to do!")

				#preparation de la commande
				command = gw.add_cmd()

				#envoi de la commande aux servers
				(stdout, stderr) = servers.append(command, timeout)

				#on ajoute le code retour à la reponse associée à cette gateway
				answers_dict['gateways'][key] = {'stdout': stdout, 'stderr': stderr}
			else:
				#sinon on ecrit dans la reponse que ça s'est mal passé
				answers_dict['gateways'][key] = {'stdout': "", 'stderr': "error while creating gateway object"}

		#boucle sur toutes les commands requests recues de type APP
		for key, value in requests_dict['applications'].iteritems():

			#creation de l'objet mote
			app = App(key)
			if app.exist:
				print("\nan app will be updated..."+str(app.eui))
			else:
				print("\nan app will be created..."+str(app.eui))

			#on remplit l'objet avec les parametres de la requete
			if app is not None:
				if 'name' in value:
					print("setting name..")
					if value['name'] is not app.getname():
						app.setname(value['name'])
						print("name changed to "+str(app.getname()))
					else:
						print("nothing to do!")
				if 'owner' in value:
					print("setting owner..")
					if value['owner'] is not app.getowner():
						app.setowner(value['owner'])
						print("owner changed to "+str(app.getowner()))
					else:
						print("nothing to do!")


				#preparation de la commande
				command = app.add_cmd()

				#envoi de la commande aux servers
				(stdout, stderr) = servers.append(command, timeout)

				#on ajoute le code retour à la reponse associée à cette app
				answers_dict['applications'][key] = {'stdout': stdout, 'stderr': stderr}
			else:
				#sinon on ecrit dans la reponse que ça s'est mal passé
				answers_dict['applications'][key] = {'stdout': "", 'stderr': "error while creating app object"}

		#boucle sur toutes les commands requests recues de type MOTE
		for key, value in requests_dict['motes'].iteritems():

			#creation de l'objet mote
			mote = Mote(key)
			if mote.exist:
				print("\na mote will be updated..."+str(mote.eui))
			else:
				print("\na mote will be created..."+str(mote.eui))

			#on remplit l'objet avec les parametres de la requete
			if mote is not None:
				if 'appeui' in value:
					print("setting appeui..")
					if value['appeui'] is not mote.getappeui():
						mote.setappeui(value['appeui'])
						print("appeui changed to "+str(mote.getappeui()))
					else:
						print("nothing to do!")
				if 'classC' in value:
					print("setting classC..")
					if value['classC'] is not mote.getclassC():
						mote.setclassC(value['classC'])
						print("classC changed to "+str(mote.getclassC()))
					else:
						print("nothing to do!")
				if 'networkAddress' in value:
					print("setting networkAddress..")
					if value['networkAddress'] is not mote.getnetworkAddress():
						mote.setnetworkAddress(value['networkAddress'])
						print("networkAddress changed to "+str(mote.getnetworkAddress()))
					else:
						print("nothing to do!")
				if 'networkSessionKey' in value:
					print("setting networkSessionKey..")
					if value['networkSessionKey'] is not mote.getnetworkSessionKey():
						mote.setnetworkSessionKey(value['networkSessionKey'])
						print("networkSessionKey changed to "+str(mote.getnetworkSessionKey()))
					else:
						print("nothing to do!")
				if 'applicationSessionKey' in value:
					print("setting applicationSessionKey..")
					if value['applicationSessionKey'] is not mote.getapplicationSessionKey():
						mote.setapplicationSessionKey(value['applicationSessionKey'])
						print("applicationSessionKey changed to "+str(mote.getapplicationSessionKey()))
					else:
						print("nothing to do!")

				#si le mote existe deja on doit le supprimer car il n'y a pas de moyen de le modifier
				if mote.exist:
					#preparation de la commande de suppression
					command = mote.del_cmd()
					#envoi de la commande aux servers
					(stdout, stderr) = servers.append(command, timeout)

				#preparation de la commande d'ajout
				command = mote.add_cmd()
				#envoi de la commande aux servers
				(stdout, stderr) = servers.append(command, timeout)

				#on ajoute le code retour à la reponse associée à ce mote
				answers_dict['motes'][key] = {'stdout': stdout, 'stderr': stderr}
			else:
				#sinon on ecrit dans la reponse que ça s'est mal passé
				answers_dict['motes'][key] = {'stdout': "", 'stderr': "error while creating mote object"}

		#boucle sur toutes les commands requests recues de type REPORT
		for key, value in requests_dict['reports'].iteritems():

			#on crée d'abord le looper
			if 'sql' in value:
				loop = Looper(value['sql'])
				if loop is not None:
					if 'iterations' in value:
						loop.iterations = value['iterations']
					if 'period' in value:
						loop.period = value['period']
					print("\nreport "+str(key)+" created. will send "+str(loop.iterations)+" message(s) every "+str(loop.period)+" second(s)")

					#puis on recupere le PID du thread pour le mettre dans le registre
					reports_id.update({key: loop.getPID()})
					print(repr(reports_id))

					#enfin on lance le looper
					loop.start()
					print("started")

					#code retour
					answers_dict['reports'][key] = "running"
				else:
					answers_dict['reports'][key] = "error while creating report object"
					print("error")
			else:
				answers_dict['reports'][key] = "missing sql statement"
				print("missing sql")

		raw_input("Press Enter to continue...")

		#on bl-oucle sur toutes les donnees à envoyer aux motes
		for key, value in requests_dict['frames'].iteritems():

			if 'port' in value and 'data' in value:
				#on prepare la commande
				command = "cs\nmote send "+str(key)+" port "+str(value['port'])+" data "+str(value['data'])+"\n"

				#et on envoit
				(stdout, stderr) = servers.append(command, timeout)
				print("data has been sent to mote: "+str(key)+" on port: "+str(value['port'])+" => "+str(value['data']))

				#code retour
				answers_dict['frames'][key] = "ok"
			else:
				answers_dict['frames'][key] = "missing parameter"

		raw_input("Press Enter to continue...")

		#boucle sur touts les objets à supprimer de type GW
		for i, value in enumerate(requests_dict['DEL']['gateways']):

			#creation de l'objet gw
			gw = Gateway(value)

			#on remplit l'objet avec les parametres de la requete
			if gw is not None:

				#preparation de la commande
				command = gw.del_cmd()
				print("\na gateway will be deleted..."+str(gw.eui))

				#envoi de la commande aux servers
				(stdout, stderr) = servers.append(command, timeout)
				print("done!")

				#on ajoute le code retour à la reponse associée à cette gateway
				answers_dict['DEL']['gateways'][value] = {'stdout': stdout, 'stderr': stderr}
			else:
				#sinon on ecrit dans la reponse que ça s'est mal passé
				answers_dict['DEL']['gateways'][value] = {'stdout': "", 'stderr': "error while creating gateway object"}

		#boucle sur touts les objets à supprimer de type MOTE
		for i, value in enumerate(requests_dict['DEL']['motes']):

			#creation de l'objet gw
			mote = Mote(value)

			#on remplit l'objet avec les parametres de la requete
			if mote is not None:

				#preparation de la commande
				command = mote.del_cmd()
				print("\na mote will be deleted..."+str(mote.eui))

				#envoi de la commande aux servers
				(stdout, stderr) = servers.append(command, timeout)
				print("done!")

				#on ajoute le code retour à la reponse associée à cette gateway
				answers_dict['DEL']['motes'][value] = {'stdout': stdout, 'stderr': stderr}
			else:
				#sinon on ecrit dans la reponse que ça s'est mal passé
				answers_dict['DEL']['motes'][value] = {'stdout': "", 'stderr': "error while creating mote object"}

		#boucle sur touts les objets à supprimer de type APP
		for i, value in enumerate(requests_dict['DEL']['applications']):

			#creation de l'objet gw
			app = App(value)

			#on remplit l'objet avec les parametres de la requete
			if app is not None:

				#preparation de la commande
				command = app.del_cmd()
				print("\na app will be deleted..."+str(app.eui))

				#envoi de la commande aux servers
				(stdout, stderr) = servers.append(command, timeout)
				print("done!")

				#on ajoute le code retour à la reponse associée à cette gateway
				answers_dict['DEL']['applications'][value] = {'stdout': stdout, 'stderr': stderr}
			else:
				#sinon on ecrit dans la reponse que ça s'est mal passé
				answers_dict['DEL']['applications'][value] = {'stdout': "", 'stderr': "error while creating app object"}

		#boucle sur touts les objets à supprimer de type REPORT
		for i, value in enumerate(requests_dict['DEL']['reports']):

			#on recupere le pid du looper
			if value in reports_id:
				pid = reports_id[value]

				#puis on le kill samaireuh
				print("killing service: "+str(value)+" with PID: "+str(pid))
				#os.kill(pid, signal.SIGKILL)
				print("done!")

				#code retour
				answers_dict['DEL']['reports'][value] = "killed"
			else:
				answers_dict['DEL']['applications'][value] = "could not fetch pid"

		#envoi de la reponse au server
		print(repr(answers_dict))
		rt = cloud.post_data(answers_dict)




