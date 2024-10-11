# Code source pour l'épreuve finale

L'épreuve finale consiste en un parcours complexe et simultané de cinq robots. Chaque robot se repère grâce à des ArUco.

[Modalités de l'épreuve finale](https://discourse.r2.enst.fr/t/seance-evaluation-finale/381/3)

## Fonctions de la bibiliothèque

Tous les fichiers commençant par 'B_" font partie d'une bibliothèque commune aux épreuves finale et intermédiaire. Leur fonctionnement est détaillé dans le dossier Bibliothèques.

## Fonctions de notre groupe

Les fichiers fonctions_communes.py et protocol.py ont été développés par le groupe entier et permettent de mettre en oeuvre notre stratégie et la communication entre robots par laquelle elle passe. Des éléments de documentation sont présents sur le dépôt commun :

[Dépôt de groupe](https://gitlab.telecom-paris.fr/proj103/2324/gr3/depot-groupe)

## main_epreuve_finale.py

**Le script main_epreuve_finale.py est lancé en ssh lorsque le robot qui agit comme serveur a lancé ce dernier.**

On utilise la bibliothèque asyncio afin de réaliser des opérations asynchrones (attente d'informations de la part du robot serveur).

On réutilise aussi les fonctions développées pour l'épreuve intermédiaire (voir le fichier associé)