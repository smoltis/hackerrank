import unittest
from test_python3 import main


class TestPython3(unittest.TestCase):
    """Test main function for exceptions"""
    def test_main_function(self):
        self.assertRaises(IndexError, main("test"))



unittest.main()