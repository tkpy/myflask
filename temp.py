# -*- coding: utf-8 -*-
from flask import Flask 
from flask import render_template
app = Flask(__name__)

# 静态模板的访问
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8008,debug=True)