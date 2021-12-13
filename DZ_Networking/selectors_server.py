import selectors
import socket
from fibonacci import fibonacci_of
import time

selector = selectors.DefaultSelector()


def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 8090))
    server_sock.listen()

    selector.register(
        fileobj=server_sock,
        events=selectors.EVENT_READ,
        data=accept_connection
    )

def accept_connection(server_sock: socket.socket) -> None:
    client_socket, client_addr = server_sock.accept()
    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_sock: socket.socket) -> None:
    request = client_sock.recv(4096).decode('utf-8')
    if request:
        some = request[0:5]
        num = int(request[5:])
        if some == "data:":
            t_start = time.time()
            ###
            f = fibonacci_of(num)
            ###
            t_end = time.time()

            t_diff = t_end - t_start
            print(t_diff)
            
            client_sock.send(str(f).encode())
        else:    
            client_sock.send(request.encode())
    else:
        selector.unregister(client_sock)
        client_sock.close()


def event_loop():
    while True:
        events = selector.select()  # key, events (bit mask read or write)
        for key, _ in events: # key has fileobj, events, data
            callback_function = key.data
            callback_function(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()