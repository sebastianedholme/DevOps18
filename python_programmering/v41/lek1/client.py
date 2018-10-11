import socket

with socket.socket() as s:
    while True:
        try:
            port = int(input("Enter port> "))
        except TypeError:
            print("port must be an int")
        if port > 0 or port < 65535:
            break
        print("Must be between 0 & 65535")
            
    s.connect(('localhost', port))

    while True:
        # Skicka medelande
        msg = input("Client > ")
        if msg == ':q':
            break
        s.send(b"{msg}".decode('utf8'))

        data = s.recv(1024)
        print(data.decode('utf8'))
print("Hej då!")
