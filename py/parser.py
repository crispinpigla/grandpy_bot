""" Parser."""

from . import config


class Parser:
	"""docstring for Spliteur"""
	def __init__(self):
		"""Init."""
		self.caractere_to_replace = config.PONCTUATION_SUPPORT
		self.str_replaced_ponctuation = None
		self.split_byspace = None
		self.list_clean = []
		self.list_filtred = []

	def _filtre(self, list_apply, support):
		"""Filtre. à déplacer """
		for caractere in list_apply:
			if caractere.lower() not in support:
				self.list_filtred.append(caractere)


	def _split_and_clean(self, str_to_replace):
		""" split and clean. """
		
		self.str_replaced_ponctuation = str_to_replace
		for caractere in self.caractere_to_replace:
			self.str_replaced_ponctuation = self.str_replaced_ponctuation.replace(caractere, ' ')

		self.split_byspace = self.str_replaced_ponctuation.split(' ')

		for caractere in self.split_byspace:
			if caractere != '':
				self.list_clean.append(caractere)


	def handle_message(self, message):
		"""handle"""

		self._split_and_clean(message)
		self._filtre( self.list_clean, config.SUPPORT_PARSAGE)