from constants import *
from utils import Tag


class Arrow:
    def __init__(self, canvas, node):
        self.canvas = canvas
        self.node = node

        self.tail_x = node.coordinates.x + NODE_DIAMETER_IN_PIXELS
        self.tail_y = node.coordinates.y + NODE_DIAMETER_IN_PIXELS // 2
        self.head_x = node.coordinates.x + NODE_DIAMETER_IN_PIXELS + ARROW_LENGTH_IN_PIXELS
        self.head_y = node.coordinates.y + NODE_DIAMETER_IN_PIXELS // 2

        self.arrow = None
        self.create_arrow()

        self.dragging = False
        self.last_x, self.last_y = 0, 0


    def create_arrow(self):
        self.arrow = self.canvas.create_line(
            self.tail_x, self.tail_y, self.head_x, self.head_y,
            arrow='last',
            arrowshape=ARROW_SHAPE,
            width=2,
            tags=(Tag.ALL_CANVAS_ITEMS, Tag.ARROW),
            activefill='#00FF00'
        )

        self.canvas.tag_bind(self.arrow, "<Button-1>", self._start_drag)
        self.canvas.tag_bind(self.arrow, "<B1-Motion>", self._drag)
        self.canvas.tag_bind(self.arrow, "<ButtonRelease-1>", self._stop_drag)

    def _start_drag(self, event):
        self.dragging = True
        self.last_x, self.last_y = event.x, event.y

    def _drag(self, event):
        if self.dragging:
            dx = event.x - self.last_x
            dy = event.y - self.last_y
            self.head_x += dx
            self.head_y += dy
            self.canvas.coords(self.arrow, self.tail_x, self.tail_y, self.head_x, self.head_y)
            self.last_x, self.last_y = event.x, event.y

    def _stop_drag(self, event):
        self.dragging = False
