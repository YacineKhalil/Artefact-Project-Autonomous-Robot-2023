# Communication entre le pilote et le robot par interface web

La communication se fait via wifi, en utilisant un navigateur internet quelconque sur un ordinateur/téléphone connecté au même réseau wifi que la Raspberry du robot. Pour se connecter à l'interface web, il faut entrer dans la barre de recherche du navigateur :

> (adresse ip du robot):8080/static/site_joystick

Il est possible de connaître l'adresse ip du robot depuis un invité de commandes en appelant :

> hostname -I

## Serveur

Le serveur est hébergé directement sur la Raspberry, en excécutant la commande :

> python3 heberger_serveur.py

Ce serveur tourne grâce au module Bottle de python, solution légère qui se base sur le protocole http (Bottle est similaire à Flask).

Lorsque le pilote se connecte au serveur ouvert, ce dernier lui envoie les fichiers de static, puis l'appareil du client renvoie toutes les 0.1 secondes les données de son click, grâce à la méthode POST. Alors ces données sont inscrites dans le fichier x_y_R_isAuto.txt grâce à la fonction de stocke_donnees.py.

## Interface web

L'interface web fonctionne grâce aux fichiers du dossier static (image d'un joystick, fichier css pour la présentation visuelle du site web, fichier html pour la structure de base du site et fichier js pour l'interactivité de l'interface), servies par le serveur. 

Le fichier js permet notamment de déterminer le lieu du click du pilote par rapport au centre du joystick.

Un interrupteur permet de passer du mode conduite manuelle au mode conduite automatique et inversement.

Visuel de l'interface :

![interface_web](Documentation/Interface/interface_web.jpg)