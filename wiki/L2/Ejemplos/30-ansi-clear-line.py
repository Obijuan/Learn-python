#!/usr/bin/env python3
import time

# ───────────────────────────────────────
#            CODIGOS ANSI
# ───────────────────────────────────────

# ── Secuencia de ESCAPE
ESC = '\x1b'

# ── Llevar el cursor a la posicion (1,1)
HOME = ESC + '[H'

# ── Borrar la pantalla
CLEAR = ESC + '[2J'

# ── CLS: Borrar la pantalla y llevar cursor a home
CLS = CLEAR + HOME

# ── Borrar linea: Desde el cursor a la derecha
CLEAR_LINE_RIGHT = ESC + '[0K'

# ── Borrar linea: Desde el cursor a la izquierda
CLEAR_LINE_LEFT = ESC + '[1K'

# ── Borrar linea completa
CLEAR_LINE = ESC + '[2K'

# ── Ocultar el cursor
CURSOR_OFF = ESC + '[?25l'

# ── Mostrar el cursor
CURSOR_ON = ESC + '[?25h'

# ── Guardar la posicion del cursor
CURSOR_SAVE = ESC + '[s'

# ── Guardar la posicion del cursor
CURSOR_RESTORE = ESC + '[u'


# ─────────── COLORES DE LA TINTA ───────────
# ── Colores normales
GREY = ESC + '[30m'
RED = ESC + '[31m'
GREEN = ESC + '[32m'
YELLOW = ESC + '[33m'
BLUE = ESC + '[34m'
MAGENTA = ESC + '[35m'
CYAN = ESC + '[36m'
WHITE = ESC + '[37m'

# ── Colores brillantes
LGRAY = ESC + '[90m'
LRED = ESC + '[91m'
LGREEN = ESC + '[92m'
LYELLOW = ESC + '[93m'
LBLUE = ESC + '[94m'
LMAGENTA = ESC + '[95m'
LCYAN = ESC + '[96m'
LWHITE = ESC + '[97m'

# ─────────── COLORES DEL FONDO ───────────
BACK_BLACK = ESC + '[40m'
BACK_RED = ESC + '[41m'
BACK_GREEN = ESC + '[42m'
BACK_YELLOW = ESC + '[43m'
BACK_BLUE = ESC + '[44m'
BACK_MAGENTA = ESC + '[45m'
BACK_CYAN = ESC + '[46m'
BACK_WHITE = ESC + '[47m'


# ──── Otros caracteres especiales
# ── Volver al color por defecto
DEFAULT = ESC + '[0m'


# ──────────────────────
# MAIN
# ──────────────────────

# ── Tiempo a esperar tras cada operacion de borrado
# ── En segundos
WAIT = 1

# ── Borrar pantalla
print(CLS, end='', flush=True)

print("Esta es una linea de texto")
print("Esta es una linea de texto")
print("Esta es una linea de texto")

# ── Posicionar cursor en mitad de la primera linea
print(ESC + '[1;13f', end='', flush=True)

time.sleep(WAIT)

# ── Borrar desde el cursor hacia la derecha
print(CLEAR_LINE_RIGHT, end='', flush=True)
time.sleep(WAIT)

# ── Bajar el cursor a la siguiente linea
print(ESC + '[1B', end='', flush=True)
time.sleep(WAIT)

# ── Borrar desde el cursor hacia la izquierda
print(CLEAR_LINE_LEFT, end='', flush=True)
time.sleep(WAIT)

# ── Bajar el cursor a la siguiente linea
print(ESC + '[1B', end='', flush=True)
time.sleep(WAIT)

# ── Borrar la línea completa
print(CLEAR_LINE, end='', flush=True)
time.sleep(WAIT)

print()
