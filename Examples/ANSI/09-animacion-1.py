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

def print_frame(frame):
   """Print a frame on the console
   """
   #-- Print the frame, line by line
   for line in frame:
      print(line)


#──── The sprite is composed of frames
SPRITE = [
   [ 
    "● ",  #-- Frame 0
    "  "
   ],
   [
    " ●",  #-- Frame 1
    "  "
   ],
   [
   "  ",   #-- Frame 2
   " ●"
   ],
   [
   "  ",   #-- Frame 3
   "● "
   ]
]


#───────────────────────────────────────
# MAIN
#───────────────────────────────────────

#-- Frame period, in seconds
WAIT = 0.2

#-- Ocultar cursor
print(CURSOR_HIDE, end='', flush=True)

#── Guardar la posicion del cursor
print(CURSOR_PUSH, end='', flush=True)

try:

   #-- La animación se repite hasta que se pulse Ctrl-C
   while True:

      #-- Imprimir todos los frames, uno tras otro
      for frame in SPRITE:
         print(CURSOR_POP, end='', flush=True)
         print_frame(frame)

         time.sleep(WAIT)

#── Se ha pulsado Ctrl-C: Terminar
except KeyboardInterrupt:
   print()
   print()

   ##- Volver a hacer el cursor visible
   print(CURSOR_SHOW)

