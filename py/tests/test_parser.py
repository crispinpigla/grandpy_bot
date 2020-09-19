"""Test"""


from .. import parser

from . import value_expected


class TestParser:
	"""docstring for TestParser"""

	def test_ponctuation_parser(self):
		"""Vérifie que les ponctuations sont retiré d'une chaine de caractere"""

		input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		parser0 = parser.Parser()
		parser0.handle_message(input_value)
		assert parser0.str_replaced_ponctuation == value_expected.expectedvalue_test_ponctuation_parser


	def test_clean_parser(self):
		"""Vérifie la liste de caractère intermédiaire sans ponctuation et chaines vides."""

		input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		parser0 = parser.Parser()
		parser0.handle_message(input_value)
		assert parser0.list_clean == value_expected.expectedvalue_test_clean_parser


	def test_filtre_parser(self):
		"""Vérifie la liste finale obtenue apres le parsage."""

		input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		parser0 = parser.Parser()
		parser0.handle_message(input_value)
		assert parser0.list_filtred == value_expected.expectedvalue_test_filtre_parser