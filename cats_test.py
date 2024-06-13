import unittest
from io import StringIO
from unittest.mock import patch
from cats import get_older_cat, Cat


class TestCats(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_get_older_cat(self, mock_stdout):
        cat1 = Cat('Michy', 15)
        cat2 = Cat('Peluca', 18)
        cat3 = Cat('Blanco y Negro', 19)
        get_older_cat(cat1, cat2, cat3)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Blanco y Negro is the oldest cat, at 19 years old')
