# -*- coding: UTF-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'hello word'

@app.route('/hello')
def hello():
	return '你好世界'

# 携带参数
# @app.route('/user/<username>')
# def show_user_profile(username):
# 	return "user %s"% username

# 传递整数参数
@app.route('/post/<int:post_id>')
def post(post_id):
	return "Post %d"% post_id

# 唯一URL/重定向行为
@app.route('/projects/')
def projects():
	return 'The projects page'
@app.route('/about')
def about():
	return 'The about page'

# 构造url
from flask import url_for
@app.route('/login')
def login():
	pass
@app.route('/user/<username>')
def profile(username):
	pass
with app.test_request_context():
	print url_for('index')
	print url_for('login')
	print url_for('login',next='/')
	print url_for('profile',userename='John Doe')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8008,debug=True)
