import unittest

class MiTestCase(unittest.TestCase):
    
    def test_num(self):
        self.assertEqual(2, 2)
        
    def test_str(self):
        self.assertEqual('pepe', 'pepe')
        
    def test_bool(self):
        self.assertEqual(True, True)

def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(MiTestCase('test_num'))
    suite.addTest(MiTestCase('test_str'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())