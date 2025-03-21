import unittest
from src.calculator import addition, subtraction, multiplication, divide

"""
Esta clase nos va a dar una serie de funcionalidades que nos van a permitir ver el progreso de 
las pruebas, qué prueba se ejecutó, qué prueba falló, por qué falló
comando en terminal para ejecutar las pruebas: python -m unittest discover -s tests  # -s es para indicar la carpeta donde están los tests
"""
class CalculatorTest(unittest.TestCase):
    
    def test_addition(self):
        assert addition(2, 3) == 5
    
    def test_subtraction(self):
        assert subtraction(10, 5) == 5
    
    def test_multiplication(self):
        assert multiplication(2, 4) == 8
    
    # def test_division(self):
    #     assert division(30, 2) == 15
    def test_divide(self):
        result = divide(10, 2)
        expected = 5
        assert result == expected
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(30, 0)