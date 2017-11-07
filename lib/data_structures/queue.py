class Queue:
    def __init__(self):
        self.store = []

    def queue(self, data):
        self.store.insert(0, data)

    def dequeue(self):
        result = self.store.pop()
        return result

    def size(self):
        return self.store.__len__()

    def is_empty(self):
        return False if self.store else True
