
# all the imports
import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flask 
app = Flask(__name__)

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
if __name__ = '__main__':
	app.run(host='0.0.0.0',port=8008)