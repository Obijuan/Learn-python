#!/usr/bin/env python3

# -- Imprimir en la posicion actual actual del cursor
print()
print("HOLA......")

# -- Cursor a Home
print("\x1b[H", end='', flush=True)

# -- Imprimir mensaje en origen de la pantalla
print("🙂")
