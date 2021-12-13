import socket
import time
from get_custom_logger import get_logger
import json

#logger = get_logger("Echo_test")
def echo_server_test(server_name: str, host: str, port: int, log_name: str):
    logger = get_logger(log_name)
    client_socket = socket.socket()
    server_host = host
    server_port = port
    client_socket.connect((server_host, server_port))

    n = 1500
    t_diff = 0
    while t_diff < 1:
        t_start = time.time()
        for i in range(n):
            client_socket.send('Some'.encode())
            response = client_socket.recv(100)
        t_end = time.time()
        t_diff = t_end - t_start
        n += 100
    logger.info(f"{server_name} approximately {n} in one second({t_diff})")
    client_socket.close()

def cpu_bound_server_test(server_name: str, host: str, port: int, log_name: str):
    logger = get_logger(log_name)
    client_socket = socket.socket()
    server_host = host
    server_port = port
    n = 30
    client_socket.connect((server_host, server_port))

    t_start = time.time()
    client_socket.send(f"data:{n}".encode())
    response = client_socket.recv(4096)
    #print(response)
    t_end = time.time()
    t_diff = t_end - t_start
    
    logger.info(f"{server_name} fibonacci of {n} calculate for {t_diff}")



def main():
    cpu_bound_server_test(server_name="Selectors_server", host="localhost", port=8090, log_name='cpu_bound_test')

if __name__ == "__main__":
    main()