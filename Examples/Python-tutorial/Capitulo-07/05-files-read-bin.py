#!/usr/bin/env python3

FICHERO = "test1.bin"

#-- Ejemplo de apertura de un fichero binario
#-- para lectura
with open(FICHERO, "rb") as f:
    data = f.read()


print()
print(f"CONTENIDO FICHERO {FICHERO}:")
print(f"Tamaño: {len(data)} bytes")
print("──────────────────────")
print(data)
print("──────────────────────")


