import selectors
import socket

class ServerApplication():
    def __init__(self, port, host):
        self.port = port
        self.host = host

if __name__ == "__main__":
    app = ServerApplication(53883, 'localhost')
