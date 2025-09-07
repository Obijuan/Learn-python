#!/usr/bin/env python3
import time

# ───────────────────────────────────────
#            CODIGOS ANSI
# ───────────────────────────────────────

# ── Llevar el cursor a la posicion (1,1)
HOME = "\x1b[H"

# ── Borrar la pantalla
CLEAR = "\x1b[2J"

# ── CLS: Borrar la pantalla y llevar cursor a home
CLS = CLEAR + HOME

# ── Ocultar el cursor
CURSOR_OFF = "\x1b[?25l"

# ── Mostrar el cursor
CURSOR_ON = "\x1b[?25h"

# ─────────── COLORES DE LA TINTA ───────────
# ── Colores normales
GREY = "\x1B[30m"
RED = "\x1B[31m"
GREEN = "\x1B[32m"
YELLOW = "\x1B[33m"
BLUE = "\x1B[34m"
MAGENTA = "\x1B[35m"
CYAN = "\x1B[36m"
WHITE = "\x1B[37m"

# ── Colores brillantes
LGRAY = "\x1B[90m"
LRED = "\x1B[91m"
LGREEN = "\x1B[92m"
LYELLOW = "\x1B[93m"
LBLUE = "\x1B[94m"
LMAGENTA = "\x1B[95m"
LCYAN = "\x1B[96m"
LWHITE = "\x1B[97m"

# ─────────── COLORES DEL FONDO ───────────
BACK_BLACK = "\x1B[40m"
BACK_RED = "\x1B[41m"
BACK_GREEN = "\x1B[42m"
BACK_YELLOW = "\x1B[43m"
BACK_BLUE = "\x1B[44m"
BACK_MAGENTA = "\x1B[45m"
BACK_CYAN = "\x1B[46m"
BACK_WHITE = "\x1B[47m"


# ──── Otros caracteres especiales
# ── Volver al color por defecto
DEFAULT = "\x1B[0m"


# ──────────────────────
# MAIN
# ──────────────────────

# ── Borrar pantalla
print(CLS, end='', flush=True)

# ── Imprimir mensaje
print("El cursor está visible: ", end='', flush=True)
time.sleep(3)

# ── Ocultar el cursor
print(CURSOR_OFF)
print("El cursor está oculto...", end='', flush=True)
time.sleep(3)

# ── Enseñar el cursor antes de terminar
print(CURSOR_ON)
