#!/usr/bin/env python3

num = 35
cad = "Hola"

#-- Imprimir las variables
print(f"Variable num: {num}, Variable cad: {cad}")

#-- Establecer una anchura máxima
print(f"Variable num: {num:10}, Variable cad: {cad:10}---")

#-- Mostrar el valor para depuración
print(f"Debug: {num=}, {cad=}")

#-- Imprimir numeros en base diferente
print(f"Num: Decial: {num:d}, Hexa: {num:x}, Binario: {num:b}----")

#-- Establecer tamaño maximo para numeros
print(f"Num: Decial: {num:5d}, Hexa: {num:4x}, Binario: {num:8b}----")

#-- Rellenar con 0s la izquierda
print(f"Num: Decial: {num:05d}, Hexa: {num:04x}, Binario: {num:08b}----")

