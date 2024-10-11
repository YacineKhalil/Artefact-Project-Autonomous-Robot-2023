# Amélioration de la vitesse de démarrage du robot

Les modules de ce dossier servent à automatiser le démarrage du robot pour la conduite manuelle (plus généralement dans le cadre de l'épreuve intermédiaire).
Ils permettent ainsi de lancer le robot sans utiliser la connexion en ssh, il faut uniquement connaître l'adresse du robot pour se connecter à l'interface web de contrôle du véhicule.

## Description

On utilise des fichiers .sh (fichier bash de commandes Linux) pour automatiser la procédure.

**->** demarrage.sh exécute tous les scripts python nécessaires au fonctionnement du robot.

**->** parametrage_droit.sh permet de donner tous les droits d'exécution aux scripts précédents (opération à refaire à chaque pull du git)

**->** init_commandes.py réinitialise le fichier de contrôle de la voiture en mode manuel (qui contient avant cette opération les dernières commandes données lors de la précédente utilisation du robot)

Ces fichiers se lancent après allumage de la carte Raspberry, dès lors que cette dernière a accès à une connexion wifi. Cela est permis par manipulation du fichier run-at-startup.service (voir ci-dessous)

## Procédure détaillée à suivre

1] donner le droit d'exécution de script.py à robot-pi12
ligne de commande à entrer après avoir ajouté script.py à la mémoire de la Raspberry :
chmod +x <chemin vers script.py>

ou

faire directement "parametrage_droits.sh" dans la console (ce qui automatise cet octroi de droits pour ne pas avoir à le faire à la main à chaque pull du git)

2] faire exécuter script.py au démarrage de la Raspberry après que le réseau soit disponible
1ère commande qui crée le fichier de configuration :
sudo nano /etc/systemd/system/run-at-startup.service

y copier le texte suivant :
[Unit]
Description=Lance le contrôle de la voiture
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=<chemin vers script.sh (bash)>
Restart=on-failure

[Install]
WantedBy=multi-user.target

3] créer fichier bash pour exécuter un script python
première ligne : #!/bin/bash
deuxième ligne : sudo python3 <chemin_accès/fichier.py>

4] activer les changements (de run-at-startup.service)
1ère commande
systemctl daemon-reload
2ème commande
systemctl enable run-at-startup.service