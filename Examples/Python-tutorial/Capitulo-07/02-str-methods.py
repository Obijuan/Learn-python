#!/usr/bin/env python3

cad = "Hola"

#-- Justifiacion a la derecha
print("*" + cad.rjust(10) + "*")

#-- Justificación a la izquierda
print("*" + cad.ljust(10) + "*")

#-- Centrar texto
print("*" + cad.center(10) + "*")

#--- Cadena numerica
numcad = "576"

#--- Campo numero de 5 digitos, rellenado con ceros a la izquierda
print("*" + numcad.zfill(5) + "*")



