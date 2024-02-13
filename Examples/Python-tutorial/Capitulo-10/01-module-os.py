#!/usr/bin/env python3

import os

#-- Imprimir el directorio actual
print(f"Directorio actual: {os.getcwd()}")

#-- Subir de directorio
os.chdir("..")

#-- Imprimir el directorio actual
print(f"Directorio actual: {os.getcwd()}")

#-- Ejecutar un comando en la consola
ret = os.system('echo "hola"')

#-- Resultado
#-- Si ret es 0, todo ha ido bien...
if ret==0:
  print("OK!!")

#-- Ejecutamos un comando incorrecto
ret = os.system('fakeee')
if ret!=0:
  print("ERROR!!!!!")


