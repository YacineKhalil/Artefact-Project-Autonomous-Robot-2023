import cv2
import time
import instructions_conduite_auto as c_auto
import conduite_manuelle as c_manu
import B_lecture_bibli as lect
import pygame 


#PARTIE CONTROLE DE L'ENCEINTE#

# Adresse MAC de l'enceinte : 00:12:3D:00:2D:86

N=10   #on va utliser un filtre glissant pour avoir l'impression que le bruit du moteur ne saccade pas

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("bruit_moteur.wav")
sound.set_volume(0)
sound.play(-1)
P_moteur_liste=[0]*N    #N valeurs précédentes : on va faire un lisseur
P_sortie_audio=0

################################

T = True

while T:

    etat = lect.read('/home/pi/artefact/teame/Versions/Epreuve_intermédaire/Communication/x_y_R_isAuto.txt')     # syntaxe requise pour etat: float,float,float,bool

    if etat=="bug communication":
        print(etat)


    else:
        P_new=c_manu.conduite_manuelle(etat)    #applique les tensions au moteur et affecte la valeur de puissance fournie aux moteurs à P_new
        P_moteur_liste.append(P_new)
        print(etat)

        P_last=P_moteur_liste.pop(0)
        P_sortie_audio=P_sortie_audio+(P_new-P_last)/N      #équivalent à faire sum(P_moteur_liste)/len(P_moteur_liste) mais économise des calculs
        sound.set_volume(P_sortie_audio + 0.05)      #+0.05 pour ne jamais avoir un moteur totalement silencieux
        time.sleep(0.1)
