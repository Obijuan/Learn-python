#!/usr/bin/env python3

#───────────────────────────────────────
# Definiciones ANSI para el cursor
#───────────────────────────────────────

#──── Almacenar la posicion actual del cursor
CURSOR_PUSH = "\x1B[s"

#──── Recuperar la posicion del cursor previamente guardada
CURSOR_POP = "\033[u"

#───────────────────────────────────────
# MAIN
#───────────────────────────────────────
#── Nada más empezar se guarda la posicion del cursor
print(CURSOR_PUSH, end='', flush=True)

#-- Imprimir mensaje en primer linea
print("HolaHola")

#-- Recuperar la posicion del cursor
print(CURSOR_POP, end='', flush=True)

#-- Escribir puntos encima, para borrar los caracteres anteriores
print("...")


