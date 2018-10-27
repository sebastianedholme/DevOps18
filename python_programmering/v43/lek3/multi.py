import sys
import selectors
import socket

sel = selectors.DefaultSelector()
port = 53883
host = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
s.setblocking(False)

sel.register(s, selectors.EVENT_READ, data=None)

while True:
    event = sel.select(timeout=None)
    for key, mask in event:
        if event:
            print(key)
            print(mask)
        elif not sel.get_map():
            break
