#!/usr/bin/env python3


#-- Imprimir los numeros de fibonacci hasta el número n
def fibo(n: int) -> list:
    """Lista con los numeros de fibonacci hasta el numero n"""
    a,b = 0,1

    #- Lista donde almacenar la lista de fibonacci
    result = []

    while b < n:
        #-- Añadir elemento a la lista
        result.append(b)
        
        #-- Actualizar termino de fibonacci
        a,b = b, a+b

    #-- Devolver la lista
    return result


#-- Llamar a la funcion
l=fibo(100)
print("Lista de fibonacci: ", l)


