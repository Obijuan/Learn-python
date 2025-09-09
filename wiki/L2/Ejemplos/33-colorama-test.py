# ──────────────────────────────────────────────────────
# ── Imprimir mensajes en colores
# ── usando el modulo colorama
# ──────────────────────────────────────────────────────
import colorama

print("══════════════════════════════")
print("Mensaje con atributos normales")
print(f"{colorama.Fore.RED}Mensaje en rojo")
print(f"{colorama.Fore.GREEN}Mensaje en verde")

# ── Establecer colores por defecto
print(colorama.Style.RESET_ALL, end="")
print("──────────────────────────────")
