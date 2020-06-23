# linked_list.py
# Sample Linked List Module


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None

    def append(self, value):
        if self.current is None:
            self.first = Node(value)
            self.last = self.first
            self.current = self.first
        else:
            self.last.next = Node(value)
            self.last = self.last.next

    def prepend(self, value):
        if self.current is None:
            self.first = Node(value)
            self.last = self.first
            self.current = self.first
        else:
            first_node = Node(value)
            first_node.next = self.first
            self.first = first_node
            self.current = self.first
