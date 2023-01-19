# The following code is based on the code shown in labs written by the TA and his github repository
# Referenced author: aianta
# Profile page: https://github.com/aianta
# Repository: https://github.com/aianta/cmput404-tcp-lab

import socket

BUFFER_SIZE = 4069

def get(host, port):
    request = b"GET / HTTP/1.1\nwww.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request)
        s.shutdown(socket.SHUT_WR)
        print("waiting for response!")
        chunk = s.recv(BUFFER_SIZE)
        result = b'' + chunk

        while len(chunk) > 0:
            chunk = s.recv(BUFFER_SIZE)
            result += chunk
        
        return result

print(get("127.0.0.1", 8080))