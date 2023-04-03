#!/usr/bin/env python3

import json

#-- Constantes asociadas a las propiedades del .ice
VERSION = "version"
PACKAGE = "package"
DESIGN = "design"
DEPENDENCIES = "dependencies"
BOARD = "board"
GRAPH = "graph"
BLOCKS = "blocks"
WIRES = "wires"
ID = "id"
TYPE = "type"
SIZE = "size"

class Ice:
   
    def __init__(self, file: str=None) -> None:
        """Crear un objeto circuito a partir de un fichero .ice"""

        if file:
            #-- Leer el archivo .ice
            with open(file) as f:
                self._top = json.load(f)
        else:
            self._top = {
                "version": "1.2",
                "package": {
                    "name": "",
                    "version": "",
                    "description": "",
                    "author": "",
                    "image": ""
                },
                "design": {
                    "board": "alhambra-ii",
                    "graph": {
                        "blocks": [],
                        "wires": []
                    }
                },
                "dependencies": {}
            }

    @property
    def version(self):
        return self._top[VERSION]
    
    @property
    def package(self):
        return self._top[PACKAGE]
    
    @property
    def design(self):
        return self._top[DESIGN]
    
    @property
    def dependencies(self):
        return self._top[DEPENDENCIES]
    
    def __str__(self):

        cad = ""
        cad += f"Version: {ice.version}\n"
        cad += f"Placa: {ice.design[BOARD]}\n"
        cad += f"Cables: {len(ice.design[GRAPH][WIRES])}\n"
        cad += f"Bloques: {len(ice.design[GRAPH][BLOCKS])}\n"
        cad += f" * Tamaño: {ice.design[GRAPH][BLOCKS][0][SIZE]}\n"
        return cad


#-- Leer circuito
ice = Ice("02-info-1.ice")

#-- Imprimir información
print(ice)



