import cv2
import cv2.aruco as aruco
import numpy as np 
# Tableau des coins = [supérieur gauche, supérieur droit, inférieur droit, inférieur gauche ]
# le (0,0) est en haut à gauche, le (max,max) est en bas à droite 

#cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture(0)

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
              
        for i in range(len(ids)):
            L=[]
            L.append(ids[i][0])
            #print(str(ids[i][0]))
            for k in range(4):
                #print(str(corners[i][0][k]))
                L.append(corners[i][0][k])
            return L
    else:
        return () 
    
def distance(point1,point2):
    """distance euclidienne dans R2"""
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def hauteur_rectangle(points):
    """points est une liste de points (4 points)
    prendre la moyenne des deux côtés réduit les incertitudes"""
    d_droit = distance(points[1],points[2])
    d_gauche = distance(points[3],points[0])
    return (d_droit+d_gauche)/2
    
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
            
for i in range(10**3):
    test = capture(cap)
    if test != (): 
        print(distance_reelle(test))
    else:
        print("pas détecté")

    
