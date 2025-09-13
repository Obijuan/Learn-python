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
WAIT = 1

# ────── Inicializacion
stdscr = curses.initscr()

# ── Inicializar los colores
curses.start_color()

# ── Definir colores a usar
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_CYAN)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_WHITE)
curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

# ── Variable con el identificador del par a usar
col1 = curses.color_pair(1)
col2 = curses.color_pair(2)
col3 = curses.color_pair(3)
col4 = curses.color_pair(4)
col5 = curses.color_pair(5)
col6 = curses.color_pair(6)
col7 = curses.color_pair(7)
col8 = curses.color_pair(8)

# ── Ocultar el cursor
curses.curs_set(OFF)

# ── Cambiar color del fondo
stdscr.bkgd(col1)

# ── Imprimir mensaje
stdscr.addstr(5, 0, "Mensaje de prueba")
stdscr.refresh()
time.sleep(WAIT)

# ── Cambiar color del fondo
stdscr.bkgd(col2)
stdscr.refresh()
time.sleep(WAIT)

# ── Cambiar color del fondo
stdscr.bkgd(col3)
stdscr.refresh()
time.sleep(WAIT)

# ── Cambiar color del fondo
stdscr.bkgd(col4)
stdscr.refresh()
time.sleep(WAIT)

# ── Cambiar color del fondo
stdscr.bkgd(col5)
stdscr.refresh()
time.sleep(WAIT)

# ── Cambiar color del fondo
stdscr.bkgd(col6)
stdscr.refresh()
time.sleep(WAIT)

# ── Cambiar color del fondo
stdscr.bkgd(col7)
stdscr.refresh()
time.sleep(WAIT)

# ── Cambiar color del fondo
stdscr.bkgd(col8)
stdscr.refresh()
time.sleep(WAIT)

# ── Volver a enseñar el cursor antes de terminar
curses.curs_set(ON)

# ── Terminar. Volver a la pantalla original del terminal
curses.endwin()
