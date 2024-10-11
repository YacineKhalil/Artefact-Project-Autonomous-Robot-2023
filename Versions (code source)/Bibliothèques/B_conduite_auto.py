import cv2
import numpy as np
import cv2.aruco as aruco
# Tableau des coins = [supérieur gauche, supérieur droit, inférieur droit, inférieur gauche ]
# le (0,0) est en haut à gauche, le (max,max) est en bas à droite 

def distance(point1,point2):
    """distance euclidienne dans R2"""
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


def hauteur_rectangle(points):
    """points est une liste de points (4 points)
    prendre la moyenne des deux côtés réduit les incertitudes"""
    d_droit = distance(points[1],points[2])
    d_gauche = distance(points[3],points[0])
    return (d_droit+d_gauche)/2

def largeur_rectangle(points):
    """points est une liste de points (4 points)
    prendre la moyenne des deux côtés réduit les incertitudes"""
    d_haut = distance(points[0],points[1])
    d_bas = distance(points[2],points[3])
    return (d_haut+d_bas)/2


def hauteur_pixels(tab):
    points = tab[1:]
    return hauteur_rectangle(points)

a = 6096.14102686       #calculé grâce à une régression : voir wiki

def f(x):
    """x la hauteur en pixels du marqueur sur l'image
    f(x) la distance en cm entre caméra et marqueur"""
    return a/x


def distance_reelle(tab):
    """renvoie la distance en cm entre caméra et marqueur"""
    return f(hauteur_pixels(tab))
    
 # pour avoir la distance réelle faire :    f(distance_cap(capture()))


def theta(tab):
    """renvoie l'angle (radians) entre la normale au marqueur et la 
    droite passant par le centre du marqueur et le centre de la caméra"""
    d=distance_reelle(tab)
    points = tab[1:]
    K=(d*largeur_rectangle(points))/a
    K=min(1,K)          #on peut parfois avoir K=1.003 ce qui produit un bug
    return np.arccos(K)

def capture(cap):
    # Créez un dictionnaire ArUco
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000)

    # Créez un paramètre de détection
    parameters = aruco.DetectorParameters_create()

    # Initialiser la capture vidéo à partir de la caméra (0 pour la caméra par défaut)
    

    # Lire une image de la caméra
    ret, frame = cap.read()
    if not ret:
        return ()  # Arrêter la boucle si la capture échoue ou si l'utilisateur appuie sur une touche
    
    # Détecter les marqueurs dans l'image
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    if ids is not None:
        # Dessiner les marqueurs détectés sur l'image
        #frame_with_markers = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        Ltot=[]
        for i in range(len(ids)):
            L=[]
            L.append(ids[i][0])
            #print(str(ids[i][0]))
            for k in range(4):
                #print(str(corners[i][0][k]))
                L.append(corners[i][0][k])
            Ltot.append(L)
        return Ltot
    else:
        return ()         
            
    
    # Afficher l'image avec ou sans marqueurs
    #cv2.imshow('Image avec marqueurs', frame_with_markers if ids is not None else frame)
    
    
    # Attendre une petite période et vérifier si l'utilisateur appuie sur la touche "q" pour quitter
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #return()
    # Libérer la capture vidéo et détruire les fenêtres OpenCV
    cap.release()
    cv2.destroyAllWindows()

