# !/usr/bin/env python
import numpy as np
"""
Module permettant d'utiliser la conduite manuelle.
"""
v_max=100

def Arg(x,y):
    if y==0:
        if x==0:
            return 0        
        if x<0:
            return np.pi
    return 2*np.arctan(y/(x+np.sqrt(x**2+y**2)))

def calcul_r0(x,y,R):
    pi=np.pi

    theta=Arg(x,y)

    v=v_max*np.sqrt(x**2+y**2)/R
    v=min(v,v_max)                 
    v=int(v)                       

    if 0<=theta<=pi/2:
        return [0,"avancer",v]

    if pi/2<=theta<=pi:
        return [0,"avancer",v*((pi-theta)/(pi/2))]

    if -pi<=theta<=-pi/2:
        return [0,"reculer",abs(v*(-(pi+theta)/(pi/2)))]

    return [0,"reculer",v]                      

def calcul_r1(x,y,R):
    pi=np.pi

    theta=Arg(x,y)

    v=int(min(v_max*np.sqrt(x**2+y**2)/R,v_max)) 

    if 0<=theta<=pi/2:
        return [1,"avancer",v*(theta/(pi/2))]

    if pi/2<=theta<=pi:
        return [1,"avancer",v]

    if -pi<=theta<=-pi/2:
        return [0,"reculer",v]

    return [1,"reculer",abs(v*(theta/(pi/2)))]



