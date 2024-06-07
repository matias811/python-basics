import unittest
from birthYearToAge import calculate_age


class TestCalculateAge(unittest.TestCase):
    def test_calculate_age(self):
        age = calculate_age(1997)
        self.assertEqual(age, 26)


if __name__ == '__main__':
    unittest.main()
