#!/usr/bin/env python3

#-- Calcular la divisibilidad de los numeros entre 2 y 10
for n in range(2, 10):

    #-- Dividir n entro todos los numeros inferiores a n
    for x in range(2, n):

        #-- Numero divisible
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break

    #-- No es divisible
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')