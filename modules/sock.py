# Socket module
# Without it... we're going nowhere!

import socket

class sock:
    _sock = 0

    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, server, port):
        self._sock.connect((server, port))

    def send(self, data):
        return self._sock.send(data)

    def recv(self):
        return self._sock.recv(2048)
