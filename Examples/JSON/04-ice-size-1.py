#!/usr/bin/env python3

import json

#-- Constantes asociadas a las propiedades del .ice
VERSION = "version"
DESIGN = "design"
BOARD = "board"
GRAPH = "graph"
BLOCKS = "blocks"
WIRES = "wires"
ID = "id"
TYPE = "type"
SIZE = "size"

class Size:
    """Tamaño de los bloques de icestudio"""

    def __init__(self, width=0, height=0) -> None:
        """Crear un objeto Size a partir de numeros enteros"""
        self.width = width
        self.height = height

    def obj(self) -> dict:
        """Devolver el objeto (diccionario) que contiene los datos"""
        
        return {
            "width" : self.width,
            "height": self.height
        }
    
    def __str__(self):
        """Devolver la cadena imprimible"""

        return f'Size({self.width}, {self.height})'


#-- Fichero .ice a leer
ICE_FILE = "02-info-1.ice"

#-- Leer circuito. Accesible desde el objeto "top"
with open(ICE_FILE) as f:
    top = json.load(f)

#-- Obtener tamaño del primer bloque
size = Size(**top[DESIGN][GRAPH][BLOCKS][0][SIZE])
size2 = Size(0,0)

#-- Imprimir información
print(f"Version: {top[VERSION]}")
print(f"Placa: {top[DESIGN][BOARD]}")
print(f"Cables: {len(top[DESIGN][GRAPH][WIRES])}")
print(f"Bloques: {len(top[DESIGN][GRAPH][BLOCKS])}")
print(f"    * Tamaño: {size}")
print(f"    * Tamaño: {size2}")

