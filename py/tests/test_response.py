"""Test traitement"""

from .. import response

from . import value_expected


class TestResponse:
    """docstring for TestResponse"""

    def test_response(self):
        """Test sur la reponse renvoyée au front"""

        entree_utilisateur = "openclassrooms"
        response0 = response.Response(entree_utilisateur)
        response0.traitement()
        assert len(response0.to_send_to_front) > 0
