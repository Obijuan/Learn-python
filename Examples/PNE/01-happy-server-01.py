# ──────────────────────────────────────────────────────
# ── Ejemplo 1: happy server!
# El servidor se queda esperando conexiones. En cuanto
# se conecta un cliente, se imprime un mensaje y 
# se termina
# ──────────────────────────────────────────────────────
import socket

#-- Configurar el puerto y la IP
PORT = 5678
IP = "127.0.0.1" #-- Localhost

#-- Paso 1: Crear el socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#-- Paso 2: Asociar el socket a una IP y un puerto
server.bind((IP, PORT))

#-- Paso 3: Escuchar conexiones
server.listen()

print(f"Servidor escuchando en el puerto: {PORT}")
print("Esperando conexiones...")

#-- Paso 4: Aceptar conexiones
server.accept()

print("Cliente conectado!!!")

#-- Cerrar el socket
server.close()

