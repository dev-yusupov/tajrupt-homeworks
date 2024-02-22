import unittest
from unittest.mock import patch
from sum1 import sum_numbers
import io
import sys

class TestProblem1(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[5, 3])
    def test_sum(self, mock_input, mock_stdout):
        sum_numbers()
        self.assertEqual(mock_stdout.getvalue(), '8\n')
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[5, 5])
    def test_sum_second(self, mock_input, mock_stdout):
        sum_numbers()
        self.assertEqual(mock_stdout.getvalue(), '10\n')


if __name__ == "__main__":
    unittest.main()