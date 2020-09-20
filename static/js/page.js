

var input = document.getElementById("input_utilisateur");



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
    {

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
    {
    	this.parentMonCanvas.removeChild(this.monCanvas); 
    }

    put_user_message(message)
    {

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
    {

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
        //             google maps

        this.contenu_map_string = '<div class="contain_dialogue" style="width: 100%;'+
        'display: flex;justify-content: right;margin-bottom: 10px;" ><div class="map" style="border-radius: 10px;border: solid silver 1px;height: 200px; width: 1200px; border: solid 1px;" ></div></div>';
        this.contenu_map_html = document.createRange().createContextualFragment(this.contenu_map_string);

        var wait0 = wait;
        var to_put = this.contenu_map_html;
        var position_pointed0 = position_pointed

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



var gestionnaire_interaction = new GestionnaireInteraction();









//           Envoie de la demande


document.addEventListener("keypress", function()

	{

		if ( event.keyCode == 13 ) 
		{

            gestionnaire_interaction.put_user_message(input.value)

			gestionnaire_interaction.loading();

			var xhr = new XMLHttpRequest();
			xhr.open('GET', '/question?question=' + input.value );
			xhr.send(null);
            input.value = ''

			xhr.addEventListener('readystatechange', function()
			{ // On gère ici une requête asynchrone

		        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) { // Si le fichier est chargé sans erreur
		        	
		        	gestionnaire_interaction.stopload();
                    var from_backend = JSON.parse(xhr.responseText)
                    if ( from_backend.length == 0 ) 
                    {
                        //  Aucun résultat n'est trouvé
                        console.log("Aucun résultat n'a été trouvé après le parsage")
                    }
                    else if ( from_backend.length == 1 ) 
                    {
                        gestionnaire_interaction.put_pybot_message('Bien sûr mon poussin !', 1500);

                        if ( from_backend[0][1].length > 1 ) 
                        {
                            gestionnaire_interaction.put_pybot_message("J'en ai " + from_backend[0][1].length + ' les voici !' , 2000 );

                            for (var i = 0; i < from_backend[0][1].length; i++) 
                            {
                                gestionnaire_interaction.put_pybot_message(from_backend[0][1][i][0].formatted_address, 1500 + (1000*(i+1)) );
                                gestionnaire_interaction.put_pybot_map(from_backend[0][1][i][0].geometry.location , 1500 + (1000*(i+1)) );
                            }


                            for (var i0 = 0; i0 < from_backend[0][1].length; i0++) 
                            {

                                for (var i1 in from_backend[0][1][i0][1])
                                {
                                    
                                    if ( from_backend[0][1][i0][1][i1].extract != undefined ) 
                                    {
                                        gestionnaire_interaction.put_pybot_message("Mais t'ai-je déjà raconté l'histoire de " + from_backend[0][1][i0][1][i1].title + ' ?' , 1500 + (1000*(i+1)) );
                                        i += 1;
                                        gestionnaire_interaction.put_pybot_message( from_backend[0][1][i0][1][i1].extract , 1500 + (1000*(i+1)) );
                                        i += 1;
                                        console.log('du backend 0 :', from_backend[0][1][i0][1][i1] )
                                    }
                                    
                                }

                            }
                            
                        }
                        
                        
                    }
                    else
                    {
                        //  Plusieurs caractères sont obtenus après le parsage
                        console.log("Plusieurs résultats ont été trouvé après le parsage")
                    }

		        }

			});

		}

	});





