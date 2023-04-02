#!/usr/bin/env python3

while True:

    try:
        #-- Pedir byte al usuario
        print()
        num = int(input("Introduce byte (0-255): "))


        #-- Pasar el numero a una cadena binaria de 8 bits
        cadbin = f"{num:08b}"

        #-- Sustituir el bit 0 por otro caracter
        cad = cadbin.replace('0','___').replace('1','▐█▌')

        #-- Imprimir
        print()
        print(" 0  1  2  3  4  5  6  7")
        print(cad)

    except KeyboardInterrupt:
        print()
        print("Fin")
        break


