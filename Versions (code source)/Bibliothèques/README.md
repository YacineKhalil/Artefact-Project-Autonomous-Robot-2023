# Bibliothèque de fonctions python

Tous les scripts utiles au fonctionnement de la voiture en mode manuel ou automatique sont regroupés ici.

## B_conduite_auto.py

Ensemble des fonctions liées à la vision, utiles pour le mode conduite automatique : estimation de la distance à un ArUco, estimation de l'angle d'inclinaison par rapport à la normale à un ArUco ...

Explications :

## Distance à un marqueur :

![distance_1](Documentation/Vision/distance_1.png)

![distance_2](Documentation/Vision/distance_2.png)

![distance_3](Documentation/Vision/distance_3.png)

## Inclinaison à la normale d'un marqueur :

![deviation_1](Documentation/Vision/deviation_1.png)

![deviation_2](Documentation/Vision/deviation_2.png)

## B_fonctions_calibrage.py

Fonctions utiles pour calibrer les moteurs afin de pouvoir faire avancer le robot d'un nombre de mètres déterminé et afin de pouvoir le faire tourner d'un angle déterminé (nous ne disposons pas d'un retour sur la vitesse de rotation des roues, qui aurait pu permettre de se passer de ce genre de calibrages)

L'idée est globalement de faire une règle de proportionnalité en utilisant time.sleep : 

 > Si en ayant tourné à vitesse v_rotation pendant T secondes on a fait une rotation de alpha degrés, pour faire une rotation de beta degrés on peut tourner à vitesse v_rotation pendant beta * (T/alpha) secondes


## B_lecture_bibli.py

Cette fonction est utile pour le contrôle du robot en mode manuel (voir documentation du dossier Communication dans Epreuve_intermediaire).

## B_module_moteur.py

Le script B_module_moteur.py permet de contrôler les moteurs via le simple appel de la fonction MotorDriver.MotorRun.

Un code similaire est présent sur le site du fabricant du motor driver :

[Documentation de la carte de contrôle des moteurs](https://www.waveshare.com/wiki/Motor_Driver_HAT)

Le script utilise la bibliothèque PCA9685 qui réalise un asservissement des moteurs grâce à la carte de contrôle des moteurs.

## B_module_vitesse.py

Ce fichier est utilisé lors de la conduite en mode manuel, afin de faire le lien entre la position du click du pilote et le contrôle des moteurs (soit la tension à appliquer à chacun des moteurs).

Le pilote dispose d'un joystick et la position de son click est utilisée par le module vitesse selon ces principes :

![docu_calcul_U1_U2-1](Documentation/Conduite/docu_calcul_U1_U2-1.png)

![docu_calcul_U1_U2-2](Documentation/Conduite/docu_calcul_U1_U2-2.png)

![docu_calcul_U1_U2-3](Documentation/Conduite/docu_calcul_U1_U2-3.png)

![docu_calcul_U1_U2-4](Documentation/Conduite/docu_calcul_U1_U2-4.png)

## B_PCA9685

[Documentation de la carte de contrôle des moteurs](https://www.waveshare.com/wiki/Motor_Driver_HAT)

Ce module a été entièrement repris du site du fabricant de la carte de contrôle des moteurs, et est utile dans la mise en rotation de chaque moteur.

## B_rencentre_bibli.py

Ce fichier est utilisé par le robot pour centrer un ArUco dans son champ de vision, lors de la conduite automatique.

Détail en pseudo-code de la méthode pour ce faire :

    ->Tant qu'on n'a pas centré dans le champ de vision un ArUco de la parité désirée

    ->s'immobiliser

    ->prendre plusieurs captures de l'écran

    ->si aucun ArUco n'est détecté

        ->si un ArUco a déjà été vu mais qu'il n'a pas été centré (on l'a perdu de vue pendant le recadrage)

            ->pivoter à gauche sur place

        ->sinon

            ->pivoter à droite sur place

    ->sinon (un ArUco est détecté)

        -> tourner à droite jusqu'à ce que l'ArUco soit centré dans le champ de vision (<=> la moyenne des abscisses des coins du marqueur est à peu près nulle)


## B_recentrer_mvmt_bibli.py

Le script B_recentrer_mvmt_bibli.py associe les fonctionnalités du fichier précédent à un mouvement rectiligne.

## B_stop_motor.py

Ce module permet d'arrêter le fonctionnement des deux moteurs présents sur la voiture, et est notamment utile lorsque le contrôle du robot a été perdu, afin d'éviter une collision.