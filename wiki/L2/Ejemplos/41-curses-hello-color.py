#!/usr/bin/env python3
import curses

# ────── Inicializacion
stdscr = curses.initscr()

# ── Inicializar los colores
curses.start_color()

# ── Definir el color '1' mediante su tinta y fondo
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)

# ── Imprimir un mensaje con el color definido ('1')
stdscr.addstr("Holi...", curses.color_pair(1))

# ── Esperar a que el usuario apriete una tecla
stdscr.getch()

# ── Terminar. Volver a la pantalla original del terminal
curses.endwin()
