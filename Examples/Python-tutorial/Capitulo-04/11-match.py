#!/usr/bin/env python3

print("1.- Opcion 1")
print("2.- Opcion 2")
print("3.- Terminar")

while True:
    op = int(input("Elige opcion: "))

    match(op):
        case 1: 
            print("Opción 1")
        case 2:
            print("Opción 2")
        case 3:
            print("Terminar")
            break
        case _:
            print("Opción inválida")

