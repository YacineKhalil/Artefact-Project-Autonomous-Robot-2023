# Code source pour l'épreuve intermédiaire

Le code source pour l'épreuve intermédiaire se divise en deux parties :

- communication entre le pilote et la voiture (via interface web de joystick)

- pilotage de la voiture (se produit en interne sur la Raspberry)

Ces deux divisions des opérations effectuées par le robot s'exécutent en parallèle (il y a un thread communication parallèlement à un thread pilotage).

Le lien entre ces deux fils d'exécutions est le fichier texte x_y_R_isAuto.txt :

-> La partie communication consiste à modifier le fichier x_y_R_isAuto.txt grâce aux directives du pilote (qui utilise une interface web)

-> La partie pilotage consiste à utiliser les valeurs inscrites dans le fichier x_y_R_isAuto.txt pour contrôler les moteurs

**Pour démarrer le robot dans la logique de l'épreuve intermédiaire, on peut ouvrir deux fenêtres de l'invité de commandes d'un ordinateur, se connecter en ssh au robot sur chacune d'entre elles puis naviguer vers /Communication et vers /Pilotage respectivement. Il reste alors à rentrer les commandes, respectivement :**

> python3 heberger_serveur.py

> python3 main_epreuve_intermediaire.py