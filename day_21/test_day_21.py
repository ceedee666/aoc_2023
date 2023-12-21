import unittest
from unittest import TestCase

import day_21

test_string = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


class Testing(TestCase):
    def test_part_1(self):
        start, grid, _, _ = day_21.parse_input(test_string.split("\n"))
        result = day_21.solve_part_1(start, grid, 6)
        self.assertEqual(result, 16, "The result should be 16.")


if __name__ == "__main__":
    unittest.main()
