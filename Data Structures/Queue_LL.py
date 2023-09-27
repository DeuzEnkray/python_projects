# __gold-init__
# Queue implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__n = 0

    def enqueue(self, data):
        node = Node(data)

        if self.__front is None:
            self.__front = node
            self.__rear = node

        else:
            self.__rear.next = node
            self.__rear = node

        self.__n += 1

    def dequeue(self):
        if self.__front is None:
            print('Queue empty')

        else:
            data = self.__front.data
            self.__front = self.__front.next
            self.__n -= 1
            return data

    def front(self):
        if self.__front is None:
            return None

        else:
            return self.__front.data

    def rear(self):
        if self.__front is None:
            return None

        else:
            return self.__rear.data

    def is_empty(self):
        return self.__front is None
