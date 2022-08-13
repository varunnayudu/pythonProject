import unittest
import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from main import fetch_data_from_file



class TestMain(unittest.TestCase):
    def test_fetch_data_from_file(self):
        result = fetch_data_from_file("input.txt")
        self.assertEqual(True, result.)  # add assertion here


if __name__ == '__main__':
    unittest.main()



