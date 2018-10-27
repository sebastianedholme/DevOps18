from tkinter import *

root = Tk()

window = Frame(master=root)

wpath = "/usr/share/icons/gnome/48x48/apps/libreoffice-"
weather = ["base","calc","draw","math","main","writer"]
buttons = []

count = 0

for w in weather:
    count +=1
    buttons.append(Button(window))
    b = buttons[-1]
    b.image = PhotoImage(file=wpath+w+'.png')
    b.configure(image=b.image)
    b.grid(row=1, column=count)


root.mainloop()
