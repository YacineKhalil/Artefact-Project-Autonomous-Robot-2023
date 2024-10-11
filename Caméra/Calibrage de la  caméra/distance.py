import numpy as np
# Tableau des coins = [supérieur gauche, supérieur droit, inférieur droit, inférieur gauche ]
# le (0,0) est en haut à gauche, le (max,max) est en bas à droite 

def distance(point1,point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def determine_distance (sommets_Aruco): 
    d_droit = distance(points[1],points[2])
    d_gauche = distance(points[3],points[0])
    return (d_droit+d_gauche)/2

a = 6217.1948758

def d(x): 
    """ x:hauteur (en pixels) de l'Aruco sur l'image prise par la caméra 
        -> d:distance réelle (en cm) entre la caméra et l'Aruco """
    return a/x
    
 # pour avoir la distance réelle faire :    f(distance_cap(capture()))