""" Traitement """



import spliteur, filtre, reponse_apis, reponse_gmaps_api, reponse_apis, config

class TraitementDemande:
	"""docstring for TraitementDemande"""
	def __init__(self):
		"""Init."""
		self.demande_utilisateur = None
		self.liste_objet_reponse = []
		self.liste_recherche_gmaps = []


	def traitement(self, demande_utilisateur):
		"""Traitement."""

		spliteur0 = spliteur.Spliteur()   #  1
		filtre0 = filtre.Filtre()     #  2
		reponse_gmaps0 = reponse_gmaps_api.GmapsApi()    #   3

		spliteur0.split_and_clean( demande_utilisateur )
		filtre0.filtre( spliteur0.list_clean, config.SUPPORT_PARSAGE )

		for caractere0 in filtre0.self.list_filtred:
			self.liste_recherche_gmaps.append(reponse_gmaps_api.GmapsApi(caractere0))


		result_search_google = []
		for input_search in filtre0.list_filtred:
			reponse_gmaps0.send_request(input_search)
			result_search_google.append( [reponse_gmaps0.find_by_google_search] )

		print(len(result_search_google), '-'*10)
		print(result_search_google)

		#list_reponse = []
		for find in result_search_google[0]:
			self.liste_objet_reponse.append(reponse_apis.RepeonseApis())
			print( '_'*20, find)
			#self.liste_objet_reponse[0].set_adresse_coordonne(find['formatted_address'], find['geometry']['location'])

		#print(self.liste_objet_reponse)








traitement0 = TraitementDemande()

traitement0.traitement("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")