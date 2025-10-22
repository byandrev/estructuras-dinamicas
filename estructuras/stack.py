"""
Stack (Pila) implementado con lista enlazada simple.

TODO:
- Implementa Node (valor, next)
- Implementa Stack con operaciones: push, pop, peek, is_empty, size
- Garantiza que push y pop sean O(1)

Sugerencia:
- Mantén referencia a la "cabeza" (top) y un contador de tamaño.
"""

class Node:
	def __init__(self, next, value):
		self.next = next
		self.value = value

class Stack:
	def __init__(self):
		self.head = None
		self.length = 0

	# TODO: implementar pila enlazada
	def push(self, value):
		"""Inserta en el tope. O(1)"""
		temp = None

		if self.is_empty():
			self.head = Node(None, value)
		else:
			newNode = Node(None, value)
			newNode.next = self.head
			self.head = newNode

		self.length += 1

	def pop(self):
	    """Extrae y retorna el tope. O(1). Debe lanzar IndexError si está vacía."""
	    if self.is_empty():
	        raise IndexError

	    popped_node = self.head
	    self.head = self.head.next
	    popped_node.next = None
	    self.length -= 1

	    return popped_node.value

	def peek(self):
		"""Retorna el tope sin extraer. O(1). IndexError si vacía."""
		if self.is_empty():
			raise IndexError

		return self.head.value

	def is_empty(self):
		"""True si no hay elementos. O(1)"""
		return self.length == 0

	def size(self):
		"""Cantidad de elementos. O(1)"""
		return self.length
