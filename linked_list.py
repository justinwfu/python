# Linked List
# Collection of nodes fast to insert O(1) if indexing separate
# Index O(n) is no current marker


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
        if self.current == None:
            self.first = Node(value)
            self.last = self.first
            self.current = self.first

        else:
            self.last.next = Node(value)
            self.last = self.last.next

    def prepend(self, value):
            first_node = Node(value)
            first_node.next = self.first
            self.first = first_node
            self.current = self.first


# test cases
# 1. append 
# 2. prepend
# 3. append and append
# 4. append and prepend
# 5. prepend and append
# 6. append and prepend and append
# 7. prepend and append and prepent

