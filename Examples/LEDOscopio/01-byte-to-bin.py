#!/usr/bin/env python3

while True:

    try:
        #-- Pedir byte al usuario
        num = int(input("Introduce byte (0-255): "))

        #-- Imprimir en binario
        print(f"{num:08b}")

    except KeyboardInterrupt:
        print()
        print("Fin")
        break


