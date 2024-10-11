import B_module_moteur as m
import time
    

"""
fonctions de deplacement de base
"""
#roues defectueuses rapport de 1.06 mis au point le 20/12/2023 piles charges a 100% 
#attention à ce que les roues ne touchent pas le cadre. 
def avancer(d):
    if d>0:
        vitesse_réelle = 0.38
        vitesse_avancement = 50
        rapport_roue_0_1 = 0.95
        m.Motor.MotorRun(0,"avancer",vitesse_avancement*rapport_roue_0_1)
        m.Motor.MotorRun(1,"avancer",vitesse_avancement) 
        time.sleep(d/vitesse_réelle)
    else:
        d=-d
        vitesse_réelle = 0.38
        vitesse_avancement = 50
        rapport_roue_0_1 = 0.95
        m.Motor.MotorRun(0,"reculer",vitesse_avancement*rapport_roue_0_1)
        m.Motor.MotorRun(1,"reculer",vitesse_avancement) 
        time.sleep(d/vitesse_réelle)

    m.Motor.MotorStop(1)
    m.Motor.MotorStop(0)

# après test, 0.38 m/s
#avancer(1)

#Expérimentation faite dans le hall. 
def angle(theta):
    if theta >0: # angle positif = sens trigo
        vitesse_avancement = 60
        vitesse_rotation = 208
        m.Motor.MotorRun(1,"avancer",vitesse_avancement) 
        m.Motor.MotorRun(0,"reculer",vitesse_avancement)
        time.sleep(theta/vitesse_rotation)
    else:
        theta = -theta
        vitesse_avancement = 60
        vitesse_rotation = 208
        m.Motor.MotorRun(0,"avancer",vitesse_avancement) 
        m.Motor.MotorRun(1,"reculer",vitesse_avancement)
        time.sleep(theta/vitesse_rotation)
    m.Motor.MotorStop(1)
    m.Motor.MotorStop(0)

#vitesse_rotation = 208 deg/S

def avancer_angle(d,theta):
    angle(theta)
    avancer(d)

def carre():
    for i in range(4):
        avancer_angle(1,90)

