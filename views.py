"""La vue."""


from flask import Flask, render_template, request

from py import spliteur

#import config


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/acceuil/')
def index():
	"""Acceuil."""
	return render_template('acceuil.html')

@app.route('/question/')
def response():
	""" reponse."""
	#print(request.args.get('question'))
	#spliteur0 = spliteur.Spliteur()
	#spliteur0.split_and_clean(request.args.get('question'))

	return 1



if __name__ == "__main__":
    app.run()