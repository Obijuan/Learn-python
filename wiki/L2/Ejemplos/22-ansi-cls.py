#!/usr/bin/env python3

# --------- Codigos ANSI
# -- Llevar el cursor a la posicion (1,1)
HOME = "\x1b[H"

# -- Borrar la pantalla
CLEAR = "\x1b[2J"

# -- CLS: Borrar la pantalla y llevar cursor a home
CLS = CLEAR + HOME

# ------------------
# -- MAIN
# ------------------

# -- Borrar la pantalla
print(CLS, end='', flush=True)

# -- Impresion de prueba
print("🙂")
