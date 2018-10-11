import socket

port = 53883

with socket.socket() as s:
    s.bind(('127.0.0.1', port))
    print(f"Socket is binded to port: {port}")
    while True:
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

        print("The connection from the client was closed")
        command = input("Would you like to quit? Y/N")
        if command.lower == 'y':
            break

print("Hej då!")
