# ──────────────────────────────────────────────────────
# ── Imprimir mensajes en colores
# ── usando el modulo colorama
# ──────────────────────────────────────────────────────

# ── Renombrar el módulo como 'col'
import colorama as col

print("══════════════════════════════")
print("Mensaje con atributos normales")

# ── Usamos el nuevo nombre 'col' como prefijo
print(f"{col.Fore.RED}Mensaje en rojo")
print(f"{col.Fore.GREEN}Mensaje en verde")

# ── Establecer colores por defecto
print(col.Style.RESET_ALL, end="")
print("──────────────────────────────")
