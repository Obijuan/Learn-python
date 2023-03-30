#!/usr/bin/env python3


#-- Imprimir los numeros de fibonacci hasta el número n
def fibo(n: int):
    """Imprimir los numeros de fibonacci hasta el numero n"""
    a,b = 0,1

    while b < n:
        print(b, end=" ")
        a,b = b, a+b

#-- Llamar a la funcion
fibo(100)
print()


