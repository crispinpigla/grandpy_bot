"""Test recherche"""

from .. import recherche


class TestRecherche:
    """docstring for TestRecherche"""

    def test_recherche_api_gmaps(self):
        """ test d'une recherche sur l'api de google maps """
        recherche0 = recherche.Recherche("openclassrooms")
        recherche0.request_to_gmaps()
        assert len(recherche0.resultat_gmaps) > 0

    def test_quartier_api_gmaps(self):
        """Test les quartier extrait des resultats de gmaps"""
        recherche0 = recherche.Recherche("openclassrooms")
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()
        assert recherche0.resultat_quartier == {"10 Quai de la Charente, 75019 Paris, France": " Quai de la Charente", "10 Cité Paradis, 75010 Paris, France": " Cité Paradis" }

    def test_recherche_api_wiki(self):
        """ test des recherches sur l'api de wikipedia """
        recherche0 = recherche.Recherche("openclassrooms")
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()
        recherche0.build_description()
        print(recherche0.resultat_gmaps_wiki)
        # assert recherche0.resultat_gmaps_wiki = ?
