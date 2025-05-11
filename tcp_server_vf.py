import socket 


#Funcion correr servidor
def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Permite reutilizar la misma dirección IP y puerto inmediatamente 
    # después de cerrar el servidor, evitando el error "Address already in use".
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    server_address = ('Localhost', 5000)
    print(f"Iniciando servidor en: {server_address}")

    try:
        #Asocia el socket a la dirección y puerto especificados
        sock.bind(server_address)
        sock.listen(5)
        #bucle infinito para aceptar múltiples clientes 
        # (uno a la vez en este caso).
        while True:
            print("Esperando a un conexion...")
            connection, client_address = sock.accept()
            try:
                print(f'Conectado a {client_address}')
                #Se inicia otro bucle para manejar la comunicación con el cliente actual.
                #recv(1024) recibe hasta 1024 bytes de datos del cliente.
                while True:
                    data = connection.recv(1024)
                    if not data:
                        print(f'{client_address} cerró la conexión')
                        break
                    message = data.decode('utf-8')
                    print(f'Recibido: "{message}"')
                    if message == "DESCONEXION":
                        print(f'Cerrando conexión con {client_address}')
                        break
                    connection.sendall(message.upper().encode('utf-8'))
            finally:
                connection.close()
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario")
    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        sock.close()


if __name__ == '__main__':
    run_server()