import unittest
from unittest.mock import patch
from io import StringIO
from firstGUI import draw


class TestFirstGUI(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_gui(self, mock_stdout):
        draw()


if __name__ == '__main__':
    unittest.main()