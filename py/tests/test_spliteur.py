"""Test"""


from parser import Parser


class TestParser:
	"""docstring for TestParser"""

	def test_parser(self):
		"""Test"""

		input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		parser0 = Parser()
		parser0.handle_message("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
		assert parser0.str_replaced_ponctuation == "Salut GrandPy   Est ce que tu connais l adresse d OpenClassrooms  "
		assert parser0.split_byspace == ['Salut', '', 'GrandPy', '', '', '', 'Est', 'ce', 'que', 'tu',
		'connais', 'l', 'adresse','d', 'OpenClassrooms', '', ''  ]
		assert parser0.list_clean == ['Salut', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse','d', 'OpenClassrooms']

