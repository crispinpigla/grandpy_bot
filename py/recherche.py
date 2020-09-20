""" Module des differentes recherches effectuées sur google maps et sur wikipedia."""

import requests, json


class Recherche:
    """docstring for Recherche"""

    def __init__(self, caractere_recherche):
        """Init"""
        self._caractere_recherche = caractere_recherche
        self._resultat_gmaps = []
        self._resultat_quartier = {}
        self._resultat_wiki = {}
        self._liste_resultats = []

    def request_to_gmaps(self):
        """Effectue une recherche sur l'api de google maps"""
        request_gmaps = requests.get(
            "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
            + self.caractere_recherche
            + "&key=AIzaSyDMG3FXdLnjx4LkN8J8m0OR6qnbFaBsK9Y"
        )
        request_gmaps = json.loads(request_gmaps.text)
        self.resultat_gmaps = request_gmaps["results"]


    def adresse_to_quartier(self):
        """Renvoie les quartiers à partir d'adresse recuperé sur gmaps"""
        index_rue = -3
        index_ville = -2
        index_pays = -1

        for resultat in self.resultat_gmaps:
            partie_adresse = resultat["formatted_address"]
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
                        raise e

            for caractere in quartier:
                if caractere.isnumeric():
                    quartier = quartier.replace(caractere, "")

            key_element = resultat
            self.resultat_quartier[resultat["formatted_address"]] = quartier


    def build_description(self):
        """Fait des recherches sur l'api de wikipedia """
        for adresse in self.resultat_quartier:
            request_wiki = requests.get(
                "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&titles="
                + self.resultat_quartier[adresse]
                + "&format=json"
            )
            request_wiki = json.loads(request_wiki.text)
            self.resultat_wiki[adresse] = request_wiki["query"]["pages"]
            

    def build_resultat(self):
        """Construit la liste des resultats"""

        for resultat_gmaps in self.resultat_gmaps:
            for adresse in self.resultat_wiki:
                if resultat_gmaps["formatted_address"] ==  adresse :
                    self.liste_resultats.append( [ resultat_gmaps, self.resultat_wiki[adresse] ] )


    @property
    def caractere_recherche(self):
        return self._caractere_recherche

    @property
    def resultat_quartier(self):
        return self._resultat_quartier

    @property
    def resultat_wiki(self):
        return self._resultat_wiki

    @property
    def liste_resultats(self):
        return self._liste_resultats