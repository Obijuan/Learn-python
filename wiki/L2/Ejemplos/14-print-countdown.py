#!/usr/bin/env python3

import time

# -- Imprimir primer digito de la cuenta atrás
# -- Y retroceder el cursor una posición
print('3', end='', flush=True)

# -- Pausa
time.sleep(1)

# -- Imprimir segundo dígito de la cuenta atrás
print('\b2', end='', flush=True)
time.sleep(1)

# -- Impresión tercer dígito de la cuenta atrás
print('\b1', end='', flush=True)
time.sleep(1)

# -- Impresión + pausa
print('\b0', end='', flush=True)
time.sleep(1)

print()
