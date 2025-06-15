#!/usr/bin/env python3

# -- Código UNICODE
cod1 = 0x41
cod2 = 0xD1
cod3 = 0x2591
cod4 = 0x1F642

# -- Obtener una cadena con el carácter correspondinete
# -- a ese punto de código unicode
str1 = chr(cod1)
str2 = chr(cod2)
str3 = chr(cod3)
str4 = chr(cod4)

print("\nCodigos UNICODE")
print(f"• U+{cod1:X} ➜ {str1}")
print(f"• U+{cod2:X} ➜ {str2}")
print(f"• U+{cod3:X} ➜ {str3}")
print(f"• U+{cod4:X} ➜ {str4}")
print()
