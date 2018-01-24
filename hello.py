from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'hello word'
if __name__ == '__main__':
	app.run(host='0.0.0.0',post='8008',debug=True)
