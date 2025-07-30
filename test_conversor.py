import unittest
from cambio_de_moneda import *

class Test_conversor (unittest.TestCase):
    def test_correcto(self):
        moneda_actual = 'USD'
        moneda_convert = 'ARS'
        monto = 100
        self.assertEqual(conversor(moneda_actual,monto,moneda_convert), 129655)

    def test_actual_incorrecta(self):
        moneda_actual = 'UR'
        moneda_convert = "USD"
        monto = 1000
        self.assertEqual(conversor(moneda_actual,monto,moneda_convert), None)

    def test_convert_incorrecta(self):
        moneda_actual = 'ARS'
        moneda_convert = "UR"
        monto = 1000
        self.assertEqual = (conversor(moneda_actual,monto,moneda_convert), None)

if __name__ == "__main__":
    unittest.main()