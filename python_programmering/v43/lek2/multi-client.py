#!/usr/bin/env python3
"""
A multi socket client
"""
import sys
import selectors
import socket
import types

sel = selectors.DefaultSelector()

messages = [b'Message 1 from client.', b'Message 2 from client.']

def start_connections(host, port, num_conns):
    server_addr = (host, port) # Starting connection

    for i in range(0, num_conns):
        connid = i + 1
        print(f'Starting connection {connid}, to {server_addr}')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(False)

        s.connect_ex(server_addr)

        events = selectors.EVENT_READ | selectors.EVENT_WRITE

        data = types.SimpleNamespace(connid=connid,
                                     msg_total=sum(len(m) for m in messages),
                                     recv_total=0,
                                     messages=list(messages),
                                     outb=b'')

        sel.register(s, events, data=data)

def service_connection(key, mask):
    s = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = s.recv(1025)
        if recv_data:
            print(f'Recieved: {repr(recv_data)} from {data.connid}')
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print("Closing connection {data.connid}")
            sel.unregister(s)
            s.close()

    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
    if data.outb:
        print(f'sending.. > {repr(data.outb)} to {data.connid}')
        sent = s.send(data.outb)
        data.outb = data.outb[sent:]



if len(sys.argv) != 4:
    print("Usage: ", sys.argv[0], "<host> <port> <num_conns>")
    sys.exit(1)

host, port, num_conns = sys.argv[1:4]

start_connections(host, int(port), int(num_conns))

try:
    while True:
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
