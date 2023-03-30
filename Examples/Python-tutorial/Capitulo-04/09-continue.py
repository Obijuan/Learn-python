#!/usr/bin/env python3

#-- Catalogar los números del 2 al 10
#-- entre pares e impares
for n in range(2,10):

    #-- Divisible entre 2: par
    if n % 2 == 0:
        print(n, "es par")

        #-- Pasar a la siguiente iteración
        continue

    #-- Es impar
    print(n, "es Impar")
