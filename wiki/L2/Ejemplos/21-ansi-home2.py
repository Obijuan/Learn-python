#!/usr/bin/env python3

# --------- Codigos ANSI
# -- Llevar el cursor a la posicion (1,1)
HOME = "\x1b[H"

# -- Imprimir en la posicion actual actual del cursor
print()
print("HOLA......")

# -- Cursor a Home
print(HOME, end='', flush=True)

# -- Imprimir mensaje en origen de la pantalla
print("🙂")
