from enum import StrEnum

from data_structures.linked_list import LinkedList


class DSType(StrEnum):
    LINKED_LIST = "Linked List"
    TREE = "Tree"
    GRAPH = "Graph"


class DataStructureFactory:
    def create(self, entry, ds_type):
        data_structure = self._get_data_structure(entry, ds_type)
        return data_structure

    @staticmethod
    def _get_data_structure(entry, ds_type):
        match ds_type:
            case DSType.LINKED_LIST:
                return LinkedList(entry)
            case _:
                raise ValueError(ds_type)
