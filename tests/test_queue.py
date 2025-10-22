import unittest
from retos.reto2_queue import QueueManager

class TestChallenge2Queue(unittest.TestCase):
    def test_serve_in_fifo_order(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Ana")
        self.assertEqual(tiempo, 5)

    def serve_person(self):
        gestor = QueueManager()

        with self.assertRaises(IndexError):
            gestor.serve_person()

    def test_status(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        gestor.serve_person()
        state = gestor.state()

        self.assertEqual(state, ["Luis"])

    def test_full(self):
        gestor = QueueManager()
        gestor.add_person("Andres", 5)
        gestor.add_person("Alessandro", 3)
        gestor.add_person("Orlando", 8)

        gestor.serve_person()
        gestor.serve_person()

        gestor.add_person("Mauricio", 1)

        state = gestor.state()

        self.assertEqual(state, ["Andres", "Mauricio"])


if __name__ == "__main__":
    unittest.main()
