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
    ef __init__(self, next, prev, value):
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
        """Inserta al final. O(1)"""
        raise NotImplementedError

    def dequeue(self):
        """Extrae el primero. O(1). Debe lanzar IndexError si está vacía."""
        raise NotImplementedError

    def peek(self):
        """Retorna el primero sin extraer. O(1). IndexError si vacía."""
        if self.is_empty():
            raise IndexError

        return self.tail.value

    def is_empty(self):
        """True si la cola está vacía. O(1)"""
        return self.length == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self.length
