#!/usr/bin/env python3
# ──────────────────────────────────────────────────────
# ── Pruebas del modulo CURSES
# ── Ejemplo de borrado de la pantalla
# ──────────────────────────────────────────────────────
import curses
import time

# ────── Constantes para determinar la visibilidad del cursor
ON = 2
OFF = 0
# ── Tiempo a esperar
# ── En segundos
WAIT = 3

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

# ── Imprimir lineas de asteriscos
stdscr.addstr(5, 0, "*" * 30, col_verde)
stdscr.addstr("\n" + ("*" * 30), col_verde)
stdscr.addstr("\n" + ("*" * 30), col_verde)
stdscr.addstr("\n" + ("*" * 30), col_verde)
stdscr.addstr("\n" + ("*" * 30), col_verde)
stdscr.refresh()
time.sleep(WAIT)

# ── Borrar la pantalla
stdscr.clear()

# ── Esperar a que el usuario apriete una tecla
stdscr.addstr(12, 0, "\nPulsa una tecla", col_verde)
stdscr.getch()

# ── Volver a enseñar el cursor antes de terminar
curses.curs_set(ON)

# ── Terminar. Volver a la pantalla original del terminal
curses.endwin()
