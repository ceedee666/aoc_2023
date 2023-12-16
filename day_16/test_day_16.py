import unittest
from unittest import TestCase

import day_16

test_string = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


class Testing(TestCase):
    def test_part_1(self):
        result = day_16.solve_part_1(test_string.split("\n"))
        self.assertEqual(result, 46, "There should be 46 energized tiles.")

    def test_part_2(self):
        result = day_16.solve_part_2(test_string.split("\n"))
        self.assertEqual(result, 51, "There should be a maximum of 51 energized tiles.")


if __name__ == "__main__":
    unittest.main()
