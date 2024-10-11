import B_module_vitesse as v
import B_module_moteur as m
import time



def controle_r0(etat):
    if len(etat) ==4:
        V = v.calcul_r0(etat[0],etat[1],etat[2])
        m.Motor.MotorRun(V[0],V[1],V[2])
        #print(V[0],V[1],V[2])
        return V[2]
    else:
        m.Motor.MotorStop(1)
        m.Motor.MotorStop(0)
        return 0

def controle_r1(etat):
    if len(etat) == 4:
        V = v.calcul_r1(etat[0],etat[1],etat[2])
        m.Motor.MotorRun(V[0],V[1],V[2])
        #print(V[0],V[1],V[2])
        return V[2]
    else:
        m.Motor.MotorStop(1)
        m.Motor.MotorStop(0)
        return 0


def conduite_manuelle(etat) : 
    v0=controle_r0(etat)
    v1=controle_r1(etat)
    return max(v0,v1)/100      #normalisation à 1