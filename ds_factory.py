from data_structures.linked_list import LinkedList
from constants import *
from utils import Coordinates, DSType


class DataStructureFactory:
    def __init__(self, canvas_width, canvas_height):
        self.data_structures = []
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def create(self, entries, ds_type):
        for entry in entries:
            data_structure = self._get_data_structure(entry, ds_type, self._get_coordinates())
            self.data_structures.append(data_structure)
        return self.data_structures

    def _get_coordinates(self):
        if not self.data_structures:
            return Coordinates(FIRST_NODE_X, self.canvas_height // 2 - NODE_DIAMETER_IN_PIXELS // 2)

        for ds in self.data_structures:
            for node in ds.nodes:
                node.coordinates.y -= NODE_Y_SHIFT
        return Coordinates(FIRST_NODE_X, self.data_structures[-1].nodes[0].coordinates.y + NEXT_DS_Y_SHIFT)

    @staticmethod
    def _get_data_structure(entry, ds_type, coordinates):
        match ds_type:
            case DSType.LINKED_LIST:
                return LinkedList(entry, coordinates)
            case _:
                raise ValueError(ds_type)
