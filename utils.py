from enum import StrEnum

class Coordinates:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Tag(StrEnum):
    ALL_CANVAS_ITEMS = "all_canvas_items"
    ARROW = "arrow"
    ARROW_POINT = "arrow_point"


class DSType(StrEnum):
    LINKED_LIST = "Linked List"
    TREE = "Tree"
    GRAPH = "Graph"
