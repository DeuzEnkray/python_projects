# __gold-init__
# Dictionary implementation using hashing and chaining

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Inserts node at tail
    def insert(self, key, value):
        node = Node(key, value)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    # Searches for key in linked list
    def find_key(self, key):
        current_node = self.head
        counter = 0

        if current_node is None:
            return None

        while current_node is not None:
            if current_node.key == key:
                return counter

            counter += 1
            current_node = current_node.next

        return None

    # Remove node from linked list
    def remove(self, key):
        index = self.find_key(key)

        if index == 0:
            self.head = self.head.next

        elif index is not None:
            node = self.head

            for i in range(index - 1):
                node = node.next

            node.next = node.next.next

            if node.next is None:
                self.tail = node

        else:
            return -1

    # Return node at index
    def return_node_at_index(self, index):
        if self.head is None:
            return None

        elif index == 0:
            return self.head

        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next

            return current_node

    # Temporary traverse function for debugging
    def traverse(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.key, ':', current_node.value)
            current_node = current_node.next


class Dictionary:
    def __init__(self):
        self.size = 0
        self.n = 0
        self.buckets = self.__make_buckets()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __str__(self):
        result = ''
        for i in self.buckets:
            node = i.return_node_at_index(0)
            if node is None:
                continue
            else:
                while node is not None:
                    if type(node.key) in (int, float) and type(node.value) in (int, float):
                        result += str(node.key) + ': ' + str(node.value) + ', '

                    elif type(node.key) in (int, float) and type(node.value) not in (int, float):
                        result += str(node.key) + ': ' + '\'' + str(node.value) + '\', '

                    elif type(node.key) not in (int, float) and type(node.value) in (int, float):
                        result += '\'' + str(node.key) + '\'' + ': ' + str(node.value) + ', '

                    else:
                        result += '\'' + str(node.key) + '\'' + ': ' + '\'' + str(node.value) + '\', '
                    node = node.next

        return '{' + result[:-2] + '}'

    def __make_buckets(self):
        temp_arr = []
        self.size += 4

        for i in range(self.size):
            temp_arr.append(LinkedList())

        return temp_arr

    def __hash_function(self, key):
        return abs(hash(key)) % self.size

    # Dynamically increases the size of the dictionary
    def __rehash(self):
        temp_buckets = self.buckets
        self.buckets = self.__make_buckets()
        self.n = 0

        for i in range(self.size - 4):
            node = temp_buckets[i].return_node_at_index(0)
            while node is not None:
                self.put(node.key, node.value)
                node = node.next

    def put(self, key, value):
        bucket_index = self.__hash_function(key)

        # Index of key if key is present
        index = self.buckets[bucket_index].find_key(key)

        if index is None:
            load_factor = self.n / self.size
            if load_factor >= 2:
                self.__rehash()

            self.buckets[bucket_index].insert(key, value)
            self.n += 1

        else:
            key_node = self.buckets[bucket_index].return_node_at_index(index)
            key_node.value = value

    def get(self, key):
        bucket_index = self.__hash_function(key)

        # Index of the key if key is present
        index = self.buckets[bucket_index].find_key(key)

        if index is not None:
            node = self.buckets[bucket_index].return_node_at_index(index)
            return node.value

        else:
            print('Key not in Dictionary')

    def remove(self, key):
        bucket_index = self.__hash_function(key)

        # Index if key is present
        status = self.buckets[bucket_index].remove(key)

        if status == -1:
            print('Key not in Dictionary')

        else:
            self.n -= 1
D1['i'] = 8

print(D1)
