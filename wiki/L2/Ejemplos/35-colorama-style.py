# ──────────────────────────────────────────────────────
# ── Pruebas de estilo
# ──────────────────────────────────────────────────────
import colorama as col

print()

# ── Impresión en diferentes estilos
print("══════════════════════════════")
print(f"{col.Style.NORMAL}Mensaje con estilo normal...")
print(f"{col.Style.BRIGHT}Mensaje con estilo resaltado...")
print(f"{col.Style.DIM}Mensaje con estilo apagado....")


# ── Establecer colores por defecto
print(col.Style.RESET_ALL, end="")
print("──────────────────────────────")
print()
