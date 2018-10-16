from tkinter import *
from tkinter.ttk import *

def calculate(*args):
    try:
        x_calc = int(x.get())
        y_calc = int(y.get())
        result.set(x_calc + y_calc)
    except ValueError:
        pass

# Skapar main fönstret
root = Tk()
root.title("Feet to meters")

s = Style()
s.configure("BW.TLabel", foreground="", background="dark orchid")

# mainframe är mitt huvud fönster.
mainframe = Frame(root, padding="3 3 12 12", style="BW.TLabel") # Paddingen mot root
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

x = IntVar()
y = IntVar()
result = StringVar()

x_entry = Entry(mainframe, width=5, textvariable=x)
y_entry = Entry(mainframe, width=5, textvariable=y)

x_entry.grid(column=1, row=1, sticky=(W, E))
y_entry.grid(column=2, row=1, sticky=(W, E))

Label(mainframe, textvariable=result, style="BW.TLabel").grid(column=2, row=2, sticky=(W, E))
Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=1, sticky=W)

root.mainloop()
