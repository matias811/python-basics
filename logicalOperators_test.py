import unittest
from io import StringIO
from unittest.mock import patch
from logicalOperators import check_class


class TestLogicalOperators(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_false_magician(self, mock_stdout):
        is_magician = False
        is_expert = False
        check_class(is_magician, is_expert)
        self.assertEqual(mock_stdout.getvalue().strip(), "You need magic powers")

    @patch('sys.stdout', new_callable=StringIO)
    def test_noob_magician(self, mock_stdout):
        is_magician = True
        is_expert = False
        check_class(is_magician, is_expert)
        self.assertEqual(mock_stdout.getvalue().strip(), "You are getting there")

    @patch('sys.stdout', new_callable=StringIO)
    def test_master_magician(self, mock_stdout):
        is_magician = True
        is_expert = True
        check_class(is_magician, is_expert)
        self.assertEqual(mock_stdout.getvalue().strip(), "You are a Master Magician")


if __name__ == '__main__':
    unittest.main()
