import B_recentrer_mvmt_bibli as R
import time 
import B_fonctions_calibrage as c 
import cv2
import time
import instructions_conduite_auto as c_auto
import conduite_manuelle as c_manu
import B_lecture_bibli as lect
import pygame 
import B_fonctions_calibrage as calibr


def conduite_auto(cap):
    R.avance_vers_aruco(1,cap) #aruco n°1
    R.reculer(100)
    time.sleep(1)
    R.arret()
    c.angle(-150)

    R.avance_vers_aruco(0,cap) #aruco n°0
    R.avance_vers_aruco(9,cap) #aruco n°1
    
    R.arret()

    


