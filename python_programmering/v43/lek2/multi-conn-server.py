#!/usr/bin/env python3

import sys
import selectors
import socket
import types

# Instanciate selector. The selector will be used to listen to a socket.
sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print(f"{conn} is accepted from {addr}")
    conn.setblocking(False) # Stop blocking on this socket

    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')

    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print(f"closing connection to; {data.addr}")
            sel.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {repr(data.outb)} to {data.addr}")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

if len(sys.argv) != 3:
    print("Usage, ", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Start a socket server and listen
listen_sock.bind((host, port))
listen_sock.listen()

print("Server will now start to listen")

# Stop blocking from several requests to the server.
listen_sock.setblocking(False)


# We register a selector to listen to our listen_sock
# The data will be the stream of data to listen to in
# the event loop
# The data is returned when select() is returned
sel.register(listen_sock, selectors.EVENT_READ, data=None)

# Event loop
try:
    while True:
        # sel.select returns a list of key, events tuples, ONE for each socket
        # the key is a selectorKey namedtuples that contains the fileobj attribute
        # and is the socket object
        events = sel.select(timeout=None) # Never timeout
        for key, mask in events:
            # If the key.data is None, it's coming from the listening socket(No data has been sent or recv)
            if key.data is None:
                accept_wrapper(key.fileobj) # This will accept a new connection
                # If the key.data contains somethings, the connection has already been accepted and
                # can be used to read data
            else:
                service_connection(key, mask) # This will service the connection and data
except KeyboardInterrupt:
    print('Caught keyboard interrupt, exiting')
finally:
    sel.close()
