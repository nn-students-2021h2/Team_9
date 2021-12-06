import socket
from select import select
from fibonacci import fibonacci_of

def get_server_socket():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 8090))
    server_sock.listen()

    return server_sock


to_monitor = []


def accept_connection(server_sock: socket.socket) -> None:
    client_socket, client_addr = server_sock.accept()
    to_monitor.append(client_socket)


def send_message(client_sock: socket.socket) -> None:
    request = client_sock.recv(4096).decode('utf-8')
    if request:
        some = request[0:5]
        num = int(request[5:])
        if some == "data:":
            client_sock.send(str(fibonacci_of(num)).encode())
        else:    
            client_sock.send(request.encode())
    else:
        to_monitor.remove(client_sock)
        client_sock.close()


def event_loop():
    while True:
        # readable, writable, errors
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock == server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    server_socket = get_server_socket()
    to_monitor.append(server_socket)
    event_loop()