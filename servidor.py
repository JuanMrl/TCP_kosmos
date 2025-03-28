import socket 

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección del servidor
server_address = ('localhost', 5000)
print('Conectando a %s puerto %s' % server_address)
sock.bind(server_address)

# Escuchar conexiones entrantes
sock.listen(5)

while True:
    print('Esperando conexión...')
    connection, client_address = sock.accept()  # Aceptar la conexión
    try:
        print('Conectado a', client_address)
        while True:
            # Recibir datos en bloques de bytes
            data = connection.recv(1024)
            if not data:
                print('No hay más datos de', client_address)
                break  # Salir si no hay más datos

            message = data.decode('utf-8')  # Decodificar los datos recibidos
            print('Recibido "%s"' % message)

            if message == "DESCONEXION":
                print('Cerrando conexión con', client_address)
                break  # Salir del bucle para cerrar la conexión

            #mensaje en mayúsculas
            response = message.upper()
            connection.sendall(response.encode('utf-8'))  # Enviar la respuesta al cliente

    finally:
        connection.close()  