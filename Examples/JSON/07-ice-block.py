#!/usr/bin/env python3

from Icestudio import BlockInfo, Ice

#-- Leer circuito
top = Ice("02-info-1.ice")

#-- Imprimir información
print(top)

block = BlockInfo()
print(block)

