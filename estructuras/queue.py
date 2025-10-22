"""
Queue (Cola) implementada con lista doblemente enlazada.

TODO:
- Implementa DoubleNode (value, prev, next)
- Implementa Queue con operaciones: enqueue, dequeue, peek, is_empty, size
- Enqueue al final (tail) y dequeue al inicio (head) para O(1)

Sugerencia:
- Mantén punteros a head y tail, más un contador.
"""

class DoubleNode:
    def __init__(self, next, prev, value):
        self.next = next
        self.prev = prev
        self.value = value

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # TODO: implementar cola enlazada doble
    def enqueue(self, value):
        new_node = DoubleNode(None, None, value)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")

        data = self.head.value
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self.length -= 1

        return data

    def peek(self):
        if self.is_empty():
            raise IndexError

        return self.tail.value

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length
