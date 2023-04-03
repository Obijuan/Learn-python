#!/usr/bin/env python3

import json

FICHERO1 =  "list.json"

#-- Leer directamente el fichero json
with open(FICHERO1, encoding='utf-8') as f:
    lista = json.load(f)

#-- Sabemos que el objeto es una lista...
#-- la iteramos e imprimimos su contenido
for e in lista:
    print(e)

