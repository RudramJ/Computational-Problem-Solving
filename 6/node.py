"""
file: node.py
description: A double linkable node class for use in stacks, queues, and linked lists
This class was provided as a reference to work on our own list
Main author: Author
author1: Rudram Joshi
author2: Moinuddin Memon
# importing double linked node from lecture code
"""
class DoubleLinkedNode:

    __slots__ = "value", "front", "back"

    def __init__(self, value, front = None, back = None):
        self.value = value
        self.front = front
        self.back = back

    def __str__(self):
        return str(self.value)

