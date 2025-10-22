"""
Reto 3: Gestor de tareas con DoublyLinkedList.

Funciones a implementar (usa DoublyLinkedList de estructuras/linkedlist.py):
    - add_task(id:int, descripcion:str, prioridad:int) -> None
    - find_by_id(id:int) -> dict|None
    - find_by_priority(prioridad:int) -> list[dict]

Nota:
- La lista interna debe almacenar dicts con llaves: id, descripcion, prioridad.
"""

from estructuras.linkedlist import DoubleLinkedList

_lista_tareas = DoubleLinkedList()

def add_task(task_id: int, descripcion: str, prioridad: int) -> None:
    _lista_tareas.append({
        'id': task_id,
        'descripcion': descripcion,
        'prioridad': prioridad
    })

def find_by_id(task_id: int):
    return _lista_tareas.find_by_id(task_id)

def find_by_priority(prioridad: int):
    return _lista_tareas.find_by_prioridad(prioridad)

def remove_task(task_id: int) -> None:
    _lista_tareas.remove_by_id(task_id)
