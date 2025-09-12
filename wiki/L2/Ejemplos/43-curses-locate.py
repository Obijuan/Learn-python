#!/usr/bin/env python3
# ──────────────────────────────────────────────────────
# ── Pruebas del modulo CURSES
# ── Ejemplo de posicionamiento del cursor
# ──────────────────────────────────────────────────────
import curses
import time

# ────── Constantes para determinar la visibilidad del cursor
ON = 2
OFF = 0
# ── Tiempo a esperar tras imprimir cada punto
# ── En segundos
WAIT = 1

# ────── Inicializacion
stdscr = curses.initscr()

# ── Inicializar los colores
curses.start_color()

# ── Definir el color '1' mediante su tinta y fondo
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

# ── Variable con el identificador del par a usar
col_verde = curses.color_pair(1)

# ── Ocultar el cursor
curses.curs_set(OFF)

# ──────────── Imprimir 4 puntos en la pantalla

# ── Punto 1
stdscr.addstr(8, 15, '●', col_verde)
stdscr.refresh()
time.sleep(WAIT)

# ── Punto 2
stdscr.addstr(9, 12, '●', col_verde)
stdscr.refresh()
time.sleep(WAIT)

# ── Punto 3
stdscr.addstr(9, 18, '●', col_verde)
stdscr.refresh()
time.sleep(WAIT)

# ── Punto 4
stdscr.addstr(10, 15, '●', col_verde)
stdscr.refresh()
time.sleep(WAIT)

# ── Esperar a que el usuario apriete una tecla
stdscr.addstr(12, 1, "\nPulsa una tecla", col_verde)
stdscr.getch()

# ── Volver a enseñar el cursor antes de terminar
curses.curs_set(ON)

# ── Terminar. Volver a la pantalla original del terminal
curses.endwin()
