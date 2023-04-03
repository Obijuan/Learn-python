#!/usr/bin/env python3

import json

#-- Fichero .ice a leer
ICE_FILE = "02-info-1.ice"

#-- Constantes asociadas a las propiedades del .ice
VERSION = "version"
DESIGN = "design"
BOARD = "board"
GRAPH = "graph"
BLOCKS = "blocks"
WIRES = "wires"

#-- Leer circuito. Accesible desde el objeto "top"
with open(ICE_FILE) as f:
    top = json.load(f)

#-- Obtener el grafo del circuito
grafo = top[DESIGN][GRAPH]

#-- Obtener la lista de bloques y cables
bloques = grafo[BLOCKS]
cables = grafo[WIRES]


num_blocks = len(bloques)
num_wires = len(cables)

#-- Imprimir información
print(f"Version: {top[VERSION]}")
print(f"Placa: {top[DESIGN][BOARD]}")
print(f"Cables: {num_wires}")
print(f"Bloques: {num_blocks}")

