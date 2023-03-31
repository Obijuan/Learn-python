#!/usr/bin/env python3

#-- Funcion con parámetros clave pasados a través de un diccionario
def debug(**args):
    print("LLamada")
    print("  Diccionario: ", args)
    print("  Argumentos pasados: ", len(args))

    # #-- Imprimir todos los argumetnos pasados
    for arg in args:
         print("   ", arg, "---> ", args[arg])
    print()


#-- Llamar a la función con diferentes parámetros
debug()
debug(a1=1, a2=2)
debug(a=1, b="hola", c="vamos")

