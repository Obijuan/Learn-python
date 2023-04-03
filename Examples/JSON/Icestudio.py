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
DATA = "data"
POSITION = "position"


class Size:
    """Tamaño de los bloques de icestudio"""

    def __init__(self, width=0, height=0) -> None:
        """Crear un objeto Size"""
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


class Ice:
    """Working with Icestudio circuits"""
   
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

        block = BlockInfo(**self.design[GRAPH][BLOCKS][0])

        cad = ""
        cad += f"Version: {self.version}\n"
        cad += f"Placa: {self.design[BOARD]}\n"
        cad += f"Cables: {len(self.design[GRAPH][WIRES])}\n"
        cad += f"Bloques: {len(self.design[GRAPH][BLOCKS])}\n"
        cad += f" * id: {block.id}\n"
        cad += f" * type: {block.type}\n"
        cad += f" * data: {block.data}\n"
        cad += f" * position: {block.position}\n"
        cad += f" * Size: {block.size}\n"
        return cad

    def obj(self):
        return self._top


class BlockInfo:

    def __init__(self, 
                 id="", 
                 type="basic.info",
                 data={
                    "info": "",
                    "readonly": False
                 },
                 position={
                    "x": 0,
                    "y": 0
                 },
                 size=Size(0,0)) -> None:
            
        self.id = id
        self.type = type
        self.data = data
        self.position = position
        self.size = size
        

    def __str__(self):
        cad = ""
        cad += f"  * Id: {self.id}\n"
        cad += f"  * Tipo: {self.type}\n"
        cad += f"  * Data: {self.data}\n"
        cad += f"  * position: {self.position}\n"
        cad += f"  * size: {self.size}\n"
        return cad


