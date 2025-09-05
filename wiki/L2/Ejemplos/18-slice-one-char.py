#!/usr/bin/env python3
import time

# -- Definir cadenas para hacer pruebas
cad = "HOLA🙂"

# -- Imprimir el primer carácter
print(cad[0], end='', flush=True)

# -- Pausa
time.sleep(1)

# -- Imprimir segundo carácter, borrando el anterior
print(f'\b{cad[1]}', end='', flush=True)
time.sleep(1)

# -- Impresión tercer caracter
print(f'\b{cad[2]}', end='', flush=True)
time.sleep(1)

# -- Impresión cuarto caracter
print(f'\b{cad[3]}', end='', flush=True)
time.sleep(1)

# -- Imprimir el último carácter
print(f'\b{cad[4]}', end='', flush=True)
time.sleep(1)

print()
