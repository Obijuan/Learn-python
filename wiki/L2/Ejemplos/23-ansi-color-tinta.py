#!/usr/bin/env python3

# ───────────────────────────────────────
#            CODIGOS ANSI
# ───────────────────────────────────────

# ── Llevar el cursor a la posicion (1,1)
HOME = "\x1b[H"

# ── Borrar la pantalla
CLEAR = "\x1b[2J"

# ── CLS: Borrar la pantalla y llevar cursor a home
CLS = CLEAR + HOME

# ─────────── COLORES ───────────
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

# ──── Otros caracteres especiales
# ── Volver al color por defecto
DEFAULT = "\x1B[0m"


# ──────────────────────
# MAIN
# ──────────────────────
# ── Borrar pantalla
print(CLS, end='', flush=True)

# ── Imprimir mensajes en diferentes colores
print(GREY + "Mensaje en Gris")
print(LGRAY + "Mensaje en gris claro")

print(RED + "Mensaje en color rojo")
print(LRED + "Mensaje en Rojo claro")

print(GREEN + "Mensaje en color verde")
print(LGREEN + "Mensaje en color verde claro")

print(YELLOW + "Mensaje en color amarillo")
print(LYELLOW + "Mensaje en color amarillo claro")

print(BLUE + "Mensaje en azul")
print(LBLUE + "Mensaje en azul claro")

print(MAGENTA + "Mensaje en magenta")
print(LMAGENTA + "Mensaje en magenta claro")

print(CYAN + "Mensaje en Cyan")
print(LCYAN + "Mensaje en Cyan claro")

print(WHITE + "Mensaje en blanco")
print(LWHITE + "Mensaje en blanco claro")


# ── Imprimir mensaje normal
print(DEFAULT + "Este es un mensaje normal...")
print()
