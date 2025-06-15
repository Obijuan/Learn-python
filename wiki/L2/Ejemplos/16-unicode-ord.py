#!/usr/bin/env python3

# -- Caracteres
car1 = 'A'
car2 = 'Ñ'
car3 = '░'
car4 = '🙂'

# -- Calcular su código unicode
cod1 = ord(car1)
cod2 = ord(car2)
cod3 = ord(car3)
cod4 = ord(car4)

print("\nCodigos UNICODE")
print(f"• {car1} ➜ U+{cod1:X}")
print(f"• {car2} ➜ U+{cod2:X}")
print(f"• {car3} ➜ U+{cod3:X}")
print(f"• {car4} ➜ U+{cod4:X}")
print()
