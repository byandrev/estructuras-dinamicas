import unittest
from retos.reto1_stack import validate_expression

class TestChallenge1Stack(unittest.TestCase):
    def test_simple_balanced_expression(self):
        # Arrange
        expresion = "({[]})"
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertTrue(resultado)
    
    def extra_closure_imbalance(self):
        expresion = "({[]}))"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)
        
    def incorrect_order(self):
        expresion = "{[}]"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)
        
    def empty_string(self):
        expresion = ""
        resultado = validate_expression(expresion)
        self.assertTrue(resultado)
        
    def only_openings(self):
        expresion = ""
        resultado = validate_expression(expresion)
        self.assertTrue(resultado)
        
    def single_type(self):
        expresion = "{}"
        resultado = validate_expression(expresion)
        self.assertTrue(resultado)
        

if __name__ == "__main__":
    unittest.main()
