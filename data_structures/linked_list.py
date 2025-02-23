from constants import *
from utils import Coordinates, Tag


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

        self.coordinates = Coordinates()
        self.oval = None
        self.arrow = None
        self.text = None


class LinkedList:
    def __init__(self, arr, coordinates):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = arr
        self.coordinates = coordinates
        self._build()

    def __repr__(self):
        cur = self.head.next
        res = []
        while cur != self.tail:
            res.append(str(cur.val))
            cur = cur.next
        return '->'.join(res)

    def _build(self):
        for val in self.data:
            self._append_node(val)

    def _append_node(self, val):
        node = Node(val)
        predecessor = self.tail.prev
        predecessor.next = node
        self.tail.prev = node
        node.prev = predecessor
        node.next = self.tail

        self._get_node_coordinates(node)

    def _get_node_coordinates(self, node):
        if node.prev.coordinates.x == 0:
            node.coordinates = self.coordinates
        else:
            node.coordinates.x = node.prev.coordinates.x + NODE_DIAMETER_IN_PIXELS + ARROW_LENGTH_IN_PIXELS
            node.coordinates.y = self.coordinates.y

    @staticmethod
    def _get_node_oval(canvas, node):
        return canvas.create_oval(
                node.coordinates.x,
                node.coordinates.y,
                node.coordinates.x + NODE_DIAMETER_IN_PIXELS,
                node.coordinates.y + NODE_DIAMETER_IN_PIXELS,
                width=2,
                tags=Tag.ALL_CANVAS_ITEMS
            )

    @staticmethod
    def _get_node_arrow(canvas, node):
        return canvas.create_line(
            node.coordinates.x + NODE_DIAMETER_IN_PIXELS,
            node.coordinates.y + NODE_DIAMETER_IN_PIXELS // 2,
            node.coordinates.x + NODE_DIAMETER_IN_PIXELS + ARROW_LENGTH_IN_PIXELS,
            node.coordinates.y + NODE_DIAMETER_IN_PIXELS // 2,
            arrow='last',
            arrowshape=ARROW_SHAPE,
            width=2,
            tags=Tag.ALL_CANVAS_ITEMS
        )

    @staticmethod
    def _get_node_text(canvas, node):
        return canvas.create_text(
            node.coordinates.x + NODE_DIAMETER_IN_PIXELS // 2,
            node.coordinates.y + NODE_DIAMETER_IN_PIXELS // 2,
            text=node.val,
            font=VALUE_FONT,
            tags=Tag.ALL_CANVAS_ITEMS
        )

    def map_to_canvas(self, canvas):
        cur = self.head.next
        while cur != self.tail:
            cur.oval = self._get_node_oval(canvas, cur)
            cur.arrow = self._get_node_arrow(canvas, cur)
            cur.text = self._get_node_text(canvas, cur)
            print(f"current node oval id: {cur.oval}")
            print(f"current node arrow id: {cur.arrow}")
            print(f"current node text id: {cur.text}")
            cur = cur.next
