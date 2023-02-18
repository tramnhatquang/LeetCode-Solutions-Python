from typing import *


class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map_key_node = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map_key_node:
            # move the node pointed by key to the tail
            self.move_to_end(self.map_key_node[key])
            return self.map_key_node[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map_key_node:
            self.remove(self.map_key_node[key])

        self.map_key_node[key] = Node(key, value)
        self.insert_to_end(self.map_key_node[key])
        if len(self.map_key_node) > self.capacity:
            # evict the beginning of the LL
            removed_node = self.head.next
            self.remove(removed_node)
            del self.map_key_node[removed_node.key]

    # insert a new node to the tail

    def insert_to_end(self, new_node: Node) -> None:
        prev_node = self.tail.prev
        # update the refs
        prev_node.next = self.tail.prev = new_node
        new_node.next = self.tail
        new_node.prev = prev_node

    # remove a node from the list
    def remove(self, removed_node: Node) -> None:
        prev_node, next_node = removed_node.prev, removed_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def move_to_end(self, node: Node) -> None:
        self.remove(node)
        self.insert_to_end(node)

        # time: O(1) for put and get
        # space: O(capacity) since the space is used only for a hashmap and doubly linked list with at most capacity + 1 elements


from collections import OrderedDict
class LRUCache(OrderedDict):
    """
    This implementation is used OrderedDict, that help to keep track of least recently used items. Let it extend the OrderedDict
    """
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

    # time: O(1) for put/get/move_to_end/popitem()
    # space: O(capacity)