

var input = document.getElementById("input_utilisateur");






class ContainDialogueUtilisateur 
{
    constructor(type_contenu0, obj_contenu0)
    {

        if ( type_contenu0 == 'text' )
        {
        	this.contenu_string = '<div class="contain_dialogue" style="width: 100%;border: solid silver 1px;'+
        	'display: flex;justify-content: left;margin-bottom: 10px;" ><div class="contain_dialogue_utilisateur" style="width: 60%;'+
        	'border: solid silver 1px;display: flex;justify-content: left;" ><div class="contain_dialogue_text"'+
        	' style="min-height: 35px;' + ' border-radius: 10px;max-width: 100%; border: solid silver 1px;'+
        	' background: rgb(247, 247, 247);' + 'display: inline-block;padding: 7px;" >'+ obj_contenu0.contenu +
        	'</div></div></div>';
        	this.contenu_html = document.createRange().createContextualFragment(this.contenu_string);
        }
        else if ( type_contenu0 == 'map' )
        {
        	// ...
        }
    }

}




class ContainDialogueText
{
    constructor(text) 
    {
        this.contenu = text ;
    }

}





class GestionnaireInteraction
{

    constructor()
    {
        this.load_progress = 0;
        this.parentMonCanvas = document.getElementById('contain_canvas');
        this.monCanvas;
		this.ctx ;
		//this.interrupteur_loading = 0 ;

    }

    loading()
    {

    	//this.interrupteur_loading = 1;
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


}



var gestionnaire_interaction = new GestionnaireInteraction();


//gestionnaire_interaction.loading();









//           Envoie de la demande


document.addEventListener("keypress", function()

	{

		if ( event.keyCode == 13 ) 
		{

			var contain_dialogue_utilisateur = new ContainDialogueUtilisateur('text', new ContainDialogueText(encodeURIComponent(input.value)));
			var contain_dialogue = document.getElementById('contain_dialogue');
			contain_dialogue.appendChild(contain_dialogue_utilisateur.contenu_html);

			gestionnaire_interaction.loading();

			var xhr = new XMLHttpRequest();
			xhr.open('GET', '/question?question=' + encodeURIComponent(input.value) );
			xhr.send(null);

			xhr.addEventListener('readystatechange', function()
			{ // On gère ici une requête asynchrone

		        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) { // Si le fichier est chargé sans erreur
		        	
		        	gestionnaire_interaction.stopload();
		            alert(xhr.responseText);
		        }

			});

		}

	});





//             google maps
/*
let map0, marker;

var position0 = { lat: 4.25, lng: 10.49 };

function initMap() {
  map0 = new google.maps.Map(document.getElementById("map"), {
    center: position0,
    zoom: 12
  });

  marker = new google.maps.Marker({position: position0, map: map0});
}
*/