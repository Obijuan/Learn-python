#!/usr/bin/env python3
# ──────────────────────────────────────────────────────
# ── Mini barra de progreso
# ── Código original
# ──────────────────────────────────────────────────────
import time
import ansi


# ─────────────────────────────────────────────────────────────────
# ── Funcion que realiza un paso del progreso actual
# ── El paso consiste en imprimir un asterisco y esperar un segundo
# ──────────────────────────────────────────────────────────────────
def paso():
    # ── Imprimir un carácter átomo de la barra
    print(f'{ansi.BLUE}█{ansi.DEFAULT}', end='', flush=True)

    # ── Pausa
    time.sleep(1)


# ─────────────────────────────────────────────────────────────────
# ── PROGRAMA PRINCIPAL
# ── MAIN
# ─────────────────────────────────────────────────────────────────
# ── Inicializar la pantalla
print(ansi.CLS, end='', flush=True)
print(ansi.CURSOR_OFF, end='', flush=True)

# ── Mensaje inicial
print("Barra de progreso:")
time.sleep(1)

# ── Dar 4 pasos en el progreso
paso()
paso()
paso()
paso()

print()

# ── Llevar la pantalla al estado inicial
print(ansi.CURSOR_ON)
