#!/usr/bin/env python3

#-- Crear un diccionario
notas = {
    "pepe" : 5,
    "john" : 10,
    "Vader": 8
}

#-- Recorrer diccionario obteniendo los
#-- pares clave/valor
for k,v in notas.items():
    print(k, v)

