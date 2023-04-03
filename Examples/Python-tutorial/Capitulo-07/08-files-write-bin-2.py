#!/usr/bin/env python3

FICHERO = "test2.bin"


#-- Cadena con los bytes a escribir
bytes = bytes([0x00, 0x01, 0x02, 0x03, 0xFF])

#-- Ejemplo de escritura de un fichero binario
with open(FICHERO, "wb") as f:
   f.write(bytes)

print(f"Fichero {FICHERO} creado")


