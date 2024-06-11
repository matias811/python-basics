import unittest
from duplicates import find_duplicates
from duplicates import find_duplicates_v2


class TestDuplicates(unittest.TestCase):

    def test_find_duplicates(self):
        chars_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
        expected_list = ['b', 'n']
        result = find_duplicates(chars_list)
        self.assertEqual(expected_list, result)

    def test_find_duplicates_v2(self):
        chars_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
        expected_list = ['b', 'n']
        result = find_duplicates_v2(chars_list)
        self.assertEqual(expected_list, result)
