import unittest

class MiTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('En setUpClass')

    def setUp(self):
        print('En setUp')
    
    def test_ok(self):
        self.assertEqual(2, 2)
        
    def test_fail(self):
        self.assertEqual(2, 3)
        
    def tearDown(self):
        print('En tearDown')

    @classmethod
    def tearDownClass(cls):
        print('En tearDownClass')
        
if __name__ == '__main__':
    unittest.main()