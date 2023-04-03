#!/usr/bin/env python3

#-- Ejemplo de apertura de un fichero de texto
#-- para su lectura
with open("file1.txt", encoding="utf-8") as f:
    text = f.read()

print()
print("CONTENIDO DEL FICHERO:")
print("──────────────────────")
print(text)
print("──────────────────────")
