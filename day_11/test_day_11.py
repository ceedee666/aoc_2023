import unittest
from unittest import TestCase

import day_11

test_string = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


class Testing(TestCase):
    def test_part_1(self):
        galaxies = day_11.parse_input(test_string.split("\n"))
        result = day_11.solve(galaxies)
        self.assertEqual(result, 374, "The sum of shortest paths shoot should be 374.")

    def test_part_2(self):
        galaxies = day_11.parse_input(test_string.split("\n"), 10)
        result = day_11.solve(galaxies)
        self.assertEqual(
            result, 1030, "The sum of shortest paths shoot should be 1030."
        )

        galaxies = day_11.parse_input(test_string.split("\n"), 100)
        result = day_11.solve(galaxies)
        self.assertEqual(
            result, 8410, "The sum of shortest paths shoot should be 8410."
        )


if __name__ == "__main__":
    unittest.main()
