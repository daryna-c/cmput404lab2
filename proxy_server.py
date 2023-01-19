# The following code is based on the code shown in labs written by the TA and his github repository
# Referenced author: aianta
# Profile page: https://github.com/aianta
# Repository: https://github.com/aianta/cmput404-tcp-lab

import socket
from threading import Thread

BUFFER_SIZE = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8080

def send_request(host, port, request_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Sending data to google
        client_socket.connect((host, port))
        client_socket.send(request_data)
        client_socket.shutdown(socket.SHUT_WR)

        # Getting response
        data = client_socket.recv(BUFFER_SIZE)
        result = b''+ data
        while len(data) > 0:
            data = client_socket.recv(BUFFER_SIZE)
            result += data

        return result


def handle_connection(conn, addr):
    with conn:
        print(f"Connected by: {addr}")
        request = b''
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            print(data)
            request += data
        response = send_request("www.google.com", 80, request)
        conn.sendall(response)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        conn, addr =  server_socket.accept() #?
        handle_connection(conn, addr) #?

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2) #queue of 2

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

#start_server()
start_threaded_server()