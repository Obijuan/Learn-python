#!/usr/bin/env python3

#-- Definiciones ANSI para los colores
RED = "\x1B[91m"  

#------ Otros caracteres especiales
#-- Volver al color por defecto
DEFAULT = "\x1B[0m"

#-- Imprimir mensaje en Rojo
print(RED + "Mensaje en color rojo" + DEFAULT)

#-- Imprimir mensaje normal
print("Este es un mensaje normal...")
