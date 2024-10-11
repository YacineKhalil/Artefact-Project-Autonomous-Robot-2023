import B_module_moteur as m
import B_conduite_auto as ia
import time
import B_recentre_bibli as R

#tps_avancement_cst = 0.1

def temps_avancement(distance_au_capteur):
    if distance_au_capteur < 40 : 
        return 0.03
    else:
        return 0.1

def vitesse_avancement(distance_au_capteur):
    if distance_au_capteur < 80:
        return 40
    else:
        return 80

def arret():
    m.Motor.MotorStop(1)
    m.Motor.MotorStop(0)

def avancer_tout_droit(vitesse_avancement):
    rapport_roue_0_1 = 0.995 #roues defectueuses
    m.Motor.MotorRun(0,"avancer",vitesse_avancement*rapport_roue_0_1)
    m.Motor.MotorRun(1,"avancer",vitesse_avancement) 

def reculer(vitesse):
    rapport_roue_0_1 = 0.995 #roues defectueuses
    m.Motor.MotorRun(0,"reculer",vitesse*rapport_roue_0_1)
    m.Motor.MotorRun(1,"reculer",vitesse) 

def avance_vers_aruco(no_voulu,cap):
    facteur_tolerance = 10/100
    deja_vu = False
    while True:
        aruco,deja_vu = R.recentrer(facteur_tolerance,cap,no_voulu,deja_vu)
        distance_au_capteur = ia.distance_reelle(aruco)
        print("distance au aruco:",distance_au_capteur)
        if distance_au_capteur <= 35: #il y a un taux d'erreur, on préfère dire que c'est 30cm mais mettre 35
            arret()
            print("Approche a moins de 30cm de l'aruco",no_voulu)
            break
        else:
            print("avance")
            avancer_tout_droit(vitesse_avancement(distance_au_capteur))
            time.sleep(temps_avancement(distance_au_capteur))