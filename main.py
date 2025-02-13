from tkinter import *
from tkinter import ttk


class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.last_x = None
        self.last_y = None
        self.bind("<Button-1>", self.save_position)
        self.bind("<B1-Motion>", self.add_line)

    def save_position(self, event):
        self.last_x, self.last_y = event.x, event.y

    def add_line(self, event):
        self.create_line(self.last_x, self.last_y, event.x, event.y)
        self.save_position(event)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sketchpad = Sketchpad(root, width=1500, height=750, background='white')
sketchpad.grid(column=0, row=0, sticky="nswe")

sketchpad.create_oval(625, 250, 875, 500, fill='red', outline='blue', width=5, activestipple="gray50")
sketchpad.create_text(700, 300, text='A wonderful story', anchor='nw', font='TkMenuFont', fill='white')

root.mainloop()
