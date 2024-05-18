"""

unittest:

. Es una libreria de test unitario que viene por defecto con Python.
. Generan assertions, nos va a decir si la prueba PASÓ o FALLÓ.

"""

import unittest

class MiTestCase(unittest.TestCase):
    
    def test_ok(self):
        self.assertEqual(2, 2)
        
    def test_fail(self):
        self.assertEqual(2, 3)
        

if __name__ == '__main__':
    unittest.main()