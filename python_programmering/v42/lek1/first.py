from tkinter import *
from tkinter.ttk import *

def Click_Enter():
    entry.insert(0, "Hej")

window = Tk()
main_label = Label(window, text="Sebbes Program")

main_label.pack(side="top")

###################################################################################################################

# Right Frame
frame_b = Frame(window)

b1 = Button(frame_b, text="Enter", command=Click_Enter)
b2 = Button(frame_b, text="Cancel")

# Packing Right Frame
b1.pack(side="top", fill="x")
b2.pack(side="bottom", fill="x")

frame_b.pack(side="right")

###################################################################################################################

# Left Frame
frame_a = Frame(window)

label_a = Label(frame_a, text="Hej")
entry = Entry(frame_a)

# Packing left frame
entry.pack(side="bottom")
label_a.pack(side="top")

frame_a.pack(side="left")

#################################################################################################################

# Bottom frame
frame_c = Frame(window)
q_buttom = Button(frame_c, text="Quit")

frame_c.pack(side="bottom")

q_buttom.pack(side="bottom")
window.mainloop()
