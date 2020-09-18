"""Test"""

from .. import spliteur

def test_spliteur():
	"""Test"""
	input_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
	spliteur0 = spliteur.Spliteur()
	spliteur0.split_and_clean(input_value)
	assert spliteur0.str_replaced_ponctuation == "Salut GrandPy   Est ce que tu connais l adresse d OpenClassrooms  "
	assert spliteur0.split_byspace == ['Salut', '', 'GrandPy', '', '', '', 'Est', 'ce', 'que', 'tu',
	'connais', 'l', 'adresse','d', 'OpenClassrooms', '', ''  ]
	assert spliteur0.list_clean == ['Salut', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse','d', 'OpenClassrooms']

