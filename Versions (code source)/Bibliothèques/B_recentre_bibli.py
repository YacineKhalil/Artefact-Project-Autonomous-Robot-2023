import B_module_moteur as m
import B_conduite_auto as ia
import cv2
import cv2.aruco as aruco
import time

vitesse_rotation = 50
x_centre_camera = 320

def no(aruco): #numéro aruco
    L=[]
    for i in range(len(aruco)):
        L.append(aruco[i][0])
    return L 



def multi_cap (nb_capture,cap,no_voulu):
    """
    Entree : nb_capture : int
    cap : camera
    parite_voulue : int

    Sortie: renvoie l'aruco captée si la caméra le capte et qu'il a la bonne parité sinon ()
    """
    for k in range (nb_capture):
        aruco = ia.capture(cap)
        if (aruco != ()) and (no_voulu in no(aruco)):
            for i in range(len(aruco)):
                if aruco[i][0] == no_voulu:
                    return aruco[i]

    return ()

def decalage (aruco):
    sup_g = aruco[1]
    sup_d = aruco[2]
    inf_d = aruco[3]
    inf_g = aruco[4]    
    x_centre_aruco = (sup_g[0] + sup_d[0] + inf_d[0] + inf_g[0])/4

    return(x_centre_aruco - x_centre_camera)

def tourner_a_gauche (vitesse_rotation) : 
    m.Motor.MotorRun(0,"reculer",vitesse_rotation)
    m.Motor.MotorRun(1,"avancer",vitesse_rotation) 

def tourner_a_droite (vitesse_rotation) : 
    m.Motor.MotorRun(1,"reculer",vitesse_rotation)
    m.Motor.MotorRun(0,"avancer",vitesse_rotation) 

def recentrer(facteur_tolerance,cap,no_voulu,deja_vu):
    temps_pivot = 0.1
    x_de_tolerance = x_centre_camera * facteur_tolerance
    instant_perte = 0
    print("debut fonction")
    while True:
        print("deja_vu",deja_vu)
        print("instant_perte",instant_perte)
        m.Motor.MotorStop(0)
        m.Motor.MotorStop(1)
        aruco = multi_cap(15,cap,no_voulu)
        if aruco == () :
            print("pas de aruco")
            temps_pivot = 0.1
            if not deja_vu :
                tourner_a_droite(vitesse_rotation)
            elif instant_perte % 10 >= 5:
                tourner_a_droite(vitesse_rotation)
                instant_perte+=1
            else : 
                tourner_a_gauche(vitesse_rotation)
                instant_perte+=1
            if instant_perte > 15 : 
                deja_vu = False
                print("tour")
            time.sleep(temps_pivot)
        else:
            deja_vu = True
            if instant_perte% 10 >= 5 : 
                instant_perte = 5
            else:
                instant_perte = 0
            temps_pivot = temps_pivot/3
            distance_au_capteur = ia.distance_reelle(aruco)
            print("distance au aruco:",distance_au_capteur)
            if abs(decalage(aruco)) < x_de_tolerance:
                print("decalage final:",decalage(aruco))
                return(aruco,deja_vu)
            elif decalage(aruco) > 0:
                #print("decalage droit:",decalage(aruco))
                tourner_a_droite(vitesse_rotation)
                time.sleep(temps_pivot)
            else: 
                #print("decalage gauche:",decalage(aruco))
                tourner_a_gauche(vitesse_rotation)
                time.sleep(temps_pivot)
            