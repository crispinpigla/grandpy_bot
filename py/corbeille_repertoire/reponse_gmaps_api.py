"""Gmaps api"""

import requests
import json

class GmapsApi:
	"""docstring for GmapsApi"""
	def __init__(self, caractere):
		"""Init."""
		self.caractere = caractere
		self.find_by_google_search = None


	def send_request(self):
		"""request"""

		request_gmaps = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + self.caractere + "&key=AIzaSyDMG3FXdLnjx4LkN8J8m0OR6qnbFaBsK9Y")
		request_gmaps = json.loads(request_gmaps.text)
		self.find_by_google_search = request_gmaps['results']
		print(self.find_by_google_search)





#request_gmaps = GmapsApi('openclassrooms')
#request_gmaps.send_request('openclassrooms')