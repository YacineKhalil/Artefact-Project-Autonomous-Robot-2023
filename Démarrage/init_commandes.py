#on veut repartir d'un fichier x_y_R_isAuto.txt toujours constant à chaque démarrage de la voiture
chemin_fichier="/home/pi/artefact/teame/Conduite finale/Démarrage init_commandes.py"
fichier = open(chemin_fichier,"w")
fichier.write("0,0,1,false")
fichier.close()
#ce fichier sera modifié par l'utilisateur dès qu'il se connecte au site de contrôle à distance
#il ne sera réinitialisé que si la voiture est éteinte puis rallumée