#! /usr/bin/env python3
import socket
import selectors
import types

sel = selectors.DefaultSelector()

##################### ACCEPT CONNECTION WRAPPER ######################
def accept_conn(sock):
    conn, addr = sock.accept()
    print(f"{conn} is accepted from {addr}")
    conn.setblocking(False)

    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')

    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    sel.register(conn, events, data=data)
################## END ACCEPT CONNECTION WRAPPER #####################

################# SERVICE CONNECTION ################################
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to; {data.addr}")
            sel.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("Echooing {data.outb.decode('utf8')}")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]
############# END SERVICE CONNECTION ##################################

############################## SOCKET ################################
host, port = 'localhost', 53883
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
s.setblocking(False)
############################ END SOCKET ##############################

############################# EVENT LOOP #############################
sel.register(s, selectors.EVENT_READ, data=None)
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_conn(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print('Hej dåååå kompis!')
finally:
    sel.close()
######################## END EVENT LOOP #################################
