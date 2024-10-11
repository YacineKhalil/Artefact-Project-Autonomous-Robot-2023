# Code source

Le code source du robot est écrit exclusivement à l'aide de Python. Le code source se divise en trois partie :

- Une bibliothèque de fonctions utiles à la fois pour la conduite manuelle et pour la conduite automatique (et donc pour l'épreuve intermédiaire et pour l'épreuve finale)

- Le code source pour l'épreuve intermédiaire

- Le code source pour l'épreuve finale, qui réutilise la logique du code précédent, avec ajout de communication par websockets et d'opérations asynchrones (dans le cadre de la communication avec les autres robots)