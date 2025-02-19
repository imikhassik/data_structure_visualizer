from enum import StrEnum

from data_structures.linked_list import LinkedList
from constants import *
from utils import Coordinates


class DSType(StrEnum):
    LINKED_LIST = "Linked List"
    TREE = "Tree"
    GRAPH = "Graph"


class DataStructureFactory:
    def __init__(self):
        self.data_structures = []

    def create(self, entry, ds_type):
        data_structure = self._get_data_structure(entry, ds_type, self._get_coordinates())
        self.data_structures.append(data_structure)
        return data_structure

    def _get_coordinates(self):
        if not self.data_structures:
            return Coordinates(FIRST_NODE_X, FIRST_NODE_Y)

    @staticmethod
    def _get_data_structure(entry, ds_type, coordinates):
        match ds_type:
            case DSType.LINKED_LIST:
                return LinkedList(entry, coordinates)
            case _:
                raise ValueError(ds_type)
