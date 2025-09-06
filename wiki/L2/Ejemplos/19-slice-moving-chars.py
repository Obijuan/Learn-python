#!/usr/bin/env python3
import time

# -- Definir cadenas para hacer pruebas
cad = "    HOLA"

# -- Imprimir primer tramo
i = 0
print(cad[i:i+4], end='', flush=True)

# -- Pausa
time.sleep(1)

# -- Imprimir segundo tramo
i = 1
print('\b' * 4 + cad[i:i+4], end='', flush=True)

# -- Pausa
time.sleep(1)

# -- Imprimir tercer tramo
i = 2
print('\b' * 4 + cad[i:i+4], end='', flush=True)

# -- Pausa
time.sleep(1)

# -- Imprimir cuarto tramo
i = 3
print('\b' * 4 + cad[i:i+4], end='', flush=True)

# -- Pausa
time.sleep(1)

# -- Imprimir quinto tramo
i = 4
print('\b' * 4 + cad[i:i+4], end='', flush=True)

# -- Pausa
time.sleep(1)

print()
