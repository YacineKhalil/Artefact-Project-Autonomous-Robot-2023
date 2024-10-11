#!/usr/bin/env python3

def stocke_donnees(x_y,R,isAuto):
    x_y=x_y.replace("(", "").replace(")", "").replace(" ", "")          #(x, -y) -> x,-y
    donnees_formatees=x_y+","+R+","+isAuto
    fichier=open("x_y_R_isAuto.txt",'w')
    fichier.write(donnees_formatees)
    fichier.close()
    return