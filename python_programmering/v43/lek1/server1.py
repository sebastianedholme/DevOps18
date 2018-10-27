import socket
import selectors

def accept(sock, mask):
    conn, addr = s.accept()
    print(f'Connection accepted {conn} from {addr}')
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

port = 53883

s = socket.socket()
sel = selectors.DefaultSelector()

s.bind(('', port))
s.listen(100)
s.setblocking(False)
sel.register(s, selectors.EVENT_READ, accept)

print("Socket is binded to port: %s" % port)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

