import unittest
from unittest import TestCase

import day_18

test_string = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


class Testing(TestCase):
    def test_part_1(self):
        dirs = day_18.parse_input(test_string.split("\n"))
        result = day_18.solve(dirs)
        self.assertEqual(result, 62, "The result should be 62.")

    def test_part_2(self):
        dirs = day_18.parse_input_2(test_string.split("\n"))
        result = day_18.solve(dirs)
        self.assertEqual(result, 952408144115, "The result should be 952408144115.")


if __name__ == "__main__":
    unittest.main()
