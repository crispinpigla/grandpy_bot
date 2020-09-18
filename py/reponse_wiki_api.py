"""Reponse wiki"""


import requests
import json


class ReponseWikiApi:
	"""docstring for ReponseWikiApi"""

	def __init__(self, adresse, quartier):
		"""Init."""
		self.adresse = adresse
		self.quartier = quartier
		self.decription = None

	def build_description(self):
		"""Build"""

		request_wiki = requests.get("https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&titles=" + self.quartier + "&format=json")
		request_wiki = json.loads(request_wiki.text)
		self.decription = request_wiki
		





reponse_wiki_api = ReponseWikiApi("10 Quai de la Charente, 75019 Paris, France", " Quai de la Charente")
reponse_wiki_api.build_description()
print(reponse_wiki_api.decription)