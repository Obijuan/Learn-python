# ──────────────────────────────────────────────────────
# ── Pruebas del color del primer plano
# ──────────────────────────────────────────────────────
import colorama as col

print()

# ── Impresión en diferentes colores
print("══════════════════════════════")
print(f"{col.Fore.BLACK}[BLACK] Mensaje de prueba")
print(f"{col.Fore.LIGHTBLACK_EX}[LIGHTBLACK_EX] Mensaje de prueba")

print(f"{col.Fore.RED}[RED] Mensaje de prueba")
print(f"{col.Fore.LIGHTRED_EX}[LIGHTRED_EX] Mensaje de prueba")

print(f"{col.Fore.GREEN}[GREEN] Mensaje de prueba")
print(f"{col.Fore.LIGHTGREEN_EX}[LIGHTGREEN_EX] Mensaje de prueba")

print(f"{col.Fore.YELLOW}[YELLOW] Mensaje de prueba")
print(f"{col.Fore.LIGHTYELLOW_EX}[LIGHTYELLOW_EX] Mensaje de prueba")

print(f"{col.Fore.BLUE}[BLUE] Mensaje de prueba")
print(f"{col.Fore.LIGHTBLUE_EX}[LIGHTBLUE_EX] Mensaje de prueba")

print(f"{col.Fore.MAGENTA}[MAGENTA] Mensaje de prueba")
print(f"{col.Fore.LIGHTMAGENTA_EX}[LIGHTMAGENTA_EX] Mensaje de prueba")

print(f"{col.Fore.CYAN}[CYAN] Mensaje de prueba")
print(f"{col.Fore.LIGHTCYAN_EX}[LIGHTCYAN_EX] Mensaje de prueba")

print(f"{col.Fore.WHITE}[WHITE] Mensaje de prueba")
print(f"{col.Fore.LIGHTWHITE_EX}[LIGHTWHITE_EX] Mensaje de prueba")

# ── Establecer colores por defecto
print(col.Style.RESET_ALL, end="")
print("──────────────────────────────")
print()
