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

    ip = input("Vilken IP vill du ansluta till? > ")
    s.connect((ip, port))

    while True:
        # Skicka medelande
        msg = input("Client > ")
        if msg == ':q':
            break
        s.send(bytes(msg, 'utf8')) # Skicka byte data
print("Hej då!")
