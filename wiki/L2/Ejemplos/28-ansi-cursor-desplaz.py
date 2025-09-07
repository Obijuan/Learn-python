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

# ── Borrar pantalla
print(CLS, end='', flush=True)

# ── Cambiar color a AZUL
print(BLUE)

# ── Tiempo a esperar tras imprimir cada punto
# ── En segundos
WAIT = 1

time.sleep(WAIT)

# ──────────── Imprimir 5 puntos en la pantalla

# ── Ir a la primera posicion (x=12, y=6)
print(ESC + '[6;12f', end='', flush=True)

# ── Imprimir primer punto
print('●', end='', flush=True)
time.sleep(WAIT)

# ── Moverse hacia la derecha
print(ESC + '[5C', end='', flush=True)

# ── Imprimir segundo punto
print('●', end='', flush=True)
time.sleep(WAIT)

# ── Moverse hacia abajo
print(ESC + '[5B', end='', flush=True)

# ── Imprimir tercer punto
print('●', end='', flush=True)
time.sleep(WAIT)

# ── Moverse hacia la izquierda
print(ESC + '[8D', end='', flush=True)

# ── Imprimir cuarto punto
print('●', end='', flush=True)
time.sleep(WAIT)

# ── Moverse hacia arriba
print(ESC + '[2A', end='', flush=True)

# ── Imprimir quinto punto
print('●', end='', flush=True)
time.sleep(WAIT)

# ── Ir a la posicion final (x=1, y=14)
print(ESC + '[14;1f', end='', flush=True)

# ── Establecer atributos iniciales
print(DEFAULT)

# ── Enseñar el cursor antes de terminar
print(CURSOR_ON)
