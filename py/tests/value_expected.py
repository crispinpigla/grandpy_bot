"""Module des valeurs attendues test"""


expectedvalue_test_ponctuation_parser = (
    "Salut GrandPy   Est ce que tu connais l adresse d OpenClassrooms  "
)
expectedvalue_test_clean_parser = [
    "Salut",
    "GrandPy",
    "Est",
    "ce",
    "que",
    "tu",
    "connais",
    "l",
    "adresse",
    "d",
    "OpenClassrooms",
]
expectedvalue_test_filtre_parser = ["OpenClassrooms"]

expectedvalue_test_recherche_api_gmaps = {
    "results": [{"formatted_address": "10 Quai de la Charente, 75019 Paris, France"}]
}
expectedvalue_test_quartier_api_gmaps = {
    "10 Quai de la Charente, 75019 Paris, France": " Quai de la Charente",
    "10 Cité Paradis, 75010 Paris, France": " Cité Paradis",
}
expectedvalue_test_recherche_api_wiki = {
    "query": {
        "pages": {
            "123": {
                "extract": "quai de la Charente est un quai situé le long du canal Saint-Denis, à Paris, dans le 19eme arrondissement."
            }
        }
    }
}

expectedvalue_test_response = ""
