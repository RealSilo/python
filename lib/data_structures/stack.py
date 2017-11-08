class Stack:
    def __init__(self):
        self.store = []

    def push(self, data):
        self.store.append(data)

    def pop(self):
        result = self.store.pop()
        return result

    def peek(self):
        return self.store[-1]

    def is_empty(self):
        return False if self.store else True

    def size(self):
        return self.store.__len__()


if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(3)
    print(s.pop())
    print(s.store)
    print(s.peek())
