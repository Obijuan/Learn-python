#!/usr/bin/env python3

#-- Definiciones ANSI para los colores
NEGRO = "\x1B[30m"
RED = "\x1B[31m"  
GREEN = "\x1B[32m" 
YELLOW = "\x1B[33m"
BLUE = "\x1B[34m"
MAGENTA = "\x1B[35m"
CYAN = "\x1B[36m"
WHITE = "\x1B[37m"

#------ Otros caracteres especiales
#-- Volver al color por defecto
DEFAULT = "\x1B[0m"

#-- Imprimir mensajes en diferentes colores
print(NEGRO + "Mensaje en negro")
print(RED + "Mensaje en color rojo")
print(GREEN + "Mensaje en color verde")
print(YELLOW + "Mensaje en color amarillo")
print(BLUE + "Mensaje en azul")
print(MAGENTA + "Mensaje en magenta")
print(CYAN + "Mensaje en Cyan")
print(WHITE + "Mensaje en blanco")

#-- Imprimir mensaje normal
print(DEFAULT + "Este es un mensaje normal...")
