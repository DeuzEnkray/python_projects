# __gold-init__
# Stack implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__top = None
        self.__n = 0

    def push(self, data):
        node = Node(data)

        if self.__top is None:
            self.__top = node

        else:
            node.next = self.__top
            self.__top = node

        self.__n += 1

    def pop(self):
        if self.__top is None:
            return None

        else:
            data = self.__top.data
            self.__top = self.__top.next
            self.__n -= 1
            return data

    def top(self):
        return self.__top.data

    def is_empty(self):
        return self.__top is None

    def size(self):
        return self.__n
