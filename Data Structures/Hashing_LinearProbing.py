# __gold-init__
# Dictionary implementation using hashing and linear probing

class Dictionary:
    def __init__(self):
        self.__keys = None
        self.__values = None
        self.__size = 0
        self.__n = 0
        self.__make_array()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __str__(self):
        result = ''

        for i in range(self.__size):
            if self.__keys[i] is not None:
                result += str(self.__keys[i]) + ': ' + str(self.__values[i]) + ', '

        return '{' + result[:-2] + '}'

    # Private functions
    def __make_array(self):
        self.__size += 4
        self.__keys = [None] * self.__size
        self.__values = [None] * self.__size
        self.__n = 0

    def __hash(self, key):
        return abs(hash(key)) % self.__size

    def __rehash(self, old_hash):
        return (old_hash + 1) % self.__size

    def __linear_probe(self, key):
        hash_value = self.__hash(key)
        start = hash_value
        while self.__keys[hash_value] is not None and self.__keys[hash_value] != key:
            hash_value = self.__rehash(hash_value)
            if hash_value == start:
                return -1

        return hash_value

    def __resize_dictionary(self):
        temp_keys = self.__keys
        temp_values = self.__values
        self.__make_array()
        for i in range(self.__size - 4):
            self.put(temp_keys[i], temp_values[i])

    # Public functions
    def put(self, key, value):
        hash_value = self.__hash(key)

        # Hash index is empty
        if self.__keys[hash_value] is None:
            self.__keys[hash_value] = key
            self.__values[hash_value] = value
            self.__n += 1

        # Key at hash index
        elif self.__keys[hash_value] == key:
            self.__values[hash_value] = value

        else:
            hash_value = self.__linear_probe(key)

            # Resize dictionary
            if hash_value == -1:
                self.__resize_dictionary()
                self.put(key, value)

            # Hash index is empty
            elif self.__keys[hash_value] is None:
                self.__keys[hash_value] = key
                self.__values[hash_value] = value
                self.__n += 1

            # Key at hash index
            else:
                self.__values[hash_value] = value

    def get(self, key):
        hash_value = self.__hash(key)

        if self.__keys[hash_value] == key:
            return self.__values[hash_value]

        else:
            hash_value = self.__linear_probe(key)

            if hash_value == -1 or self.__keys[hash_value] is None:
                print('Key not in dictionary')
                return None

            else:
                return self.__values[hash_value]

    def remove(self, key):
        hash_value = self.__hash(key)

        if self.__keys[hash_value] == key:
            self.__keys[hash_value] = None
            self.__values[hash_value] = None
            self.__n -= 1

        else:
            hash_value = self.__linear_probe(key)

            if hash_value == -1:
                print('Key not in dictionary')

            else:
                self.__keys[hash_value] = None
                self.__values[hash_value] = None
                self.__n -= 1
