"""Test traitement"""

from .. import response

from . import value_expected


class TestResponse:
	"""docstring for TestResponse"""

	def test_response(self):
		"""Test sur la reponse renvoyée au front"""

		entree_utilisateur = "elysee"
		response0 = response.Response(entree_utilisateur)
		response0.traitement()
		#print('prepare to send to front : ', response0.prepare_to_send_to_front)
		#print('to send to front : ', response0.to_send_to_front)
		#assert len(response0.to_send_to_front) > 0

