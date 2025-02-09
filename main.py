from tkinter import *
from tkinter import ttk

root = Tk()

canvas = Canvas(root, width=1500, height=750, background='white')

canvas.grid(column=0, row=0, sticky="nswe")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
