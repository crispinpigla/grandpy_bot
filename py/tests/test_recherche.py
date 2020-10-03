"""Test recherche"""

import requests

from .. import recherche

from . import value_expected




class MockRequests:

    def __init__(self, which_api):
        """Init."""
        self.which_api = which_api

    def json(self):
        """Json."""
        if self.which_api == 'gmaps':
            return value_expected.expectedvalue_test_recherche_api_gmaps
        elif self.which_api == 'wikipedia':
            return value_expected.expectedvalue_test_recherche_api_wiki


class TestRecherche:
    """docstring for TestRecherche"""

    input_recherche = "openclassrooms"

    def test_request_to_gmaps(self, monkeypatch):
        """ test d'une recherche sur l'api de google maps """

        def get_mock_gmaps(*url):
            """Mock la requete google maps"""
            return MockRequests('gmaps')

        monkeypatch.setattr(requests, 'get', get_mock_gmaps)

        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()

        assert recherche0.resultat_gmaps == value_expected.expectedvalue_test_recherche_api_gmaps['results']


    def test_adresse_to_quartier(self):
        """Test les quartier extrait des resultats de gmaps"""
        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()
        assert len(recherche0.resultat_quartier) > 0

    def test_build_description(self, monkeypatch):
        """ test des recherches sur l'api de wikipedia """
        
        #recherche0.adresse_to_quartier()

        def get_mock_gmaps(*url):
            """Mock la requete google maps"""
            return MockRequests('gmaps')

        monkeypatch.setattr(requests, 'get', get_mock_gmaps)

        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()

        def get_mock_wikipedia(*url):
            """Mocker la requete wikipedia"""
            return MockRequests('wikipedia')

        monkeypatch.setattr(requests, 'get', get_mock_wikipedia)

        recherche0.build_description()

        assert recherche0.resultat_wiki == { '10 Quai de la Charente, 75019 Paris, France':value_expected.expectedvalue_test_recherche_api_wiki["query"]["pages"]}


    def test_build_resultat(self):
        """Test sur le résultat final"""
        recherche0 = recherche.Recherche( self.input_recherche )
        recherche0.request_to_gmaps()
        recherche0.adresse_to_quartier()
        recherche0.build_description()
        recherche0.build_resultat()
        #print(recherche0.liste_resultats)
        #assert len(recherche0.liste_resultats) > 0