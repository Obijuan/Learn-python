# ──────────────────────────────────────────────────────
# ── Pruebas del color del fondo
# ──────────────────────────────────────────────────────
import colorama as col

print()

# ── Impresión en diferentes colores
print("══════════════════════════════")
print(f"{col.Back.BLACK}[BLACK] Mensaje de prueba")
print(f"{col.Back.LIGHTBLACK_EX}[LIGHTBLACK_EX] Mensaje de prueba")

print(f"{col.Back.RED}[RED] Mensaje de prueba")
print(f"{col.Back.LIGHTRED_EX}[LIGHTRED_EX] Mensaje de prueba")

print(f"{col.Back.GREEN}[GREEN] Mensaje de prueba")
print(f"{col.Back.LIGHTGREEN_EX}[LIGHTGREEN_EX] Mensaje de prueba")

print(f"{col.Back.YELLOW}[YELLOW] Mensaje de prueba")
print(f"{col.Back.LIGHTYELLOW_EX}[LIGHTYELLOW_EX] Mensaje de prueba")

print(f"{col.Back.BLUE}[BLUE] Mensaje de prueba")
print(f"{col.Back.LIGHTBLUE_EX}[LIGHTBLUE_EX] Mensaje de prueba")

print(f"{col.Back.MAGENTA}[MAGENTA] Mensaje de prueba")
print(f"{col.Back.LIGHTMAGENTA_EX}[LIGHTMAGENTA_EX] Mensaje de prueba")

print(f"{col.Back.CYAN}[CYAN] Mensaje de prueba")
print(f"{col.Back.LIGHTCYAN_EX}[LIGHTCYAN_EX] Mensaje de prueba")

print(f"{col.Back.WHITE}[WHITE] Mensaje de prueba")
print(f"{col.Back.LIGHTWHITE_EX}[LIGHTWHITE_EX] Mensaje de prueba")

# ── Establecer colores por defecto
print(col.Style.RESET_ALL, end="")
print("──────────────────────────────")
print()
