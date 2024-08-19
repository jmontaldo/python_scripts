import socket, pickle

host = "127.0.0.1"         #loopback's direction
port = 65123               # > 1023 --> listening port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mi_socket:
    mi_socket.bind((host, port))
    mi_socket.listen()
    conn, adress = mi_socket.accept()
    with conn:
        print(f"Conectado a {adress}")
        while True:
            try:
                data = conn.recv(1024)
                message = pickle.loads(data)
                print(f"CLIENT: {message}")
                if not data:
                    print("Conexión finalizada")
                    break
                else:
                    texto = f"El mensaje tiene {len(message)} caracteres"
                    bdatos = pickle.dumps(texto)
                    conn.sendall(bdatos)
            except:
                print("Conexión finalizada")
                break
