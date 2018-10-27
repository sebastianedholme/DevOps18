from tkinter import *
import selectors
import socket
import types

window = Tk()
def onquit():
    quit()

def start_connection(host, port):
    server = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)

    print(f"Starting connection to to {server}")

    s.connect(server)

    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    ### CONN ID FROM TKINKER
    data = types.SimpleNamespace(recv_total=0, outb=b'')

    sel.register(s, events, data=data)

def service_connection(key, mask):
    s = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = s.recv(1024)
        if recv_data:
            ### CONNID FROM TKINTER
            print(f"Recieved: {repr(recv_data)} from {data.connid}")
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print(f"Closing connection {data.connid}")
            sel.unregister(s)
            s.close()

sel = selectors.DefaultSelector()

host, port = 'localhost', 53883

def start_btn():
    start_connection(host, port)

    try:
        while True:
            events = sel.select(timeout=1)
            if events:
                for key, mask in events:
                    service_connection(key,mask)
                    if not sel.get_map:
                        break
    except KeyboardInterrupt:
        print("Good Bye!")
    finally:
        sel.close()

textbox = Text(window)
entryfield = Entry(window)
connect_btn = Button(window, text="Start", command=start_btn)

connect_btn.pack()
textbox.pack()
entryfield.pack(fill=X)

window.protocol("WM_DELETE_WINDOW", onquit)
window.mainloop()


#entryfield.bind("<Return>", sendmsg)
#receivethread = Thread(target=receive)
#receivethread.start()
