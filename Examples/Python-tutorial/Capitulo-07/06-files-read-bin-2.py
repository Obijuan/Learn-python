#!/usr/bin/env python3

FICHERO = "test1.bin"

#-- Ejemplo de apertura de un fichero binario
#-- para lectura
with open(FICHERO, "rb") as f:
    data = f.read()

#-- Pasar los bytes a cadenas de numeros hexadecimales
data_hex = [f"{byte:02x}" for byte in data]

print()
print(f"CONTENIDO FICHERO {FICHERO}:")
print(f"Tamaño: {len(data)} bytes")
print("──────────────────────")
print(" ".join(data_hex))
print("──────────────────────")


