import socket
import json
from fibonacci import fibonacci_of

def get_server_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind(('localhost', 8090))
    sock.listen()

    return sock

server_socket = get_server_socket()

while True:
    client_socket, addr = server_socket.accept()

    while True:
        request = client_socket.recv(4096).decode('utf-8')
        some  = request[0:5]
        print(some)
        if not request:
            break
        else:
            if some == "data:":
                print('test')
                client_socket.send(str(fibonacci_of(int(request[5:]))).encode())
            else:    
                client_socket.send(request.encode())
    client_socket.close()
