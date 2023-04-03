#!/usr/bin/env python3

FICHERO = "file2.txt"

#-- Ejemplo de apertura de un fichero de texto
#-- para escritura
with open("file2.txt", "w", encoding="utf-8") as f:
    f.write("Fichero de texto creado\n")
    f.write("Linea 1....\n")
    f.write("Linea 2...\n")
    f.write("Linea 3...\n")

print(f"Fichero {FICHERO} creado")
