

var input = document.getElementById("input_utilisateur");


//  Classe de l'objet qui est chargé de l'interaction entre l'utilisateur et l'application
class GestionnaireInteraction
{    

    constructor()
    {
        this.load_progress = 0;
        this.parentMonCanvas = document.getElementById('contain_canvas');
        this.monCanvas;
		this.ctx ;

    }

    loading()
    { // Active l'icone de chargement

    	var moncanvas = document.createRange().createContextualFragment('<canvas id="load" style="height: 100%;"></canvas>');
    	this.parentMonCanvas.appendChild(moncanvas);

    	this.monCanvas = document.getElementById('load');
    	this.ctx = this.monCanvas.getContext('2d');

    	var var_att = {
    		load_progress: this.load_progress,
    		monCanvas: this.monCanvas,
    		ctx: this.ctx,
    		interrupteur_loading: this.interrupteur_loading
    	};

    	console.log(var_att);

    	setInterval(function()
    	{
    		
			if ( var_att.load_progress < Math.PI*2 ) 
    		{    var_att.load_progress += 0.05;    }
    		else if ( var_att.load_progress >= Math.PI*2 )
    		{    var_att.load_progress = 0;    }

			var_att.ctx.clearRect(0, 0, 300, 150);
			var_att.ctx.strokeStyle = "blue";
			var_att.ctx.lineWidth = 25;
			var_att.ctx.lineCap = "round";
			var_att.ctx.beginPath();
			var_att.ctx.arc(150, 75, 60, 0, 0 + var_att.load_progress );
			var_att.ctx.stroke();
			var_att.ctx.closePath();

    		

    	}, 5);
    }

    stopload()
    {  // Désactive l'icone de chargement

    	this.parentMonCanvas.removeChild(this.monCanvas); 

    }

    put_user_message(message)
    {  // Affiche le message de l'utilisateur dans le dialogue

        this.contenu_string = '<div class="contain_dialogue" style="width: 100%;'+
        'display: flex;justify-content: left;margin-bottom: 10px;" ><div class="contain_dialogue_utilisateur" style="width: 60%;'+
        'display: flex;justify-content: left;" ><div class="contain_dialogue_text"'+
        ' style="min-height: 35px;' + ' border-radius: 10px;max-width: 100%; border: solid silver 1px;'+
        ' background: rgb(247, 247, 247);' + 'display: inline-block;padding: 7px;" >'+ message +
        '</div></div></div>';
        this.contenu_html = document.createRange().createContextualFragment(this.contenu_string);

        document.getElementById('contain_dialogue').appendChild(this.contenu_html);

    }

    put_pybot_message(message, wait)
    {  // Affiche le message de l'application dans le dialogue

        this.contenu_string = '<div class="contain_dialogue" style="width: 100%;'+
        'display: flex;justify-content: right;margin-bottom: 10px;" ><div class="contain_dialogue_pybot" style="width: 60%;'+
        'display: flex;justify-content: right;" ><div class="contain_dialogue_text"'+
        ' style="min-height: 35px;' + ' border-radius: 10px;max-width: 100%; border: solid silver 1px;'+
        ' background: rgb(247, 247, 247);' + 'display: inline-block;padding: 7px;" >'+ message +
        '</div></div></div>';
        this.contenu_html = document.createRange().createContextualFragment(this.contenu_string);

        var wait0 = wait;
        var to_put = this.contenu_html;
        setTimeout( function(){ document.getElementById('contain_dialogue').appendChild(to_put); }, wait0 );

    }

