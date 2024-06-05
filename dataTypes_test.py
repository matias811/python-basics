import unittest
from unittest.mock import patch
from io import StringIO
from dataTypes import print_user_name


class TestPrintUserName(unittest.TestCase):
    def test_print_user_name(self):
        # Capture the output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_user_name("Alice")
            # Check the output
            self.assertEqual(fake_out.getvalue(), "Alice\n\n")


if __name__ == '__main__':
    unittest.main()

