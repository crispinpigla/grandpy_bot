"""Filtre"""

import config

class Filtre:
	"""docstring for Filtre"""
	def __init__(self):
		"""Init."""
		self.list_filtred = []


	def filtre(self, list_apply, support):
		"""Filtre."""
		for caractere in list_apply:
			if caractere.lower() not in support:
				self.list_filtred.append(caractere)
		print(self.list_filtred)

	def adresse_to_quartier(self, adresse):
		"""Adresse to quartier"""
		partie_adresse = adresse.split(',')
		quartier = partie_adresse[0]
		for numero in config.NUMBER_SUPPORT:
			if numero in quartier:
				quartier = quartier.replace(numero,'')
		return(quartier)




filtre = Filtre()
filtre.filtre(['Salut', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse','d', 'OpenClassrooms'], config.SUPPORT_PARSAGE)
