"""Test recherche"""

from .. import recherche

from . import value_expected


class TestRecherche:
    """docstring for TestRecherche"""

    input_recherche = "openclassrooms"

    def test_request_to_gmaps(self):
        """ test d'une recherche sur l'api de google maps """
        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()
        assert len(recherche0.resultat_gmaps) > 0

    def test_adresse_to_quartier(self):
        """Test les quartier extrait des resultats de gmaps"""
        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()
        assert len(recherche0.resultat_quartier) > 0

    def test_build_description(self):
        """ test des recherches sur l'api de wikipedia """
        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()
        recherche0.build_description()
        assert len(recherche0.resultat_wiki) > 0

    def test_build_resultat(self):
        """Test sur le résultat final"""
        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()
        recherche0.build_description()
        recherche0.build_resultat()
        assert len(recherche0.liste_resultats) > 0