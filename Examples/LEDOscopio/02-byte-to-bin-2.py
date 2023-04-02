#!/usr/bin/env python3

while True:

    try:
        #-- Pedir byte al usuario
        num = int(input("Introduce byte (0-255): "))


        #-- Pasar el numero a una cadena binaria de 8 bits
        cadbin = f"{num:08b}"

        #-- Sustituir el bit 0 por otro caracter
        cad = cadbin.replace('0','_').replace('1','▉')
        print(cad)

    except KeyboardInterrupt:
        print()
        print("Fin")
        break


