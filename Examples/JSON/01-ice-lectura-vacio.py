#!/usr/bin/env python3

import json

#-- Fichero .ice a leer
ICE_FILE = "01-vacio.ice"

#-- Constantes asociadas a las propiedades del .ice
VERSION = "version"
DESIGN = "design"
BOARD = "board"

#-- Leer circuito. Accesible desde el objeto "top"
with open(ICE_FILE) as f:
    top = json.load(f)

#-- Imprimir información
print(f"Version: {top[VERSION]}")
print(f"Placa: {top[DESIGN][BOARD]}")
