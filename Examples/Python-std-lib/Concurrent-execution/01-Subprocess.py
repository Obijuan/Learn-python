#!/usr/bin/env python3

import subprocess

#-- Ejecutar "ls -l". La salida no se captura
result1 = subprocess.run(["ls", "-l"]) 

print(f"{result1.args=}")
print(f"{result1.returncode=}")
print(f"{result1.stdout=}")
print()

#-- Ejecutar "ls -l". Capturando la salida
result2 = subprocess.run(["ls", "-l"], capture_output=True)
print(f"{result2.args=}")
print(f"{result2.returncode=}")
print(f"{result2.stdout=}")
print()

#-- Esto tambien captura la salida
result3 = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
print(f"{result3.args=}")
print(f"{result3.returncode=}")
print(f"{result3.stdout=}")
print(result3)

