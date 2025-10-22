import unittest
from retos.reto3_linkedlist import add_task, find_by_id, find_by_priority, remove_task

class TestChallenge3LinkedList(unittest.TestCase):
    def test_add_and_find_by_id(self):
        add_task(1, "Probar DLL", 2)
        tarea = find_by_id(1)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea.id, 1)
        self.assertEqual(tarea.descripcion, "Probar DLL")
        self.assertEqual(tarea.prioridad, 2)

    def test_remove_by_id(self):
        add_task(2, "Tarea a eliminar", 3)
        tarea = find_by_id(2)
        self.assertIsNotNone(tarea)
        remove_task(2)
        tarea_eliminada = find_by_id(2)
        self.assertIsNone(tarea_eliminada)

    def test_remove_headl(self):
        add_task(5, "Tarea cabeza", 1)
        add_task(6, "Tarea cola", 2)
        remove_task(5)
        tarea_cabeza = find_by_id(5)
        self.assertIsNone(tarea_cabeza)

    def test_remove_tail(self):
        add_task(7, "Tarea cabeza", 1)
        add_task(8, "Tarea cola", 2)
        remove_task(8)
        tarea_cola = find_by_id(8)
        self.assertIsNone(tarea_cola)

    def test_find_by_priority(self):
        add_task(3, "Tarea prioridad alta", 1)
        add_task(4, "Tarea prioridad alta", 1)
        tareas_prioridad_alta = find_by_priority(1)
        self.assertEqual(len(tareas_prioridad_alta), 2)
        self.assertTrue(tareas_prioridad_alta[0].id in [3, 4])
        self.assertTrue(tareas_prioridad_alta[1].id in [3, 4])

    def test_find_by_id_nonexistent(self):
        tarea = find_by_id(999)
        self.assertIsNone(tarea)

if __name__ == "__main__":
    unittest.main()
