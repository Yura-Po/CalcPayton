import unittest
from Calc import add, subt, multi, division

class TestCalc(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(subt(1, 2), -1)
        self.assertEqual(multi(1, 2), 2)
        self.assertEqual(division(1, 2), 0.5)

if __name__ == "__main__":
    unittest.main()
