# The following code is based on the code shown in labs written by the TA and his github repository
# Referenced author: aianta
# Profile page: https://github.com/aianta
# Repository: https://github.com/aianta/cmput404-tcp-lab

import socket

BUFFER_SIZE = 4096
HOST = "127.00.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            print(data)
            conn.sendall(data)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # automatically closes the socket when leaving the with block
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()
        conn, addr =  s.accept()
        handle_connection(conn, addr)

start_server()