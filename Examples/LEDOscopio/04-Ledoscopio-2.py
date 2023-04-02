#!/usr/bin/env python3
 
#-- Cadenas para dibujar las lineas superiores e inferiores de un bit
#-- de la señal
#-- Hay 4 casos que dependen del bit actual y del siguiente
BIT_LINE = {

    #-- Linea superior
    "superior" : [
        '   ', #-- 0: Caso "00"
        '  ┌', #-- 1: Caso "01"
        '──┐', #-- 2: Caso "10"
        '───'  #-- 3: Caso "11"
    ],

    #-- Linea inferior
    "inferior": [
        '───', #-- 0: Caso "00"
        '──┘', #-- 1: Caso "01"
        '  └', #-- 2: Caso "10"
        '   ', #-- 3: Caso "11"
    ]
}

def print_wave(cadbin : str) -> None:
    """Imprimir la señal asociada a la cadena de bits"""

    #-- Duplicar el último bit (hay 9 bits)
    cadbin += cadbin[-1]

    #-- Cadena superior
    cadT = ""

    #-- Cadena inferior
    cadB = ""

    #-- Recorrer todos los bits para calcular las cadenas
    #-- superior e inferior
    #-- (hay 8 bits de datos a representar)
    for i in range(8):

        #-- Convertir el bit actual y el siguiente en un numero entero
        num = int(cadbin[i] + cadbin[i+1], 2)

        #-- Añadir las cadenas del bit actual
        cadT += BIT_LINE["superior"][num]
        cadB += BIT_LINE["inferior"][num]

    #-- Imprimir la señal
    print (cadT) #-- Parte superior
    print (cadB) #-- Parte inferior


#───────────────────────────────────────
# MAIN
#───────────────────────────────────────
while True:

    try:
        #-- Pedir byte al usuario
        print()
        num = int(input("Introduce byte (0-255): "))

    #-- Si se pulsa Ctrl-C --> Terminar
    except KeyboardInterrupt:
        print()
        print("Fin")
        break

    #-- Pasar el numero a una cadena binaria de 8 bits
    cadbin = f"{num:08b}"

    #-- Imprimir la señal
    print()
    print(" 0  1  2  3  4  5  6  7")

    print_wave(cadbin)

    
