# flaskapp/__init__.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworl():
	return "Hello Flask World!"


