#!/usr/bin/env python3
# ──────────────────────────────────────────────────────
# ── Pruebas del modulo CURSES
# ── Ejemplo de ocultar/mostrar el cursor
# ──────────────────────────────────────────────────────
import curses
import time

# ────── Inicializacion
stdscr = curses.initscr()

# ── Inicializar los colores
curses.start_color()

# ── Definir el color '1' mediante su tinta y fondo
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

# ── Variable con el identificador del par a usar
color_texto = curses.color_pair(1)

# ── Enseñar el cursor
curses.curs_set(2)

# ── Imprimir un mensaje con el color definido ('1')
stdscr.addstr('El cursor está visible: ', color_texto)

# ── Hay que referescar la pantalla para que se imprima
# ── el texto
stdscr.refresh()
time.sleep(3)

# ── Ocultar el cursor
curses.curs_set(0)
stdscr.addstr('\nEl cursor está oculto: ', color_texto)
stdscr.refresh()
time.sleep(3)

# ── Volver a enseñar el cursor antes de terminar
curses.curs_set(2)

# ── Terminar. Volver a la pantalla original del terminal
curses.endwin()
