#!/usr/bin/env python3
# ──────────────────────────────────────────────────────
# ── Mini barra de progreso
# ── Código original
# ──────────────────────────────────────────────────────
import time
import ansi


# ── Inicializar la pantalla
print(ansi.CLS)
print(ansi.CURSOR_OFF)

print("Barra de progreso:")
time.sleep(1)

# ── Imprimir el caracter de la barra, en azul
print(f'{ansi.BLUE}█{ansi.DEFAULT}', end='', flush=True)

# ── Pausa
time.sleep(1)

# ── Lo mismo: Impresión + pausa
print(f'{ansi.BLUE}█{ansi.DEFAULT}', end='', flush=True)
time.sleep(1)

# ── Impresión + pausa
print(f'{ansi.BLUE}█{ansi.DEFAULT}', end='', flush=True)
time.sleep(1)

# ── Impresión + pausa
print(f'{ansi.BLUE}█{ansi.DEFAULT}', end='', flush=True)
time.sleep(1)

print()

# ── Llevar la pantalla al estado inicial
print(ansi.CURSOR_ON)
