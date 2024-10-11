/*INFORMATION : on fait l'amalgame dans le nom de certaines variables entre souris (mouse) et doigt*/

var w = window.innerWidth;
var h = window.innerHeight;
/*taille de la fenêtre en pixels sur l'écran de l'utilisateur*/


const  mousePosText = document.getElementById('pos_souris')
/*la valeur du texte dans la balise d'id pos_souris (voir html) sera égale à mousePosText*/

let mousePos = { x: undefined, y: undefined };
/*équivalent du dictionnaire en javascript*/

var appui=false;
/*avant que l'utilisateur clique*/



/*POUR UTILISATEUR SOURIS*/

window.addEventListener('mousedown', (event) => {
appui=true	    
});
/*lorsque l'utilisateur est en train de cliquer la varibale appui devient vraie*/

window.addEventListener('mousemove', (event) => {
if (appui) {
mousePos = { x: event.clientX, y: event.clientY };
mousePosText.textContent = `(${mousePos.x-w/2}, ${-(mousePos.y-h/2)})`;
}
});
/*lorsque l'utilisateur bouge sa souris, on récupère la position du pointeur mais seulement si l'utilisateur est en train de cliquer, et ce par rapport au centre de la fenêtre (x et y sont calculés pour une origine en haut à gauche d'où -w/2 et -h/2)*/

window.addEventListener('mouseup', (event) => {
appui=false
mousePos = { x: 0, y: 0 };
mousePosText.textContent = `(0,0)`;
});
/*si l'utilisateur arrête de cliquer, on considère qu'il clique au centre de la fenêtre (centre du joystick) afin que la voiture s'arrête*/




/*POUR UTILISATEUR MOBILE*/

window.addEventListener('touchstart', (event) => {
appui=true	    
});
/*lorsque l'utilisateur est en train de cliquer la varibale appui devient vraie*/

window.addEventListener('touchmove', (event) => {
if (appui) {
mousePos = { x: event.changedTouches[0].pageX, y: event.changedTouches[0].pageY };
    mousePosText.textContent = `(${mousePos.x-w/2}, ${-(mousePos.y-h/2)})`;
}
});
/*lorsque l'utilisateur bouge son diogt, on récupère sa position mais seulement si l'utilisateur est en train de cliquer, et ce par rapport au centre de la fenêtre (x et y sont calculés pour une origine en haut à gauche d'où -w/2 et -h/2)*/

window.addEventListener('touchend', (event) => {
appui=false
mousePos = { x: 0, y: 0 };
mousePosText.textContent = `(0,0)`;
});
/*si l'utilisateur arrête de cliquer, on considère qu'il clique au centre de la fenêtre (centre du joystick) afin que la voiture s'arrête*/



/*AFFICHER R*/
const  RText = document.getElementById('R');
RText.textContent=`${Math.min(0.85*h/2,0.85*w/2)}`;



/*INTERRUPTEUR (SWITCH) : MODE CONDUITE*/
const  mode_conduite = document.getElementById('mode_conduite')
var isChecked=document.getElementById("switch").checked;
window.addEventListener('click', (event) => {
isChecked=document.getElementById("switch").checked
mode_conduite.textContent=`${isChecked}`;
});
/*A chaque click, on modifie la valeur du texte d'id mode_conduite en fonction de l'état de l'interrupteur (certains de ces clicks peuvent ne pas être sur l'interrupteur*/


/*RECUPERER ET STOCKER x,y,R et isAuto*/
function stocker_donnees(){
	$.post( "/envoie_donnees", {x_y: mousePosText.textContent,R: Math.min(0.85*h/2,0.85*w/2),isAuto: mode_conduite.textContent} );
}
/*fonction qui appelle le script python qui va modifier le fichier de stockage, en lui passant (x,y), R et isAuto*/

function repeter_stocker_donnees(){
	setInterval(stocker_donnees,100);
}
/*fonction qui permet de répéter l'appel de stocker_donnees() toutes les x millisecondes (en boucle infinie)*/


repeter_stocker_donnees();
/*appel de la fonction précédente*/
