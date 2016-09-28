#!/bin/python2.7
# coding=utf-8

from obj import *
from database import *
from config import *
from servers import *
from cloud import *
from report import *

import bcrypt
from getpass import getpass

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

import mysql.connector as mariadb
from config import Config

#creating the web app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#update configuration
app.config.update(dict(USERNAME='loik', PASSWORD='test', SECRET_KEY='development key'))

#master secret key for encryption
master_secret_key = getpass('tell me the master secret key you are going to use')

#creating the admin account
name = getpass("tell me the admin's name")
password = getpass("tell me the admin's password")
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
db = Database("web_database")
if db.cursor is None:
	sys.exit(-1)
sql = "DELETE FROM webusers"
print(sql)
entries = db.query(sql)
sql = "INSERT INTO webusers (name, hashed) VALUES (\'%s\', \'%s\')" % (name, hashed)
print(sql)
entries = db.query(sql)
sql = "SELECT * FROM webusers"
print(sql)
entries = db.query(sql)
if entries is None:
	db.close()
	sys.exit(-1)
print(entries)
db.close()





@app.route('/<string:obj_name>')
def show_entries(obj_name):
	if session.get('logged_in'):
		db = Database("lora_customer")
		sql = "SELECT * FROM "+str(obj_name)
		entries = db.query(sql)
		db.close()
		return render_template('show_entries.html', entries=entries)
	else:
		return redirect(url_for('login'))


@app.route('/snapshot')
def show_snap():
	if session.get('logged_in'):
		db = Database("lora_customer")
		sql = "SELECT `time`, HEX(`eui`), HEX(`appeui`), `data`, `seqNo`, `port` FROM motes AS m, appdata AS a WHERE a.id = m.lastRxFrame ORDER BY `appEui`"
		entries = db.query(sql)
		db.close()
		return render_template('show_entries.html', entries=entries)
	else:
		return redirect(url_for('login'))


@app.route('/add')
def add():
	return render_template('add.html')


@app.route('/add_gateway', methods=['POST'])
def add_gateway():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	gw = Gateway(request.form['eui'])
	gw.setregion(request.form['region'])
	gw.setmaxTxPower_dBm(request.form['maxTxPower_dBm'])
	gw.setallowGpsToSetPosition(request.form['allowGpsToSetPosition'])
	gw.setlatitude(request.form['latitude'])
	gw.setlongitude(request.form['longitude'])
	gw.setaltitude(request.form['altitude'])
	gw.setntwkMaxDelayUp_ms(request.form['ntwkMaxDelayUp_ms'])
	gw.setntwkMaxDelayDn_ms(request.form['ntwkMaxDelayDn_ms'])
	command = gw.add_cmd()
	servers = Connector()
	(stdout, stderr) = servers.append(command, 3)
	flash("stdout: "+stdout+";stderr: "+stderr)
	return redirect(url_for('show_snap'))


@app.route('/add_application', methods=['POST'])
def add_application():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	app = App(request.form['eui'])
	app.setname(request.form['name'])
	app.setowner(request.form['owner'])
	command = app.add_cmd()
	servers = Connector()
	(stdout, stderr) = servers.append(command, 3)
	flash("stdout: "+stdout+";stderr: "+stderr)
	return redirect(url_for('show_snap'))


@app.route('/add_mote', methods=['POST'])
def add_mote():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	mote = Mote(request.form['eui'])
	mote.setappeui(request.form['appeui'])
	mote.setclassC(request.form['classC'])
	mote.setnetworkAddress(request.form['networkAddress'])
	mote.setnetworkSessionKey(request.form['networkSessionKey'])
	mote.setapplicationSessionKey(request.form['applicationSessionKey'])
	command = mote.add_cmd()
	servers = Connector()
	(stdout, stderr) = servers.append(command, 3)
	flash("stdout: "+stdout+";stderr: "+stderr)
	return redirect(url_for('show_snap'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	global master_secret_key
	error = None
	if request.method == 'POST':
		db = Database("web_database")
		sql = "SELECT name, hashed FROM webusers WHERE name=\'"+str(request.form['username'])+"\'"
		entries = db.query(sql)
		db.close()
		if entries is None:
			error = "unknown user"
			return render_template('login.html', error=error)
		if bcrypt.hashpw(request.form['password'].encode("ascii","ignore"), entries[0][1].encode("ascii","ignore")) == entries[0][1].encode("ascii","ignore"):
			session['logged_in'] = True
			return redirect(url_for('show_snap'))
		error = "wrong password"
	return render_template('login.html', error=error)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
	global master_secret_key
	error = None
	if request.method == 'POST':
		if session['logged_in'] == True:
			hashed = bcrypt.hashpw(request.form['password'].encode("ascii","ignore"), bcrypt.gensalt())
			db = Database("web_database")
			sql = "INSERT INTO webusers (name, hashed) VALUES (\'%s\', \'%s\')" % (request.form['name'], hashed)
			entries = db.query(sql)
			db.close()
			flash("user created")
			return redirect(url_for('show_snap'))
	error = "failed"
	return render_template('add.html', error=error)


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_snap'))


@app.route('/send_data', methods=['POST'])
def send_data():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	mote = Mote(request.form['eui'])
	command = mote.send_cmd(request.form['port'], request.form['payload'])
	servers = Connector()
	(stdout, stderr) = servers.append(command, 3)
	flash("stdout: "+stdout+";stderr: "+stderr)
	return redirect(url_for('show_snap'))











