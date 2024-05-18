import unittest

class MiTestCase(unittest.TestCase):
    
    def test_num(self):
        self.assertEqual(2, 2)
        
    def test_str(self):
        self.assertEqual('pepe', 'pepe')
    
    @unittest.skip('demostrando skipping')
    def test_bool(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()