class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.size = 1
        self.head = Node(data)

    def add(self, data):
        node = Node(data)

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node
        self.size += 1

    def remove(self, data):
        current = self.head
        prev = None

        if current.data == data:
            self.head = current.next
            self.size -= 1
            return current

        while current is not None:
            if current.data == data:
                prev.next = current.next
                self.size -= 1
                return current

            prev = current
            current = current.next

    def find(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current
            current = current.next

        return None


linked_list = LinkedList(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.remove(3)
print(linked_list.find(4).data, linked_list.size)
