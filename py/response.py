""" Traitement """


from . import parser
from . import recherche



class Response:
	"""docstring for TraitementDemande"""
	def __init__(self,demande_utilisateur):
		"""Init."""
		self.demande_utilisateur = demande_utilisateur
		#self.liste_objet_reponse = []
		self.liste_recherche = []
		self.to_send_to_front = []


	def traitement(self):
		"""Traitement."""

		parser0 = parser.Parser()
		parser0.handle_message( self.demande_utilisateur )
		
		for caractere0 in parser0.list_filtred:
			self.liste_recherche.append(recherche.Recherche(caractere0))

		for recherche0 in self.liste_recherche:
			recherche0.request_to_gmaps()
			recherche0.adresse_to_quartier()
			recherche0.build_description()
			recherche0.build_resultat()

		for recherche1 in self.liste_recherche:
			self.to_send_to_front.append( tuple(recherche1.liste_resultats) )