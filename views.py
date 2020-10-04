"""La vue."""


import json
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request

from py.response import Response


load_dotenv(os.path.join("", ".env"))
key = os.getenv("GMAPS_API_KEY")

app = Flask(__name__)


@app.route("/")
@app.route("/acceuil/")
def index():
    """Acceuil."""
    return render_template("acceuil.html", gmaps_key=key)


@app.route("/question/")
def response():
    """ reponse."""
    response0 = Response(request.args.get("question"))
    response0.traitement()
    to_send = str(json.dumps(response0.to_send_to_front))
    return to_send


if __name__ == "__main__":
    app.run()
