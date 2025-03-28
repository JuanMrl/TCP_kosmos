import socket
import sys

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 5000)
print('Conectando a %s puerto %s' % server_address)
sock.connect(server_address)

try:
    while True:
        # Solicitar al usuario que ingrese un mensaje
        message = input('Ingresa un mensaje (o "DESCONEXION" para salir): ')
        print('Enviando "%s"' % message)
        sock.sendall(message.encode('utf-8'))  

        #Cerrando conexion 
        if message == "DESCONEXION":
            print('Cerrando cliente...')
            break  

        # Esperar una respuesta
        data = sock.recv(1024)  
        print('Recibido "%s"' % data.decode('utf-8'))  

finally:
     print('Cerrando cliente')
     sock.close()