""" Traitement """


import random

from . import config
from . import parser
from . import recherche


class Response:
    """docstring for TraitementDemande"""

    def __init__(self, demande_utilisateur):
        """Init."""
        self._demande_utilisateur = demande_utilisateur
        self._liste_recherche = []
        self._prepare_to_send_to_front = []
        self._to_send_to_front = []

    def traitement(self):
        """Traitement."""

        parser0 = parser.Parser()
        parser0.handle_message(self.demande_utilisateur)

        if len(parser0.list_filtred) == 0:
            pass

        elif len(parser0.list_filtred) in [1, 2]:

            # Parcous les element obtenus apres le parsage
            caractere = parser0.list_filtred[0]
            for caractere0 in range(1, len(parser0.list_filtred)):
                caractere += " " + parser0.list_filtred[caractere0]

            self._liste_recherche.append(recherche.Recherche(caractere))

            # Construction des reponses des differentes recherche
            for recherche0 in self.liste_recherche:
                recherche0.request_to_gmaps()
                recherche0.adresse_to_quartier()
                recherche0.build_description()
                recherche0.build_resultat()

            # Rangement des caractères recherchés
            for recherche1 in self.liste_recherche:
                self._prepare_to_send_to_front.append(
                    [recherche1.caractere_recherche, recherche1.liste_resultats]
                )

            # Formation de la reponse [ resultat_apres_parsage , [ salutation , presentation , [ adresse , {longitude , latitude} , annonce_description , description ], [ adresse , {longitude , latitude} , annonce_description , description ], ... ] ]
            rnd = random.Random()
            for resultat_parse in self._prepare_to_send_to_front:

                #  Rangement d'element obtenu apres le parsage et la reponse correspondante
                response_send_front_resultat_parse = [resultat_parse[0], []]
                response_send_front_resultat_parse[1].append(
                    rnd.choice(config.SALUTATION_RESPONSE)
                )
                response_send_front_resultat_parse[1].append(
                    rnd.choice(config.PRESENTATION_RESPONSE).replace(
                        "{{i}}", str(len(resultat_parse[1]))
                    )
                )

                #  Ajout des résultats des api
                for resultat_api in resultat_parse[1]:
                    recherche_adresse = []
                    recherche_adresse.append(resultat_api[0]["formatted_address"])
                    recherche_adresse.append(resultat_api[0]["geometry"]["location"])
                    for id_adresse_wiki in resultat_api[1]:
                        recherche_adresse.append(
                            rnd.choice(config.ANNONCE_DESCRIPTION_RESPONSE)
                            + resultat_api[1][id_adresse_wiki]["title"]
                        )
                        # print(resultat_api)
                        try:
                            recherche_adresse.append(
                                resultat_api[1][id_adresse_wiki]["extract"]
                            )
                        except Exception as e:
                            recherche_adresse.append("")
                    response_send_front_resultat_parse[1].append(recherche_adresse)

                self._to_send_to_front.append(response_send_front_resultat_parse)
                print(self._to_send_to_front)

        else:
            for caractere0 in parser0.list_filtred:
                self._to_send_to_front.append(caractere0)

    @property
    def demande_utilisateur(self):
        """getter."""
        return self._demande_utilisateur

    @property
    def liste_recherche(self):
        """getter."""
        return self._liste_recherche

    @property
    def prepare_to_send_to_front(self):
        """getter."""
        return self._prepare_to_send_to_front

    @property
    def to_send_to_front(self):
        """getter."""
        return self._to_send_to_front
