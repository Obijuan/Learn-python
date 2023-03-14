#!/usr/bin/env python3

#-- Crear una coleccion simple
users = {
    "Obijuan": "activo",
    "Dark vader": "inactivo",
    "Yoda": "activo",
    "luke skywalker": "inactivo"
}

#-- Eliminar los usuarios inactivos

#-- Estrategia 1: Iterar sobre una copia, 
#-- borrar de la colección original
#-- users.copy() es una copia
for user, estado in users.copy().items():
    if estado == "inactivo":
        del users[user]

print(users)

#-- Estrategia 2: Crear una lista nueva
user_activos = {}
for user, estado in users.items():
    if estado == "activo":
        user_activos[user] = estado

print(user_activos)