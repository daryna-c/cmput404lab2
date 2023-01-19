# The following code is based on the code shown in labs written by the TA and his github repository
# Referenced author: aianta
# Profile page: https://github.com/aianta
# Repository: https://github.com/aianta/cmput404-tcp-lab

import socket

BUFFER_SIZE = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BUFFER_SIZE)
    while(len(result) > 0):
        print(result)
        result = s.recv(BUFFER_SIZE)
    s.close()

def main():
    get("www.google.com", 80)


main()
