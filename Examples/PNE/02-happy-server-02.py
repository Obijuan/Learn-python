# ──────────────────────────────────────────────────────
# ── Ejemplo 2: happy server!
# ──────────────────────────────────────────────────────
# 
# ──────────────────────────────────────────────────────
import socket

#-- Configurar el puerto y la IP
PORT = 5678
IP = "127.0.0.1" #-- Localhost

#-- Paso 1: Crear el socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Opcional: Configurar el socket para reutilizar puertos
# -- Soluciona el error del "Port already in use"
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#-- Paso 2: Asociar el socket a una IP y un puerto
server.bind((IP, PORT))

#-- Paso 3: Escuchar conexiones
server.listen()

print(f"Servidor escuchando en el puerto: {PORT}")
print("Esperando conexiones...")

#-- Paso 4: Aceptar conexiones
#-- Devuelve una tupla con el socket y la dirección IP
cs, ip = server.accept()

print("Cliente conectado!!!")

#-- Leer el mensaje del cliente
msg_raw = cs.recv(2048)

print(msg_raw.decode())

#-- Cerrar el socket
server.close()
