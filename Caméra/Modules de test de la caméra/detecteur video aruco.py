import cv2
# Tableau des coins = [supérieur gauche, supérieur droit, inférieur droit, inférieur gauche ]
# le (0,0) est en haut à gauche, le (max,max) est en bas à droite 

# Créez un dictionnaire ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)

# Créez un paramètre de détection
parameters = cv2.aruco.DetectorParameters()

# Initialiser la capture vidéo à partir de la caméra (0 pour la caméra par défaut)
cap = cv2.VideoCapture(0)

while True:
    # Lire une image de la caméra
    ret, frame = cap.read()
    fichier_coordonnee = open("fichier_coordonnees.txt","w")
    if not ret:
        break  # Arrêter la boucle si la capture échoue ou si l'utilisateur appuie sur une touche
    
    # Détecter les marqueurs dans l'image
    corners, ids, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    if ids is not None:
        # Dessiner les marqueurs détectés sur l'image
        frame_with_markers = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        for i in range(len(ids)):
            print(str(ids[i][0]))
            fichier_coordonnee.write(str(ids[i][0]) + ',')
            for k in range(4):
                fichier_coordonnee.write(str(corners[i][0][k][0]) + ',' + str(corners[i][0][k][1]) +',')
                print(str(corners[i][0][k]))
            
    else:
        fichier_coordonnee.write("False") #Si aucun aruco n'est détécté, on continue le mouvement précédent
    fichier_coordonnee.close()
            
            
    
    # Afficher l'image avec ou sans marqueurs
    cv2.imshow('Image avec marqueurs', frame_with_markers if ids is not None else frame)
    
    
    # Attendre une petite période et vérifier si l'utilisateur appuie sur la touche "q" pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et détruire les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()