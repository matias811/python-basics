import unittest
from trickyCounter import tricky_counter


class TestTrickyCounter(unittest.TestCase):

    def test_tricky_counter(self):
        number_of_items = tricky_counter([1, 2, 36, 54, 31, 23])
        self.assertEqual(number_of_items, 147)


if __name__ == '__main__':
    unittest.main()
