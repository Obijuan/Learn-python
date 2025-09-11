#!/usr/bin/env python3
# ──────────────────────────────────────────────────────
# ── Pruebas del modulo CURSES
# ── Ejemplo HOLA-MUNDO
# ──────────────────────────────────────────────────────
import curses

# ── Crear una ventana nueva, encima del terminal actual
stdscr = curses.initscr()

# ── Imprimir un mensaje
stdscr.addstr("Holi...")

# ── Esperar a que el usuario apriete una tecla
stdscr.getch()

# ── Terminar. Volver a la pantalla original del terminal
curses.endwin()
