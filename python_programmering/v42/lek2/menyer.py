from tkinter import *

root = Tk()

root.geometry("500x500")

window_frame = Frame(root, bg="white")
window_frame.grid(column=0, row=0, sticky=(N, W, E, S))
toolbar = Frame(window_frame, bg="blue")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
edit_menu = Menu(menu)
view_menu = Menu(menu)
help_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="View", menu=view_menu)
menu.add_cascade(label="Help", menu=help_menu)

new_file_menu = Menu(file_menu)
file_menu.add_cascade(label="New", menu=new_file_menu)

image = PhotoImage(file="accessories-calculator.png")
image_label = Label(window_frame, image=image)
image_label.grid(row=1, sticky=(N, W, E, S))

#calc_label = Label(window_frame, text="000000000")
#calc_label.grid(row=2, sticky=(N, W, E, S))

root.mainloop()
