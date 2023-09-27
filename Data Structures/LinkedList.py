# __gold-init__
# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__n = 0

    def __str__(self):
        result = ''
        node = self.__head
        while node is not None:
            result += str(node.data) + ', '
            node = node.next

        return '[' + result[:-2] + ']'

    def __len__(self):
        return self.__n

    def __getitem__(self, index):
        node = self.__return_node_at_index(index)
        if node == -1:
            return None

        return node.data

    def __delitem__(self, key):
        self.pop(key)

    # Private functions
    def __return_node_at_index(self, index):
        if index > self.__n - 1:
            return -1

        current_node = self.__head

        for i in range(index):
            current_node = current_node.next

        return current_node

    def __find_node_index(self, data):
        index = 0
        current_node = self.__head

        while current_node.next is not None:
            if current_node.data == data:
                return index
            index += 1
            current_node = current_node.next

        return -1

    # Insert functions
    def insert(self, data, index=None):
        if index is not None and not self.__n >= index >= 0:
            print('Invalid Index')

        else:
            node = Node(data)
            if index is None or index == 0:
                if self.__head is None:
                    self.__head = node

                else:
                    node.next = self.__head
                    self.__head = node

            else:
                prev_node = self.__return_node_at_index(index - 1)
                node.next = prev_node.next
                prev_node.next = node

            self.__n += 1

    def append(self, data):
        if self.__head is None:
            self.insert(data)

        else:
            node = Node(data)
            last_node = self.__return_node_at_index(self.__n - 1)
            last_node.next = node

        self.__n += 1

    def insert_after(self, key, data):
        index = self.__find_node_index(key)
        if index == -1:
            print(key, 'not present in the list')

        elif index == 0:
            self.insert(data)

        else:
            self.insert(data, index + 1)

    # Delete function
    def pop(self, index=None):
        if self.__head is None:
            print('List Empty')

        else:
            if index is None:
                node = self.__return_node_at_index(self.__n - 2)
                node.next = node.next.next
                self.__n -= 1

            elif index == 0:
                self.__head = self.__head.next
                self.__n -= 1

            elif self.__n >= index >= 0:
                node = self.__return_node_at_index(index - 1)
                node.next = node.next.next
                self.__n -= 1

            else:
                print('Invalid Index')

    def clear(self):
        self.__head = None
        self.__n = 0
