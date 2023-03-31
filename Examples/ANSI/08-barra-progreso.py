#!/usr/bin/env python3

import time

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

#-- Ocultar cursor
print(CURSOR_HIDE, end='', flush=True)

#── Guardar la posicion del cursor
print(CURSOR_PUSH, end='', flush=True)

#-- Imprimir plantilla barra de progreso
print("░" * 10)


print(CURSOR_POP, end='', flush=True)

for i in range(0,10):
   print("█", end='', flush=True)
   time.sleep(0.1)

##- Volver a hacer el cursor visible
print(CURSOR_SHOW)
