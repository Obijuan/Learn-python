#!/usr/bin/env python3

# ── Hacer accesible el fichero ansi.py
import ansi

# ── Borrar pantalla
print(ansi.CLS, end='', flush=True)

# ── Imprimir mensaje en color verde
print(ansi.GREEN + "Probando el modulo ansy.py...")
print()

# ── Establecer colores por defecto
print(ansi.DEFAULT, end='', flush=True)
