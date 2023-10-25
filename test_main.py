import unittest
from main import add, subtract

class TestMainFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 2), 8)

if __name__ == '__main__':
    unittest.main()
