# ──────────────────────────────────────────────────────
# ── Pruebas de posicionamiento del cursor
# ──────────────────────────────────────────────────────
import time
import ansi
from colorama import Fore, Style, Cursor


# ── Ocultar el cursor
print(ansi.CURSOR_OFF)

# ── Borrar pantalla
print(ansi.CLS, end='', flush=True)

# ── Cambiar color a VERDE
print(Fore.GREEN)

# ── Tiempo a esperar tras imprimir cada punto
# ── En segundos
WAIT = 1
time.sleep(WAIT)

# ──────────── Imprimir 4 puntos en la pantalla
print(Cursor.POS(x=15, y=8), end='', flush=True)
print('●')
time.sleep(WAIT)

print(Cursor.POS(x=12, y=9), end='', flush=True)
print('●')
time.sleep(WAIT)

print(Cursor.POS(x=18, y=9), end='', flush=True)
print('●')
time.sleep(WAIT)

print(Cursor.POS(x=15, y=10), end='', flush=True)
print('●')
time.sleep(WAIT)

# ── Establecer colores por defecto
print(Style.RESET_ALL, end='')

# ── Enseñar el cursor antes de terminar
print(ansi.CURSOR_ON)

print("──────────────────────────────")
print()
