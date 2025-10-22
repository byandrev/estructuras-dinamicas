"""
Reto 2: Simulador de atención usando Queue (FIFO).

Clase a implementar:
    class QueueManager:
        - add_person(nombre: str, tiempo: int) -> None
        - serve_person() -> tuple[str, int]   # (nombre, tiempo)
        - state() -> list[str]                # nombres en orden FIFO

Reglas:
- 'agregar_persona' encola al final.
- 'atender_persona' desencola y retorna la tupla; si está vacía, lanza IndexError.
- 'estado' retorna los nombres en el orden actual sin mutar la cola.

Tips:
- Usa Queue de estructuras/queue.py
"""

from estructuras.queue import Queue

class QueueManager:
    # TODO: implementar usando Queue internamente.
    def __init__(self):
        self.queue = Queue()

    def add_person(self, nombre: str, tiempo: int) -> None:
        self.queue.enqueue((nombre, tiempo))

    def serve_person(self) -> tuple[str, int]:
        nombre, tiempo = self.queue.dequeue()
        return (nombre, tiempo)

    def state(self) -> list[str]:
        head = self.queue.head
        result = []

        while head is not None:
            result.append(head.value[0])
            head = head.next

        return result

