# Caméra

### Notre caméra

Caméra HD 720p USB avec module OV9726

### Marqueurs ArUco

Les marqueurs ArUco sont des marqueurs semblables aux QR Code. Il existe différentes bibliothèques d'ArUco, dans lesquelles chaque ArUco est associé à un identifiant distinct.

Les marqueurs utilisés pour l'évalutation sont des ArUco au standard 6 × 6, imprimés sur du papier blanc (5cm × 5cm).

### Détection des ArUco

**Important** : Le module utilisé pour détecter les marqueurs est OpenCV (version python). Nous avons remarqué que les marqueurs imprimés avec une large bordure blanche sont bien mieux détectés que ceux découpés sans bordure. 
Cela peut peut-être s'expliquer par le fait que l'algorithme est entraîné sur des images où les QR Code/ArUco sont souvent entourés d'une large bordure blanche (penser à un QR Code que l'on scanne habituellement au milieu de l'écran).
La caméra doit être correctement règlée afin de pouvoir détecter les ArUco correctement.