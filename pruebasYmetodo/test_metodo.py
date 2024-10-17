import unittest

from metodo import sumar  

class TestSumar(unittest.TestCase):
    def test_suma_numeros_positivos(self):
        self.assertEqual(sumar(3, 5), 8)
    
    def test_suma_numeros_negativos(self):
        self.assertEqual(sumar(-3, -5), -8)

    def test_suma_cero(self):
        self.assertEqual(sumar(0, 0), 0)

    def test_suma_mixta(self):
        self.assertEqual(sumar(-3, 5), 2)
    
    def test_suma_decimales(self):
        self.assertAlmostEqual(sumar(3.5, 2.1), 5.6)

    def test_valor_no_numerico(self):
        with self.assertRaises(ValueError):
            sumar("a", 2)

    def test_ambos_no_numericos(self):
        with self.assertRaises(ValueError):
            sumar("a", "b")

if __name__ == "__main__":
    unittest.main()
