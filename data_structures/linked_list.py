class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, arr):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        for val in arr:
            self.append_node(val)

    def __repr__(self):
        cur = self.head.next
        res = []
        while cur != self.tail:
            res.append(str(cur.val))
            cur = cur.next
        return '->'.join(res)

    def append_node(self, val):
        node = Node(val)
        predecessor = self.tail.prev
        predecessor.next = node
        self.tail.prev = node
        node.prev = predecessor
        node.next = self.tail
