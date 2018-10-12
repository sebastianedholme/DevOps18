"""
This is my first multi-threaded socket server
"""
import socket
import threading

class ThreadedServer():
    """
    This is the class that defines the multithreaded socket server. The init takes a port
    and a host IP/name. Then it creates a socket object.
    Listens on the socket port and tries to create a connection
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.bind((self.host, self.port))

    def listen(self):
        self.s.listen(5)
        while True:
            client, address = self.s.accept() # Accept sock client connection
            #client.settimeout(60) # Timeout to 60 sec
            threading.Thread(target=self.listen_to_client, args=(client, address))

    def listen_to_client(self, client, address):
        """
        Return to the threading with client connection and responds to client
        """
        size = 1024
        while True:
            try:
                data = client.recv(size)
                response = data.decode('utf8')
                client.send(response)
            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = int(input("What port: "))

        ThreadedServer('', port_num).listen()
