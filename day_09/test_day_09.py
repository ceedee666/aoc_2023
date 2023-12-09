import unittest
from unittest import TestCase

import day_09

test_string = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


class Testing(TestCase):
    def test_part_1(self):
        result = day_09.solve_part_1(test_string.split("\n"))
        self.assertEqual(result, 114, "The result should be 114.")

    def test_part_2(self):
        result = day_09.solve_part_2(test_string.split("\n"))
        self.assertEqual(result, 2, "The result should be 2.")


if __name__ == "__main__":
    unittest.main()
