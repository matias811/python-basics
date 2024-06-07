import unittest
from unittest.mock import patch
from io import StringIO
from passwordChecker import check_password


class TestPasswordChecker(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_password_checker(self, mock_stdout):
        check_password("username", "password")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hey username, your password ******** is 8 letters long.")


if __name__ == '__main__':
    unittest.main()
