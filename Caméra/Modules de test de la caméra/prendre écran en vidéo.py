import cv2

# Initialiser la capture vidéo à partir de la caméra (0 pour la caméra par défaut)
cap = cv2.VideoCapture(0)

while True:
    # Lire une image de la caméra
    ret, frame = cap.read()
    if not ret:
        break  # Arrêter la boucle si la capture échoue ou si l'utilisateur appuie sur une touche
    
    
    # Afficher l'image avec ou sans marqueurs
    cv2.imshow('Image avec marqueurs', frame)
    
    # Attendre une petite période et vérifier si l'utilisateur appuie sur la touche "q" pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et détruire les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()



    #if keyboard.is_pressed('q'):
     #   print("Touche 'q' appuyée. Arrêt de la boucle.")
      #  break
