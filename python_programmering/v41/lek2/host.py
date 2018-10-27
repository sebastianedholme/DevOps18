import socket

port = 53883

with socket.socket() as s:
    s.bind(('', port))
    print(f"Socket is binded to port: {port}")
    s.listen(5)
    print("Listening...")

    c, addr = s.accept() # Client anslutningen
    print(addr)
    while True:
        # Ta emot
        msg = c.recv(1024)
        if not msg:
            break
        print(f"Server<< {msg.decode('utf8')}")

print("Hej då!")
