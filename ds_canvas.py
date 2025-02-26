from tkinter import *

from utils import Tag
from constants import *


class DSCanvas:
    def __init__(self, parent):
        self.canvas = Canvas(parent)
        self.canvas.configure(width=CANVAS_WIDTH_IN_PIXELS, height=CANVAS_HEIGHT_IN_PIXELS, background="white")

        self.canvas.tag_bind(Tag.POINTER, "<Button-1>", self._start_drag)
        self.canvas.tag_bind(Tag.POINTER, '<B1-Motion>', self._drag)
        self.canvas.tag_bind(Tag.POINTER, '<ButtonRelease-1>', self._stop_drag)

        self.canvas.grid(column=0, row=2, columnspan=2, sticky="nsew")

        self.dragging = False
        self.item = None
        self.last_x, self.last_y = 0, 0

    def _start_drag(self, event):
        self.dragging = True
        self.item = self.canvas.find_withtag("current")[0]
        self.last_x, self.last_y = event.x, event.y

    def _drag(self, event):
        if self.dragging:
            dx = event.x - self.last_x
            dy = event.y - self.last_y
            self.canvas.move(self.item, dx, dy)
            self.last_x, self.last_y = event.x, event.y

    def _stop_drag(self, event):
        self.dragging = False
