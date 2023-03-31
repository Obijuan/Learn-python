#!/usr/bin/env python3

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#-- Codigo que se ejecuta al importar el modulo
print("--> Modulo Fibonacci")

if __name__ == '__main__':
    import sys
    print("Llamando a la función fib()...")
    fib(int(sys.argv[1]))
