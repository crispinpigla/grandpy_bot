""" Module des differentes recherches effectuées sur google maps et sur wikipedia."""

import requests, json
from . import config
from pprint import pprint


class Recherche:
    """docstring for Recherche"""

    GMAPS_SEARCH_SERVICE = 1  # Google maps
    OSM_SEARCH_SERVICE = 2  # Openstreetmaps

    CURRENT_SEARCH_MAPS_SERVICE = OSM_SEARCH_SERVICE

    SEARCH_MAPS_SERVICE_TO_ADDRESS_KEY = {
        GMAPS_SEARCH_SERVICE: 'formatted_address',
        OSM_SEARCH_SERVICE: 'display_name'
    }

    def __init__(self, caractere_recherche):
        """Init"""
        self._caractere_recherche = caractere_recherche
        self._resultat_search_maps = []
        self._resultat_quartier = {}
        self._resultat_wiki = {}
        self._liste_resultats = []

    def request_to_gmaps(self):
        """Effectue une recherche sur l'api de google maps"""
        # request_gmaps = requests.get(
        #     "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
        #     + self.caractere_recherche
        #     + "&key=AIzaSyDMG3FXdLnjx4LkN8J8m0OR6qnbFaBsK9Y"
        # ).json()
        request_gmaps = config.GMAPS_OUTPUT_TEST
        print(request_gmaps)
        self.resultat_search_maps = request_gmaps["results"]

    def request_to_nominatim_osmap(self):
        """"""
        request_nominatim = requests.get(
            "https://nominatim.openstreetmap.org/search?q=%s&format=json" % self.caractere_recherche
        ).json()
        # pprint(request_nominatim)
        self.resultat_search_maps = list()
        address_in_resultat_search_maps = list()
        for element in request_nominatim:
            if element['display_name'] not in address_in_resultat_search_maps:
                self.resultat_search_maps.append(element)
                address_in_resultat_search_maps.append(element['display_name'])

    def adresse_to_quartier(self):
        """
        Renvoie les quartiers à partir d'adresse recuperé sur gmaps
        Only compatible with google maps api output
        """
        index_rue = 1  # -3
        index_ville = 2  # -2
        index_pays = 3  # -1

        for resultat in self.resultat_search_maps:
            partie_adresse = resultat[
                self.SEARCH_MAPS_SERVICE_TO_ADDRESS_KEY[
                    self.CURRENT_SEARCH_MAPS_SERVICE
                ]
            ]
            partie_adresse = partie_adresse.split(",")

            try:
                quartier = partie_adresse[index_rue]
            except Exception as e:
                try:
                    quartier = partie_adresse[index_ville]
                except Exception as e:
                    try:
                        quartier = partie_adresse[index_pays]
                    except Exception as e:
                        quartier = ""

            for caractere in quartier:
                if caractere.isnumeric():
                    quartier = quartier.replace(caractere, "")

            key_element = resultat
            self.resultat_quartier[resultat[self.SEARCH_MAPS_SERVICE_TO_ADDRESS_KEY[self.CURRENT_SEARCH_MAPS_SERVICE]]] = quartier

    def build_description(self):
        """Fait des recherches sur l'api de wikipedia """
        for adresse in self.resultat_quartier:
            request_wiki = requests.get(
                "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&titles="
                + self.resultat_quartier[adresse]
                + "&format=json"
            ).json()



            self.resultat_wiki[adresse] = request_wiki["query"]["pages"]

    def build_resultat(self):
        """Construit la liste des resultats"""

        for resultat_search_maps in self.resultat_search_maps:
            for adresse in self.resultat_wiki:
                if resultat_search_maps[self.SEARCH_MAPS_SERVICE_TO_ADDRESS_KEY[self.CURRENT_SEARCH_MAPS_SERVICE]] == adresse:
                    self.liste_resultats.append(
                        [resultat_search_maps, self.resultat_wiki[adresse]]
                    )

    @property
    def caractere_recherche(self):
        """getter"""
        return self._caractere_recherche

    @property
    def resultat_quartier(self):
        """getter"""
        return self._resultat_quartier

    @property
    def resultat_wiki(self):
        """getter"""
        return self._resultat_wiki

    @property
    def liste_resultats(self):
        """getter"""
        return self._liste_resultats
