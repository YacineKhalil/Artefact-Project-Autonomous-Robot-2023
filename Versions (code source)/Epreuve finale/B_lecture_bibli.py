def read(fichier): # fichier en string et mettre .txt 
    f = open(fichier,"r")
    ligne = f.read()
    f.close()
    ligne = ligne.split(',')
    if ligne == [""]:
        return "bug communication"
    else:
        L = [float(i) for i in ligne[:3]]
        if ligne[3]=="true":    #conduite automatique
            L.append(True)
        else:                   #conduite manuelle
            L.append(False)
        return L