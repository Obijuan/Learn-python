#!/usr/bin/env python3

#───────────────────────────────────────
# Definiciones ANSI para el cursor
#───────────────────────────────────────

#──── Almacenar la posicion actual del cursor
CURSOR_PUSH = "\x1B[s"

#──── Recuperar la posicion del cursor previamente guardada
CURSOR_POP = "\x1B[u"

#──── Ocultar el cursor
CURSOR_HIDE = "\x1B[?25l"

#──── Mostrar el cursor
CURSOR_SHOW = "\x1B[?25h"

#───────────────────────────────────────
# MAIN
#───────────────────────────────────────

print(CURSOR_HIDE, end='', flush=True)

#── Guardar la posicion del cursor
print(CURSOR_PUSH, end='', flush=True)

#-- Imprimir mensaje en primer linea
print("HolaHola")

try:
  while True:

    #-- Recuperar la posicion del cursor
    print(CURSOR_POP, end='', flush=True)

    #-- Escribir puntos encima, para borrar los caracteres anteriores
    print("...")

except KeyboardInterrupt:
  ##- Volver a hacer el cursor visible
  print(CURSOR_SHOW)
