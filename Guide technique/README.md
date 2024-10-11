# Guide développeur

Ce guide recense les méthodes importantes que nous avons suivies pour développer le robot.

**NB** : Avant que la Raspberry ait accès au wifi, les manipulations peuvent être faites directement sur la carte usb insérée dans la Raspberry (en la mettant dans un autre ordinateur)

# Configuration wifi

### La première étape pour pouvoir communiquer avec la Raspberry Pi via wifi est de connecter la carte à un réseau

Lorsque le réseau wifi nécessite un certificat, il faut mettre le fichier de certificat dans le boot et effectuer d'autres opérations : [suivre ce lien](https://discourse.r2.enst.fr/t/configuration-wpa-supplicant-pour-le-reseau-campustelecom/269)

# Connexion ssh

### Pour pouvoir communiquer avec la Raspberry Pi via wifi et ainsi modifier son code source, on peut utiliser l'invité de commandes de n'importe quel ordinateur

Pour ce faire, il faut ajouter une des clefs ssh de l'ordinateur depuis lequel on veut contrôler la Raspberry dans un dossier spécifique : [lien vers un tutoriel](https://www.raspberryme.com/configuration-des-cles-ssh-sur-le-raspberry-pi/)

Moralement, on donne ainsi le contrôle de la Raspberry aux ordinateurs associés aux clefs ssh ajoutées.

Il est alors possible de se connecter en ssh à la Raspberry depuis un ordinateur autorisé et connecté au même wifi en ouvrant un invité

**Commande pour se connecter à la raspberry (sur campus telecom) :**

> ssh pi@robotpi-12.enst.fr


**Commande pour éteindre le raspberry :**

> sudo poweroff 

**Si la raspberry est connectée sur un rooter plutôt que sur le wifi Campus-Télécom, on fera plutôt :**

> ssh pi@robotpi-12.enst.fr

# Utiliser GIT pour développer facilement une solution

### Configuration du GIT sur l'ordinateur de chaque développeur

- Installer git au préalable.

- Générer une clé SSH via ssh-keygen

- Mettre la clef dans une destination, la clé ssh sera notée .ssh dans les dossiers. 
Il peut être judicieux d'ajouter un mot de passe à cette clef.

Il est important de bien différencier deux fichiers dans le cadre du chiffrement asymétrique :

Clé privée **->** id_rsa 
Cette clé ne doit en aucun cas être partagée

Clé publique **->** Id_rsa.pub 
Cette clé a vocation à être partagée

Ensuite, il convient d'ajouter sa clé sur le gitlab

### Liste de quelques commandes utiles

Pour récupérer les dossiers : 

> git clone <lien_projet> ; 

cette commande est à faire dans le fichier où je souhaite créer une copie du dépôt

Faire un dépôt :

> git add <name_file> 

(pour un seul fichier)

> git add -A 

(pour tous les fichiers). 

Pour le commit (avant envoi) : 

> git commit -m  "résumé des modifications apportées"

Pour envoyer :

> git push

Remarque : S’il y a eu une modification entre temps : 

>git pull. 

Informations pour le dépôt git de notre raspberry : 

MDP : walle

Full Name : Walle-E

Room number : 12

# Mettre la Raspberry à l'heure

Pour mettre à l'heure la Raspberry (connectée au wifi), il est possible de suivre les étapes suivantes :

Accéder au dossier de configuration : /etc/systemd/timesyncd.conf

Utiliser la commande cd nano (dans l'invité) pour modifier le fichier :

    [Time]

    NTP=ntp.enst.fr

    FallbackNTP=0.debian.pool.ntp.org 1.debian.pool.ntp.org 2.debian.pool.ntp.org 3.debian.pool.ntp.org

Puis utiliser la suite de commandes dans l'invité :
> sudo systemctl enable systemd-timesyncd.service

> sudo systemctl start systemd-timesyncd.service

> sudo systemctl restart systemd-timesyncd.service

On pourra ensuite utiliser la commande dans l'invité

> date

pour afficher la date. 