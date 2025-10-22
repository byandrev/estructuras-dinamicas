# Estructuras Dinámicas — Mini Biblioteca + Retos

Este repo contiene una **mini-biblioteca de estructuras** (Stack, Queue, LinkedList) y **3 retos** aplicados. La intención es practicar TDD: primero verás **pruebas unitarias iniciales** que fallan (fase _Red_), luego implementarás el mínimo código para hacerlas pasar (_Green_), y finalmente mejorarás (_Refactor_).

## Estructuras

- `Stack` sobre lista enlazada simple.
- `Queue` sobre lista doblemente enlazada.
- `LinkedList` (doblemente enlazada) con operaciones básicas.

## Retos

- **Reto 1 (Stack):** Validador de paréntesis/llaves/corchetes.
- **Reto 2 (Queue):** Simulador de cola de atención (FIFO).
- **Reto 3 (LinkedList):** Gestor de tareas (insertar, eliminar, buscar, recorrer).

## Cómo ejecutar pruebas

```bash
python -m unittest -v
```

## Sugerencias

- Sigue el patrón AAA (Arrange, Act, Assert) en las pruebas.
- Agrega más casos (bordes, errores esperados).
- Documenta complejidades Big-O en los READMEs de cada carpeta.

### Breve descripción

- Stack (lista enlazada simple): LIFO; almacena elementos con push/pop/peek. Implementación con nodo cabeza (top).
- Queue (lista doblemente enlazada): FIFO; operaciones enqueue/dequeue/peek con punteros a head/tail.
- LinkedList (doblemente enlazada): lista con referencias prev/next; soporta insertar al inicio/final, insertar en índice, eliminar por índice, buscar y recorrer.

### Retos

- Reto 1 — Validador de paréntesis: comprueba balance y orden de (), {}, []. Usa un Stack para validar expresiones.
- Reto 2 — Simulador de cola de atención: modela llegada/atención de clientes con Queue.
- Reto 3 — Gestor de tareas: usa LinkedList para insertar, eliminar, buscar y listar tareas.

### Complejidad temporal (operaciones principales)

Stack (singly-linked)

- push: O(1)
- pop: O(1)
- peek/top: O(1)
- O(n)

Queue (doubly-linked)

- enqueue: O(1)
- dequeue: O(1)
- peek/front: O(1)
- recorrer/tamaño: O(n)

LinkedList (doublemente enlazada)

- insertar al inicio/fin: O(1)
- insertar en índice i: O(n) (búsqueda + enlace)
- eliminar por valor/índice: O(n)
- buscar: O(n)
- recorrer: O(n)

## Pruebas

<img width="935" height="281" alt="image" src="https://github.com/user-attachments/assets/0b768f51-8371-40c5-b4c1-31eceb568ab1" />
