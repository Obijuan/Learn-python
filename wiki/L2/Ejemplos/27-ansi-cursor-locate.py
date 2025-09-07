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

# ── Ocultar el cursor
CURSOR_OFF = ESC + '[?25l'

# ── Mostrar el cursor
CURSOR_ON = ESC + '[?25h'

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

# -- Ocultar el cursor
print(CURSOR_OFF)

# ── Borrar pantalla
print(CLS, end='', flush=True)

# ── Cambiar color a VERDE
print(GREEN)

# ── Tiempo a esperar tras imprimir cada punto
# ── En segundos
WAIT = 1

time.sleep(WAIT)

# ──────────── Imprimir 4 puntos en la pantalla

# ── Ir a la primera posicion (x=15, y=8)
# ── Primero se escribe la fila, luego la columna
print(ESC + '[8;15f', end='', flush=True)

# ── Imprimir primer punto
print('●')
time.sleep(WAIT)

# ── Ir a la segunda posicion (x=12, y=9)
print(ESC + '[9;12f', end='', flush=True)

# ── Imprimir segundo punto
print('●')
time.sleep(WAIT)

# ── Ir a la tercera posicion (x=15, y=9)
print(ESC + '[9;18f', end='', flush=True)

# ── Imprimir tercer punto
print('●')
time.sleep(WAIT)

# ── Ir a la cuarta posicion (x=15, y=9)
print(ESC + '[10;15f', end='', flush=True)

# ── Imprimir cuarto punto
print('●')
time.sleep(WAIT)

# ── Establecer atributos iniciales
print(DEFAULT)

# ── Enseñar el cursor antes de terminar
print(CURSOR_ON)
