#!/usr/bin/env python3

import json

FICHERO1 =  "list.json"
FICHERO2 = "objeto.json"

#-- Ejemplo de lista
lista = ["holi", 2, 3, "vamos"]

#-- Ejemplo de diccionario (objeto)
objeto = {
    "nombre": "test",
    "id": 234
}

#-- Pasar a JSON
lista_json =  json.dumps(lista)
objeto_json = json.dumps(objeto)

#-- Imprimir sus correspondientes representaciones en JSON
print(lista_json)
print(objeto_json)

#-- Crear dos ficheros en JSON
with open(FICHERO1, "w", encoding="utf-8") as f:
    f.write(lista_json)

print(f"Creado fichero {FICHERO1}")

with open(FICHERO2, "w", encoding="utf-8") as f:
    f.write(objeto_json)

print(f"Creado fichero {FICHERO2}")






