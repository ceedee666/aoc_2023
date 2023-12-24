import unittest
from unittest import TestCase

import day_24

test_string = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


class Testing(TestCase):
    def test_part_1(self):
        stones = day_24.parse_input(test_string.split("\n"))
        self.assertEqual(
            day_24.solve_part_1(stones, 7, 27), 2, "The result should be 2."
        )

    def test_part_2(self):
        stones = day_24.parse_input(test_string.split("\n"))
        self.assertEqual(day_24.solve_part_2(stones), 47, "The result should be 47.")


if __name__ == "__main__":
    unittest.main()
