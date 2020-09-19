"""Module des valeurs attendues test"""



expectedvalue_test_ponctuation_parser = "Salut GrandPy   Est ce que tu connais l adresse d OpenClassrooms  "
expectedvalue_test_clean_parser = ['Salut', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse','d', 'OpenClassrooms']
expectedvalue_test_filtre_parser = ['OpenClassrooms']

expectedvalue_test_recherche_api_gmaps = [{'business_status': 'OPERATIONAL', 'formatted_address': '10 Quai de la Charente, 75019 Paris, France', 'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993}, 'viewport': {'northeast': {'lat': 48.89886542989272, 'lng': 2.384749129892722}, 'southwest': {'lat': 48.89616577010728, 'lng': 2.382049470107278}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png', 'name': 'Openclassrooms', 'opening_hours': {'open_now': False}, 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'plus_code': {'compound_code': 'V9XM+29 Paris', 'global_code': '8FW4V9XM+29'}, 'rating': 3.3, 'reference': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'types': ['point_of_interest', 'establishment'], 'user_ratings_total': 30}, {'business_status': 'OPERATIONAL', 'formatted_address': '55 Avenue Louis Breguet batiment 9, 31400 Toulouse, France', 'geometry': {'location': {'lat': 43.5771408, 'lng': 1.4777689}, 'viewport': {'northeast': {'lat': 43.57847012989272, 'lng': 1.479153029892722}, 'southwest': {'lat': 43.57577047010727, 'lng': 1.476453370107278}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png', 'name': 'BAYAH DEZIGN', 'opening_hours': {'open_now': True}, 'photos': [{'height': 909, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/113135400030988796472">BAYAH DEZIGN</a>'], 'photo_reference': 'CmRaAAAAT-K3axZXBBiKzxh3gBE10Cd1kfS56LavqFKCmYBGN_KTIbB-WXMHreOphexyPLsLIaPIQp0a-I7cJvmdoNxm1dtGr1WcT1UT7zTkJExkazwMMxrKkEZzGdzH0EwzciZ8EhCDQfWvOTt-mQIf40IGnYo4GhRJAbc6218VsVXEk2g2CUkSvNcCgg', 'width': 3458}], 'place_id': 'ChIJSQjLpom7rhIRaT8XbPeWMpY', 'plus_code': {'compound_code': 'HFGH+V4 Toulouse', 'global_code': '8FM3HFGH+V4'}, 'rating': 4.7, 'reference': 'ChIJSQjLpom7rhIRaT8XbPeWMpY', 'types': ['painter', 'point_of_interest', 'establishment'], 'user_ratings_total': 6}, {'business_status': 'OPERATIONAL', 'formatted_address': 'Zone Artisanale les agriès, 600 Chemin Les Agries, 31860 Labarthe-sur-Lèze, France', 'geometry': {'location': {'lat': 43.465543, 'lng': 1.388676}, 'viewport': {'northeast': {'lat': 43.46684557989272, 'lng': 1.390198329892722}, 'southwest': {'lat': 43.46414592010727, 'lng': 1.387498670107278}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png', 'name': 'Emmaüs Labarthe-sur-Lèze', 'opening_hours': {'open_now': True}, 'photos': [{'height': 4128, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/107371813534981146378">A Google User</a>'], 'photo_reference': 'CmRaAAAAz9ZrgQqoIrirGmBwcwTGzwgz_q8icRG1FHefxNJyGwfJUp1PxSLU2VwxgqM52emMsGtJdq5ArbyBL1dudMOUmgmbzdJVlQRgnJJSzbT7EZ5ZuUwP2y1lCUvewWgxN7jIEhBVFad8s8l0zoELzYsI9N1fGhQDINtinJEydUbsaZVngfdmu62V0A', 'width': 3096}], 'place_id': 'ChIJgdK7PJDHrhIRP68fCXWTk5A', 'plus_code': {'compound_code': 'F98Q+6F Labarthe-sur-Lèze', 'global_code': '8FM3F98Q+6F'}, 'rating': 3.8, 'reference': 'ChIJgdK7PJDHrhIRP68fCXWTk5A', 'types': ['point_of_interest', 'store', 'establishment'], 'user_ratings_total': 769}, {'business_status': 'OPERATIONAL', 'formatted_address': '135 Avenue de Rangueil, 31400 Toulouse, France', 'geometry': {'location': {'lat': 43.5696438, 'lng': 1.4677288}, 'viewport': {'northeast': {'lat': 43.57108142989274, 'lng': 1.468987629892722}, 'southwest': {'lat': 43.56838177010729, 'lng': 1.466287970107278}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/school-71.png', 'name': 'INSA Toulouse', 'opening_hours': {'open_now': False}, 'photos': [{'height': 3337, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/110576967304605928144">INSA Toulouse</a>'], 'photo_reference': 'CmRaAAAAOzNpiXJmzSacz1c8YieAHzBb3tVnnTwmdfx4jkce5zT9p3hK7b_iaQ3PfQjpZREg11dzNHXdysVbj6oLT4vDu_S79KKxZMBC4rv1nycc9HHTkRJm0K35eyLdvjqYtn4oEhDUCgoXBpT5jq9scshbrVvfGhRnBSEKpywwVwCSGqSUSVFgtrEBkA', 'width': 5000}], 'place_id': 'ChIJk0KIgT-8rhIRa5Z1vqKrB7A', 'plus_code': {'compound_code': 'HF99+V3 Toulouse', 'global_code': '8FM3HF99+V3'}, 'rating': 4.6, 'reference': 'ChIJk0KIgT-8rhIRa5Z1vqKrB7A', 'types': ['university', 'point_of_interest', 'establishment'], 'user_ratings_total': 73}, {'business_status': 'OPERATIONAL', 'formatted_address': '10 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8750991, 'lng': 2.3489738}, 'viewport': {'northeast': {'lat': 48.87644047989271, 'lng': 2.350321729892723}, 'southwest': {'lat': 48.87374082010727, 'lng': 2.347622070107278}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/shopping-71.png', 'name': 'OpenClassrooms Studios', 'photos': [{'height': 4000, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/102788663327843980176">A Google User</a>'], 'photo_reference': 'CmRaAAAAU9WJ7tBrCkhzHOJ6eIz1IYOF0YNYbKFbj6jVjHoPH9zMApZZuGjzQfGabs8_1AjsP_lnHttv9pojNhS25fDuepn6_9FEkZ4JWGLH1eXaWqA-nilAo0sVxORxm4lL7Qf2EhAa6bx_FF20928AYC5vCZgaGhSs0Vp9aYQqHZMv5S1VBtz1T---QQ', 'width': 6000}], 'place_id': 'ChIJLUzI3xRu5kcRX7qwoQiY5bM', 'plus_code': {'compound_code': 'V8GX+2H Paris', 'global_code': '8FW4V8GX+2H'}, 'rating': 4.5, 'reference': 'ChIJLUzI3xRu5kcRX7qwoQiY5bM', 'types': ['electronics_store', 'home_goods_store', 'point_of_interest', 'store', 'establishment'], 'user_ratings_total': 6}]
expectedvalue_test_quartier_api_gmaps = {"10 Quai de la Charente, 75019 Paris, France": " Quai de la Charente", "10 Cité Paradis, 75010 Paris, France": " Cité Paradis" }
expectedvalue_test_recherche_api_wiki = {'10 Quai de la Charente, 75019 Paris, France': {'3120618': {'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente', 'extract': '<p class="mw-empty-elt">\n</p>\n<p>Le <b>quai de la Charente</b> est un quai situé le long du canal Saint-Denis, à Paris, dans le <abbr class="abbr" title="Dix-neuvième">19<sup>e</sup></abbr>\xa0arrondissement. \n</p>\n\n\n<h2><span id="Situation_et_acc.C3.A8s"></span><span id="Situation_et_accès">Situation et accès</span></h2>\n<p>Il fait face au quai de la Gironde.\n</p>\n<h2><span id="Origine_du_nom">Origine du nom</span></h2>\n<p>Il est nommé d\'après la Charente, un fleuve français qui donna son nom à deux départements\xa0: la Charente (16) et la Charente-Maritime (17). \n</p>\n<h2><span id="Historique">Historique</span></h2>\n<p>Cette ancienne voie du village de La Villette a reçu son nom actuel en 1863, lors de son rattachement à la voirie parisienne.\n</p>\n<h2><span id="Voir_aussi">Voir aussi</span></h2>\n<h3><span id="Articles_connexes">Articles connexes</span></h3>\n<ul><li>Liste des voies de Paris</li>\n<li>Liste des voies du 19e arrondissement de Paris</li></ul><h3><span id="Navigation">Navigation</span></h3>\n<ul id="bandeau-portail" class="bandeau-portail"><li><span><span></span> <span>Portail de Paris</span> </span></li> <li><span><span></span> <span>Portail de la route</span> </span></li>                   </ul>'}}, '10 Cité Paradis, 75010 Paris, France': {'5653202': {'pageid': 5653202, 'ns': 0, 'title': 'Cité Paradis', 'extract': '<p class="mw-empty-elt">\n</p>\n<p>La <b>cité Paradis</b> est une voie publique située dans le <abbr class="abbr" title="Dixième">10<sup>e</sup></abbr>\xa0arrondissement de Paris.\n</p>\n\n\n<h2><span id="Situation_et_acc.C3.A8s"></span><span id="Situation_et_accès">Situation et accès</span></h2>\n<p>La cité Paradis est une voie publique située dans le <abbr class="abbr" title="Dixième">10<sup>e</sup></abbr>\xa0arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d\'Hauteville et la troisième en impasse.\n</p>\n<ul class="gallery mw-gallery-packed"><li class="gallerycaption">Vues de la cité</li>\n\t\t<li class="gallerybox" style="width: 115.33333333333px">\n\t\t<li class="gallerybox" style="width: 202px">\n</ul><p>Ce site est desservi par les lignes <span>\u2009<span data-sort-value="08 !"></span>\u2009<span data-sort-value="09 !"></span></span> à la station de métro <i>Bonne-Nouvelle</i> et par la ligne <span>\u2009<span data-sort-value="07 !"></span></span> à la station <i>Poissonnière</i>.\n</p>\n<h2><span id="Origine_du_nom">Origine du nom</span></h2>\n<p>Elle porte ce nom en raison de sa proximité avec la rue éponyme.\n</p>\n<h2><span id="Historique">Historique</span></h2>\n<p>La cité Paradis a été aménagée sur les anciens jardins de l\'hôtel Titon dont la façade arrière est visible au fond de l\'impasse.\n</p><p>La partie débouchant rue de Paradis a été ouverte en 1893 et celle débouchant rue d\'Hauteville en 1906.\n</p>\n<h2><span id="R.C3.A9f.C3.A9rences"></span><span id="Références">Références</span></h2>\n\n<h2><span id="Bibliographie">Bibliographie</span></h2>\n<ul><li><span id="Hillairet1972"><span id="Jacques_Hillairet1972">Jacques <span>Hillairet</span>, <cite class="italique">Dictionnaire historique des rues de Paris</cite>, Paris, Les Éditions de Minuit, 1972, 1985, 1991, 1997,\xa0<abbr class="abbr" title="et cetera">etc.</abbr> (<abbr class="abbr" title="première">1<sup>re</sup></abbr>\xa0<abbr class="abbr" title="édition">éd.</abbr> 1960), 1\xa0476\xa0<abbr class="abbr" title="pages">p.</abbr>, 2 <abbr class="abbr" title="volume">vol.</abbr>\xa0 <small>[détail des éditions]</small> <small style="line-height:1em;">(ISBN\xa0<span>2-7073-1054-9</span>, OCLC\xa0<span>466966117</span>, présentation en ligne)</small><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Dictionnaire+historique+des+rues+de+Paris&amp;rft.place=Paris&amp;rft.pub=Les+%C3%89ditions+de+Minuit&amp;rft.aulast=Hillairet&amp;rft.aufirst=Jacques&amp;rft.date=1985&amp;rft.tpages=1%C2%A0476&amp;rft.isbn=2-7073-1054-9&amp;rft_id=info%3Aoclcnum%2F466966117&amp;rfr_id=info%3Asid%2Ffr.wikipedia.org%3ACit%C3%A9+Paradis"></span></span></span>.</li></ul><h2><span id="Annexes">Annexes</span></h2>\n<h3><span id="Article_connexe">Article connexe</span></h3>\n<ul><li>Liste des voies du <abbr class="abbr" title="Dixième">10<sup>e</sup></abbr> arrondissement de Paris</li></ul><h3><span id="Lien_externe">Lien externe</span></h3>\n<ul><li>Cité Paradis (mairie de Paris)</li></ul><ul id="bandeau-portail" class="bandeau-portail"><li><span><span></span> <span>Portail de Paris</span> </span></li> <li><span><span></span> <span>Portail de la route</span> </span></li>                   </ul>'}}}

expectedvalue_test_response = ''