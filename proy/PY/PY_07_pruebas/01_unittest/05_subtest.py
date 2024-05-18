import unittest

class MiTestCase(unittest.TestCase):

    def test_assertEqual(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0, 'el número ' + str(i) + ' no es PAR')


if __name__ == '__main__':
    unittest.main()