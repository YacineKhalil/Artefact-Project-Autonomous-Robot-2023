# Exécution locale sur la Raspberry

Le dossier Pilotage est dédié à des fonctions qui s'exécutent localement sur la Raspberry (à l'inverse dossier Communication). Elles permettent entre autres de contrôler les moteurs.

## Fonctions de la bibiliothèque

Tous les fichiers commençant par 'B_" font partie d'une bibliothèque commune aux épreuves finale et intermédiaire. Leur fonctionnement est détaillé dans le dossier Bibliothèques.

## Bruit moteur

Le bruit de moteur est une fonctionnalité qui a été ajoutée à la fin du projet pour le loisir. L'intensité du bruit s'adapte en fonction de la vitesse de la voiture.

## main_intermediaire.py

Le fichier main_intermediaire.py doit être lancé lorsque le serveur est hébergé.

    Le script récupère d'abord les valeurs inscrites dans x_y_R_isAuto.txt (dossier Communication)

    Si le bouton de conduite automatique est désactivée

        Le script rentre dans le mode conduite manuelle, avec les paramètres récupérés dans x_y_R_isAuto.txt

    Sinon

        Le script rentre en mode conduite automatique

            Faire en boucle les opérations 

            La voiture cherche un marqueur (pair ou impair en fonction des instructions de l'épreuve intermédiaire)

            Elle cadre le marqueur trouvé dans son champ de vision

            Elle avance sur une durée déterminée

            Elle s'arrête

            Revenir en début de boucle