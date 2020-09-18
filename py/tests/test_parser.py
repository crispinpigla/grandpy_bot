"""Test"""


from .. import parser


class TestParser:
	"""docstring for TestParser"""

	def test_ponctuation_parser(self):
		"""Vérifie que les ponctuations sont retiré d'une chaine de caractere"""

		input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		parser0 = parser.Parser()
		parser0.handle_message("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
		assert parser0.str_replaced_ponctuation == "Salut GrandPy   Est ce que tu connais l adresse d OpenClassrooms  "


	def test_clean_parser(self):
		"""Vérifie la liste de caractère intermédiaire sans ponctuation et chaines vides."""

		input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		parser0 = parser.Parser()
		parser0.handle_message("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
		assert parser0.list_clean == ['Salut', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse','d', 'OpenClassrooms']


	def test_filtre_parser(self):
		"""Vérifie la liste finale obtenue apres le parsage."""

		input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		parser0 = parser.Parser()
		parser0.handle_message("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
		assert parser0.list_filtred == ['OpenClassrooms']