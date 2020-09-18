"""Majisculité."""



class Masjusculite:
	"""docstring for Masjuscle"""
	def __init__(self):
		"""Init."""
		self.taille_caractere = None
		self.taille_caractere_scan = 1
		self.curseur = ''
		self.chaine_traite = ''
		self.liste_casse_forme = []


	def liste_build_casse_forme(self, chaine):
		"""Construction."""

		self.taille_caractere = len(chaine)
		
		for i0 in range( len(chaine) ):
			taille_curseur = i0 + 1
			for i1 in range( len(chaine) - i0 ):
				self.liste_casse_forme.append( chaine[0:i1] + chaine[i1:i1+taille_curseur].upper() + chaine[i1+taille_curseur:]  )

		print(self.liste_casse_forme)





#majuscule = Masjusculite()
#majuscule.liste_build_casse_forme('chaine')

