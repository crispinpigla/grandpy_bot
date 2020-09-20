"""La vue."""


import json

from flask import Flask, render_template, request
import os

from py.response import Response

app = Flask(__name__)

#app.config.from_object('config')

@app.route('/')
@app.route('/acceuil/')
def index():
	"""Acceuil."""
	return render_template('acceuil.html')

@app.route('/question/')
def response():
	""" reponse."""
	response0 = Response( request.args.get('question') )
	response0.traitement()
	to_send = str(json.dumps(response0.to_send_to_front))
	return to_send


if __name__ == "__main__":
    app.run()