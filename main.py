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

sketchpad.create_line(10, 10, 200, 50, 90, 150, 50, 80, fill="red", width=10, activestipple="gray50", joinstyle="miter", smooth="raw", splinesteps=50)

root.mainloop()
