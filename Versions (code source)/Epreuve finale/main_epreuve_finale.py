import B_fonctions_calibrage as mvmt
import B_module_moteur as m
import B_conduite_auto as ia
import B_recentrer_mvmt_bibli as R
import B_recentre_bibli as C
import protocol as pr
import fonctions_communes as fc
import cv2
import cv2.aruco as aruco
import websockets
import time
import asyncio


ordre = [3,5,1]
cap = cv2.VideoCapture(0) #on ouvre la vidéo dès le début

#cap.set(cv2.CAP_PROP_FPS,30.0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
#cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc('M','J','P','G'))

async def run():
    alpha = 0
    # ETAPES POUR TOUTES LES VOITURES (sauf la première):*
    #   - Ouvrir la connexion
    ws = await pr.open_connection(12)
    balises = await pr.get_ordre_balise(ws)
    position = [balises[str(b)] for b in ordre]
    print('balises',balises)

    #   - Attendre le go
    print("On attend de pouvoir partir")
    while not await pr.can_go(ws,0,0):
        print("on attend de pouvoir partir")
        time.sleep(0.5)

    #   - Aller au milieu
    print("On avance au milieu")
    mvmt.avancer(2.5) #avancer de 2.5m

    #   - Chercher notre balise grace a l'information donnée
    print("On s'oriente vers la première balise")
    mvmt.angle(-45*position[0]) # dans notre convention angle > 0 = sens trigo (tourner gauche)

    #       - Si problème de balise non trouvée chercher normalement
    #   - Aller à la balise
    
    await pr.send_signal(ws,1,ordre[0])
    # avancer de x metre
    print("On part vers la première balise")
    R.avance_vers_aruco(ordre[0],cap) #aller vers balise ordre [0]

    #   - Envoyer un signal quand on est arrivé
    await pr.send_signal(ws,2,ordre[0])

    aurco = C.multi_cap(20,cap,ordre[0])
    #if aruco == ():
    #    alpha = 0
    #else:
    #    corners = [aruco[1],aruco[2],aruco[3],aruco[4]]
    #    alpha = pr.estimation_angle_aruco(corners)

    #   - Calculer l'angle avec un decalage pour arriver en face
    angle = fc.angle_ij(position[0], position[1], 0.3,alpha)    
    # On peut prendre en compte le fait qu'on connait l'angle d'arrivé donc ne pas se placer a 0.3m (y a la fontion sur le git)
    print("On s'oriente vers la deuxième balise")
    mvmt.angle(-angle)

    #   - Attendre le go
    while not await pr.can_go(ws,2,ordre[0]):
        print("On attend de pouvoir partir")
        time.sleep(0.5)
        
    #   - Aller à la balise
    await pr.send_signal(ws,3,ordre[0])
    print("On part vers la deuxième balise")
    mvmt.avancer(0.5) # on avance de 1m
    R.avance_vers_aruco(ordre[1],cap) #aller vers balise ordre [1]

    #   - Envoyer un signal quand on est arrivé
    await pr.send_signal(ws, 4, ordre[1])

    aurco = C.multi_cap(20,cap,ordre[1])
    #if aruco == ():
    #    alpha = 0 
    #else:
    #    corners = [aruco[1],aruco[2],aruco[3],aruco[4]]
    #    alpha = pr.estimation_angle_aruco(corners)

    #   - Calculer l'angle avec un decalage pour arriver en face
    angle = fc.angle_ij(position[1], position[2], 0.3,alpha)
    print("On s'oriente vers la troisième balise")
    mvmt.angle(-angle)

    #   - Attendre le go
    while not await pr.can_go(ws,4,ordre[1]):
        print("On attend de pouvoir partir")
        time.sleep(0.5)

    #   - Aller à la balise
    await pr.send_signal(ws, 5, ordre[1])
    print("On part vers la troisième balise")
    mvmt.avancer(0.5) # on avance de 1m
    R.avance_vers_aruco(ordre[2],cap) #aller vers balise ordre [2]

    #   - Envoyer un signal quand on est arrivé
    await pr.send_signal(ws, 6, ordre[2])

    aurco = C.multi_cap(20,cap,ordre[2])
    #if aruco == ():
    #    alpha = 0
    #else:
    #    corners = [aruco[1],aruco[2],aruco[3],aruco[4]]
    #    alpha = pr.estimation_angle_aruco(corners)

    #   - S'orienter vers l'arrivée
    angle = fc.angle_ij(position[2], -3.5, 0.3,alpha)  # -3.5 c'est la position 9
    print("On s'oriente vers l'arrivé*")
    mvmt.angle(-angle)

    #   - Attendre le go
    while not await pr.can_go(ws,6,ordre[2]):
        print("On attend de pouvoir partir")
        time.sleep(0.5)

    #   - Aller à l'arrivé
    await pr.send_signal(ws, 7, ordre[1])
    print("On part vers l'arrivé")
    R.avance_vers_aruco(9,cap)

    #   - Envoyer un signal quand on est arrivé
    await pr.send_signal(ws, 8, 9)
    print("On est arrivé à la fin.")


    #   - Se décaler pour laisser les autres voitures passer
    mvmt.angle(45)
    mvmt.avancer(1)

    # POUR TOUTES LES VOITURES ENVOYER DES SIGNAUX DE VIES

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run())
