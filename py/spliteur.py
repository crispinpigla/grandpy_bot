""" Spliteur."""


class Spliteur():

	"""docstring for Spliteur"""
	def __init__(self):
		"""Init."""
		self.caractere_to_replace = ['.', '!', '?', "'", '-']
		self.str_replaced_ponctuation = None
		self.split_byspace = None
		self.list_clean = []

	def split_and_clean(self, str_to_replace):
		""" split and clean. """
		
		self.str_replaced_ponctuation = str_to_replace
		for caractere in self.caractere_to_replace:
			self.str_replaced_ponctuation = self.str_replaced_ponctuation.replace(caractere, ' ')

		self.split_byspace = self.str_replaced_ponctuation.split(' ')

		for caractere in self.split_byspace:
			if caractere != '':
				self.list_clean.append(caractere)




spliteur0 = Spliteur()
spliteur0.split_and_clean( "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" )
print(spliteur0.list_clean)