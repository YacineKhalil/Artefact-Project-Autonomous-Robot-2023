import cv2

# Charger une image au format PNG
image = cv2.imread('aruco1.png')

# Créez un dictionnaire ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)

# Créez un paramètre de détection
parameters = cv2.aruco.DetectorParameters()

# Détecter les marqueurs ArUco
corners, ids, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

if ids is not None:
    # Dessiner les marqueurs détectés
    image_with_markers = cv2.aruco.drawDetectedMarkers(image, corners, ids)

    # Décoder les identifiants des marqueurs
    for i in range(len(ids)):
        print(f"Marqueur ArUco {ids[i][0]} détecté")

    # Afficher l'image avec les marqueurs
    cv2.imshow('ArUco Detection', image_with_markers)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Aucun marqueur ArUco détecté.")






