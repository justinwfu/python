# Linked List
# Collection of nodes fast to insert O(1) if indexing separate
# Index O(n) is no current marker


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


print(f'testing Node object')
print(f'raw testing {Node(5)}')
n = Node(5)
print(f'testing assigned node {n}')


class LinkedList:
    def __init__(self):
        self.current = None
        self.first = None
        self.last = None

    def __str__(self):
        return f'Current: {self.current} Previous: {self.current.previous}'\
               f'Next: {self.current.next}'

    def __repr__(self):
        return f'{self.next}\t{self.previous}\t{self.current}'

    def append(self, value):
        if self.current is None:
            self.current = Node(value)
            print(f'current = {self.current}')
            self.first = self.current
            # ahhhhhhh make sure assign that *same* node object
            # dont instantiate a new one
            # self.first = Node(value)

            print(f'first = {self.current}')
            # self.last = Node(value)
        else:
            self.current.next = Node(value)
            print(f'current.next = {self.current.next}')
            self.current.next.previous = self.current
            print(f'current.next.previous = {self.current.next.previous}')
            self.current = self.current.next
            print(f'current = {self.current}')

            # self.last = Node(value)

    def prepend(self, value):
        if self.current is None:
            self.current = Node(value)
        else:
            self.first.previous = Node(value)
            self.current = Node(value)
            self.current.next = self.first
            self.first = self.current


ll = LinkedList()
# print('linkedlist representation')
# print(ll)

ll.append(1)
# self.current was None
# self.current == Node(1)
# self.first == Node(1)
ll.append(2)
# self.current was Node(1)
# Node(1).next == Node(2)
# Node(2).previous == Node(1)
# self.current == Node(2)

ll.prepend(0)

print('testing iteration')
while ll.current is not None:
    print(f'current node value is {ll.current}')
    # print(f'next node value is {ll.current.next}')
    ll.current = ll.current.next
