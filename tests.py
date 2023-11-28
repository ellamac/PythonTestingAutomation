import unittest

# code.py has the functions for add, multiply and power
from code import add, multiply, power


class TestMathMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -2), -1)
        with self.assertRaises(TypeError):
            add("1", 2)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)
        self.assertNotEqual(multiply(1, 0), 1)
        self.assertEqual(multiply(-3, 4), -12)
        with self.assertRaises(TypeError):
            multiply("1", 2)

    def test_power(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(-2, 8), 256)
        with self.assertRaises(TypeError):
            power("1", 2)


if __name__ == "__main__":
    unittest.main()
