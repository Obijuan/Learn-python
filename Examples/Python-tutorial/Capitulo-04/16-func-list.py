#!/usr/bin/env python3

#-- Funcion con parámetros variables (ninguno, uno, dos....)
def debug(*args):
    print("LLamada")
    print("  Tupla: ", args)
    print("  Argumentos pasados: ", len(args))

    #-- Imprimri todos los argumetnos pasados
    print("  ", end='')
    for arg in args:
        print(arg, end=' ')
    print()


#-- Llamar a la función con diferentes parámetros
debug()
debug(1)
debug(1,"hola")
debug(1,2,3,4)

