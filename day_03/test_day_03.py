import unittest
from unittest import TestCase

import day_03

test_string = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class Testing(TestCase):
    def test_part_1(self):
        r = day_03.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            4361,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = day_03.solve_part_2(test_string.split("\n"))

        self.assertEqual(
            467835,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
