#!/usr/bin/env python3

#- Lista de puntos cartesianos
puntos = [(0,0), (0,3), (5,0), (7,9), (-3,5)]

#-- Recorrer todos los puntos
for p in puntos:

    #-- Imprimr el tipo de punto
    match(p):
        case (0,0): 
            print("* Origen")
        case (0,x):
            print("* Sobre eje X")
        case (y,0):
            print("* Sobre eje Y")
        case (x,y):
            print("* Punto (",x,y,")")

