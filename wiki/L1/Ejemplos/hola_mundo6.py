# ──────────────────────────────────────────────────────
# ── Hola mundo 6: Usando el paquete colorama
# ──────────────────────────────────────────────────────
# ── Imprimir mensajes "Hola mundo" en colores...
# ──────────────────────────────────────────────────────
import colorama

print("══════════════════════════════")
print("Hola mundo normal...")
print(f"{colorama.Fore.RED}Hola mundo en rojo...")
print(f"{colorama.Fore.GREEN}Hola mundo en verde...")
# -- Reseteamos el color
print(colorama.Style.RESET_ALL, end="")
print("──────────────────────────────")
