# ──────────────────────────────────────────────────────
# ── Pruebas de from ... import
# ──────────────────────────────────────────────────────
from colorama import Fore, Back, Style

print()

# ── Impresión en diferentes colores
print("══════════════════════════════")
print(f"{Fore.GREEN}[GREEN] Mensaje de prueba")
print(f"{Back.GREEN}[GREEN] Mensaje de prueba")

# ── Establecer colores por defecto
print(Style.RESET_ALL, end='')
print("──────────────────────────────")
print()
