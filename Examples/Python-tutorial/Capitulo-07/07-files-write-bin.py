#!/usr/bin/env python3

FICHERO = "test2.bin"


#-- Cadena con los bytes a escribir
bytes = b"\x00\x01\x02\x03\xFF"

#-- Ejemplo de escritura de un fichero binario
with open(FICHERO, "wb") as f:
   f.write(bytes)

print(f"Fichero {FICHERO} creado")


