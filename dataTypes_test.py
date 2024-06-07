import unittest
from unittest.mock import patch
from io import StringIO
from dataTypes import print_user_name


class TestPrintUserName(unittest.TestCase):
    def test_print_user_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_user_name("Alice")
            self.assertEqual(fake_out.getvalue(), "Alice\n\n")

    def test_print_user_name_two(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print_user_name('Carlos')
            self.assertEqual(fake_output.getvalue(), 'Carlos\n\n')


if __name__ == '__main__':
    unittest.main()
