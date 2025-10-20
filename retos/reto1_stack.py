"""
Reto 1: Validador de expresión usando Stack.
Paréntesis válidos: (), {}, []

Función a implementar:
    validate_expression(expression: str) -> bool

Reglas:
- Recorre la cadena; apila aperturas; ante un cierre, desapila y compara.
- Si al final la pila queda vacía y nunca hubo desajuste -> True.

Tips:
- Usa Stack de estructuras/stack.py
"""

from estructuras.stack import Stack

PARES = {')': '(', '}': '{', ']': '['}
OPENINGS = ["(", "{", "["]
ENDINGS = [")", "}", "]"]

def validate_expression(expression: str) -> bool:
	# TODO: Implementar con Stack siguiendo las reglas de arriba.
	# Debe ser O(n) en tiempo; O(n) espacio peor caso.
	stack_structures = Stack()
	
	for item in expression:
		if item in OPENINGS:
			stack_structures.push(item)
		elif item in ENDINGS:
			if stack_structures.size() == 0:
				return False
			else:
				if stack_structures.peek() == PARES[item]:
					popped = stack_structures.pop()
	
	return stack_structures.is_empty()
