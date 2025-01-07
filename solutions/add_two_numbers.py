t
from solutions.add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -2), -3)

    def test_mixed_numbers(self):
        self.assertEqual(add_numbers(-1, 2), 1)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(add_numbers(10**6, 10**6), 2 * 10**6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_numbers("1", 2)


if __name__ == "__main__":
    unittest.main()
