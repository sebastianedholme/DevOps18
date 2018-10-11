import socket

with socket.socket()as s:
    print("Socket created")

    # reserve port
    port = 53883

    # Bind the port for the server to listen to
    # We do not bind it to any specific IP so it listens to all computers on the network
    s.bind(('127.0.0.1', port))
    print(f"Socket is binded to port {port}")

    # Next we put the socket to listening mode
    s.listen(5) # 5 specifies number of unaccepted connections
    print("socket is listening")

    # Returns a new socket object allowing data stream
    c, addr = s.accept()
    print(f"Got connection from {addr}")

    while True:
        print(".... Wating message .....")
        data = c.recv(1024)
        print("Recieved!")
        print(f"\nMessage recieved: {data.decode('utf8')}")

