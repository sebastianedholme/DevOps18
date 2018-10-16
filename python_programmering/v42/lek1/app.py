from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        print(master)

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        Button(self, text="QUIT", fg="red",
                              command=root.destroy).pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
app = Application(master=root)

app.mainloop()
