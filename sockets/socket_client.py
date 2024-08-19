import socket
import pickle

host = "127.0.0.1"  #Server's IP
port = 65123        #Destination port (must be the server's listening port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mi_socket:
    mi_socket.connect((host, port))
    while True:
        datos = input(str("CLIENT: "))
        if datos == "quit":
            break
        else:
            bdatos = pickle.dumps(datos)
            mi_socket.sendall(bdatos)
            data = mi_socket.recv(1024)
            datos_str = pickle.loads(data)
            print(f"SERVER: {datos_str}")
    print("Conexión finalizada")