    put_pybot_map(position_pointed, wait)
    {
        //    Affiche un lieu sur une carte google maps

        this.contenu_map_string = '<div class="contain_dialogue" style="width: 100%;'+
        'display: flex;justify-content: right;margin-bottom: 10px;" ><div class="map" style="border-radius: 10px;border: solid silver 1px;height: 200px; width: 1200px; border: solid 1px;" ></div></div>';
        this.contenu_map_html = document.createRange().createContextualFragment(this.contenu_map_string);

        var wait0 = wait;
        var to_put = this.contenu_map_html;
        var position_pointed0 = position_pointed;

        setTimeout( function()
            { 

                document.getElementById('contain_dialogue').appendChild(to_put); 

                var mydivs = document.getElementsByClassName('map');
                console.log('mes divs : ', mydivs)
                console.log('ma div : ', mydivs[mydivs.length - 1])
                var map0, marker;
                var position0 = position_pointed0;

                map0 = new google.maps.Map( mydivs[mydivs.length - 1] , {
                    center: position0,
                    zoom: 14,
                });

                marker = new google.maps.Marker({position: position0, map: map0});


            }, wait0 );
        
    }


}


// Création de l'objet interaction

var gestionnaire_interaction = new GestionnaireInteraction();









//           Envoie de la demande


document.addEventListener("keypress", function()

	{

        // Detection de l'appui de la touche entrée
		if ( event.keyCode == 13 ) 
		{

            // Insertion du message utilisateur dans le dialogue et activation de l'icone de chargement
            gestionnaire_interaction.put_user_message(input.value)
			gestionnaire_interaction.loading();

            // envoie de la requete ajax et reinitialisation du formulaire
			var xhr = new XMLHttpRequest();
			xhr.open('GET', '/question?question=' + input.value );
			xhr.send(null);
            input.value = '';


			xhr.addEventListener('readystatechange', function()
			{ // On gère ici une requête asynchrone

		        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) 
                { // Si le fichier est chargé sans erreur
		        	
		        	gestionnaire_interaction.stopload();
                    var from_backend = JSON.parse(xhr.responseText)
                    if ( from_backend.length == 0 ) 
                    {
                        //  Aucun résultat n'est trouvé
                        console.log("Aucun résultat n'a été trouvé après le parsage")
                        gestionnaire_interaction.put_pybot_message('Désolé mon kiki.\nJe ne peux pas traité ta demande ...', 1000);
                        gestionnaire_interaction.put_pybot_message('Réessaye peut-être une autre', 1500);
                    }
                    else if ( from_backend.length == 1 )
                    {
                        // Un résultat est trouvé
                      
                        console.log( from_backend );

                        for (var i = 0; i < from_backend.length; i++) 
                        {
                            gestionnaire_interaction.put_pybot_message(from_backend[i][1][0], 1000*(i+1) );
                            gestionnaire_interaction.put_pybot_message(from_backend[i][1][1], 1500*(i+1) );

                            // Affichage du contenu des réponses
                            for (var i0 = 2; i0 < from_backend[i][1].length; i0++) 
                            {
                                gestionnaire_interaction.put_pybot_message(from_backend[i][1][i0][0], 2000*(i+1)*(i0-1) );
                                gestionnaire_interaction.put_pybot_map(from_backend[i][1][i0][1], 2500*(i+1)*(i0-1) );
                                if ( from_backend[i][1][i0][3] != '' ) 
                                {
                                    gestionnaire_interaction.put_pybot_message(from_backend[i][1][i0][2], 3000*(i+1)*(i0-1) );
                                    gestionnaire_interaction.put_pybot_message(from_backend[i][1][i0][3], 3500*(i+1)*(i0-1) );
                                }
                                
                            }
                            
                        }
                        
                        
                    }
                    else
                    {
                        //  Plusieurs caractères sont obtenus après le parsage
                        resultat_apres_parsage = []
                        for (var i1 = 0; i1 < from_backend.length; i1++) {    resultat_apres_parsage.push( from_backend[i1] );    }
                        console.log("Plusieurs résultats ont été trouvé après le parsage :", resultat_apres_parsage);
                        gestionnaire_interaction.put_pybot_message('Désolé mon kiki mais je ne peux pas traité ta demande ...', 1000);
                        gestionnaire_interaction.put_pybot_message('Réessaye peut-être une autre', 1500);
                    }

		        }

			});

		}

	});





