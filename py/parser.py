"""Parser."""

from . import config


class Parser:
	"""docstring for Spliteur"""
	def __init__(self):
		"""Init."""
		self._caractere_to_replace = config.PONCTUATION_SUPPORT
		self._str_replaced_ponctuation = None
		self._split_byspace = None
		self._list_clean = []
		self._list_filtred = []

	def _filtre(self, list_apply, support):
		"""Filtre. à déplacer """

		for caractere in list_apply:
			if caractere.lower() not in support:
				self._list_filtred.append(caractere)


	def _split_and_clean(self, str_to_replace):
		""" split and clean. """
		
		self._str_replaced_ponctuation = str_to_replace
		for caractere in self._caractere_to_replace:
			self._str_replaced_ponctuation = self._str_replaced_ponctuation.replace(caractere, ' ')

		self._split_byspace = self._str_replaced_ponctuation.split(' ')

		for caractere in self._split_byspace:
			if caractere != '':
				self._list_clean.append(caractere)


	def handle_message(self, message):
		"""handle"""

		self._split_and_clean(message)
		self._filtre( self._list_clean, config.SUPPORT_PARSAGE)


	# getters
	"""
	@property
	def caractere_to_replace(self):
		return self._caractere_to_replace
"""
	@property
	def str_replaced_ponctuation(self):
		return self._str_replaced_ponctuation

	@property
	def list_clean(self):
		return self._list_clean

	@property
	def list_filtred(self):
		return self._list_filtred
"""
	@property
	def split_byspace(self):
		return self._split_byspace


"""
	
	
"""

	# setters
	@str_replaced_ponctuation.setter
	def str_replaced_ponctuation(self,valeur):
		self._str_replaced_ponctuation = valeur

	@str_replaced_ponctuation.setter
	def split_byspace(self,valeur):
		self._split_byspace = valeur

	@list_clean.setter
	def list_clean(self,valeur):
		self._list_clean = valeur

	@list_filtred.setter
	def list_filtred(self,valeur):
		self._list_filtred = valeur"""