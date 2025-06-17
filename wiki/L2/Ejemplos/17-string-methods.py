#!/usr/bin/env python3

# -- Definir cadenas para hacer pruebas
cad1 = "hola"
cad2 = "HOLA"
cad3 = "   Hola   "
cad4 = "hola mundo"
cad5 = "meta-circuito"

# -- Probar los métodos y mostrar los resultados
# -- en la consola
print()
print(f"'{cad1}'.upper() = '{cad1.upper()}'")
print(f"'{cad2}'.lower() = '{cad2.lower()}'")
print(f"'{cad3}'.strip() = '{cad3.strip()}'")
print(f"'{cad1}'.startwith('ho') = {cad1.startswith('ho')}")
print(f"'{cad1}'.startwith('ca') = {cad1.startswith('ca')}")
print(f"'{cad1}'.endswith('la') = {cad1.endswith('la')}")
print(f"'{cad1}'.endswith('hi') = {cad1.endswith('hi')}")
print(f"'{cad4}'.split() = {cad4.split()}")
print(f"'{cad5}'.split() = {cad5.split()}")
print(f"'{cad5}'.split('-') = {cad5.split('-')}")
print(f"'*'.join(['uno', 'dos']) = {'*'.join(['uno', 'dos'])}")
print(f"'{cad4}'.replace('mundo', 'py') = '{cad4.replace('mundo', 'py')}'")
print(f"'{cad4}'.find('xx') = {cad4.find('xx')}")
print(f"'{cad4}'.find('mun') = {cad4.find('mun')}")
print()
