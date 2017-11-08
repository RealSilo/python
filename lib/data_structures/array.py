class DynamicArray:
    def __init__(self, capacity=1):
        self.store = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def append(self, val):
        def resize():
            self.capacity *= 2
            new_store = [None] * self.capacity

            for i, s in enumerate(self.store):
                new_store[i] = self.store[i]

            self.store = new_store

        self.store[self.size] = val
        self.size += 1

        if self.size == self.capacity:
            resize()

    def pop(self):
        result = self.store.pop
        return result


if __name__ == '__main__':
    da = DynamicArray()
    for i in range(5):
        da.append(i)

    print(da.store)
